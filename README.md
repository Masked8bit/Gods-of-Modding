# Gods of Modding
A Python tool for easily installing the modded version of the VR game "Gods of Gravity" onto your VR headset.

## Compatibility
Below is a chart for computer OS compatibility.
|Computer OS|Compatible?|Official support?|
|---|---|---|
|Windows 10/11|✅|✅|
|Windows 8/8.1|❓|❌|
|Windows 7 and older|❓|❌|
|Linux|❓|❓|
|macOS|❓|❓|

## Dependencies
The Python dependencies can be easily installed using pip. Simply download the [latest release](https://github.com/Masked8bit/Gods-of-Modding/releases/latest), extract the zip file, and run the command `pip install -r requirements.txt`.

You will need to install adb as well, since that's how we actually connect to your headset. Once you've installed adb, the script should automatically start it for you.

## How to use
1. Install the dependencies and set them up as described above. You should have the requirements from the latest release installed.
2. Run the `main.py` file in your command prompt using the command `python3 main.py` (if that doesn't work, try removing the "3")
3. Follow the instructions given by the program to get an API key. This is used only to download the needed files from mod.io.
4. Use the built-in menu to install or uninstall modded Gods of Gravity.
