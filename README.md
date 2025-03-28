# My Course Addition

1. Charging: Looking from the top at the screen, the cable must exit on the right side
2. Remember the device name, e.g. "Bangle.js f415"
3. Connect to smart watch through https://www.espruino.com/ide/#
4. Connect with the icon on the top left (you won't need to connect through your operating system)
5. Upload to storage (database symbol) sensible-icon.js and sensible_settings.json
6. Open sensible.js and "Send to Espruino" (RAM)
7. Activate all the desired features (Heart rate and Accelerometer activated by default)
8. Disconnect from the watch in order to use the python scanner in the next step
9. In the script bangle_scanner.py, change device name to the corresponding one
10. Check that CHARACTERISTIC_UUID is correct (e.g., nRF Connect app on iPhone)
11. Select in notification_handler the data to be printed or stored
12. Remember that the bangle watch only allows one concurrent connection! sometime computer / phone BT restart is necessary


# Sensible

Collect all the sensor data from the Bangle.js 2, display the live readings in menu pages, and broadcast in Bluetooth Low Energy (BLE) advertising packets to any listening devices in range.


## Usage

The advertising packets will be recognised by [Pareto Anywhere](https://www.reelyactive.com/pareto/anywhere/) open source middleware and any other program which observes the standard packet types.  See our [Bangle.js Development Guide](https://reelyactive.github.io/diy/banglejs-dev/) for details.  Also convenient for testing individual sensors of the Bangle.js 2 via the menu interface.

![SensiBLE in Pareto Anywhere](/BangleApps/apps/sensible/screenshot-pareto-anywhere.png)


## Features

Currently implements:
- Accelerometer
- Barometer
- GPS
- Heart Rate Monitor
- Magnetometer

in the menu display, and broadcasts all sensor data readings _except_ acceleration in Bluetooth Low Energy advertising packets as GATT characteristic services.


## Controls

Browse and control sensors using the standard Espruino menu interface.  By default, all sensors _except_ the accelerometer are disabled.  Sensors can be individually enabled/disabled via the menu.  These settings are written to persistent storage (flash) and will be applied each time the SensiBLE app is loaded.


## Requests

[Contact reelyActive](https://www.reelyactive.com/contact/) for support/updates.


## Creator

Developed by [jeffyactive](https://github.com/jeffyactive) of [reelyActive](https://www.reelyactive.com)
