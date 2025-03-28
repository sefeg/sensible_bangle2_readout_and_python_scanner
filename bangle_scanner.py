import asyncio
import csv
import datetime
from bleak import BleakClient, BleakScanner

DEVICE_NAME = "Bangle.js f415"
CHARACTERISTIC_UUID = "6e400003-b5a3-f393-e0a9-e50e24dcca9e"  # Ensure correct UUID format

WRITE_HEART_RATE_TO_FILE = True

async def notification_handler(sender, data):
    """Callback function to handle incoming notifications."""
    try:
        decoded_data = data.decode("utf-8")  # Convert bytes to UTF-8 string

        #print(f"Notification from {sender}: {decoded_data}") # This always prints everything all the time

        data_to_print = ""

        for line in decoded_data.split("\n"):

            #if line.startswith("Heading"):
            #    print(line)
            if "BPM:" in line:
                print(line)
                
                windows_compatible_timestamp = date_time_started.replace(':','_')
                
                if WRITE_HEART_RATE_TO_FILE:
                    with open('heart_rate_' + windows_compatible_timestamp + '.csv', 'a', newline='') as csvfile:
                        hrm_writer = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
                        hrm_writer.writerow(datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S") + " -- " + line.split(":")[1].strip())
            if "BPM Confidence:" in line:
                print(line)

        

    except UnicodeDecodeError:
        print(f"Notification from {sender}: [Unable to decode, raw data: {data.hex()}]")

async def connect_and_listen():
    """Scans for the device, connects, and listens for notifications."""
    print("Scanning for BLE devices...")
    devices = await BleakScanner.discover()
    
    # Find the device by name
    target_device = next((d for d in devices if d.name == DEVICE_NAME), None)
    
    if not target_device:
        print(f"Device '{DEVICE_NAME}' not found.")
        return

    async with BleakClient(target_device.address) as client:
        print(f"Connected to {DEVICE_NAME}")

        # Wait until services are available
        while not client.services:
            await asyncio.sleep(0.1)  # Small delay to allow services to load
        
        # Extract available characteristic UUIDs
        available_characteristics = [
            char.uuid for service in client.services for char in service.characteristics
        ]

        print(available_characteristics) 

        # Check if the characteristic exists
        if CHARACTERISTIC_UUID not in available_characteristics:
            print(f"Characteristic {CHARACTERISTIC_UUID} not found.")
            return

        # Subscribe to notifications
        await client.start_notify(CHARACTERISTIC_UUID, notification_handler)
        print(f"Listening for notifications on {CHARACTERISTIC_UUID}...")

        # Keep running to receive notifications
        try:
            while True:
                await asyncio.sleep(1)
        except KeyboardInterrupt:
            print("\nUser interrupted. Disconnecting...")

        # Stop notifications before exiting
        await client.stop_notify(CHARACTERISTIC_UUID)

# Run the script properly for standalone execution
if __name__ == "__main__":
    date_time_started = datetime.datetime.now().strftime("%m_%d_%Y_%H:%M:%S")
    asyncio.run(connect_and_listen())
