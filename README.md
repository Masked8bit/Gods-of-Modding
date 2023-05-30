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

## How to use - Windows 10/11
Using Gods of Modding is extremely easy for Windows users. First, install adb on your system. Then download the [latest release](https://github.com/Masked8bit/Gods-of-Modding/releases/latest)'s "GodsOfModdingvx.x.x_Windows.zip" file, extract the zip file, and run the "main.exe" file.

## How to use - Windows 8.1 and older, Linux. MacOS
### NOTE: This project does not officially support Windows 8.1 and older, and support for Linux and MacOS is not certain yet.

## Step 1 - Dependencies
The Python dependencies can be easily installed using pip. Simply download the [latest release](https://github.com/Masked8bit/Gods-of-Modding/releases/latest)'s "GodsOfModdingvx.x.x_Other.zip" file, extract the zip file, and run the command `pip install -r requirements.txt`.

You will need to install adb as well, since that's how we actually connect to your headset. Once you've installed adb, the script should automatically start it for you.

## Step 2 - Running the program
1. Install the dependencies and set them up as described above. You should have the requirements from the latest release installed.
2. Run the `main.py` file in your terminal using the command `python3 main.py`.
3. Follow the instructions given by the program to get an API key. This is used only to download the needed files from mod.io.
4. Use the built-in UI menu to install or uninstall modded Gods of Gravity.
