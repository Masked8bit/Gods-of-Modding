import requests
from ppadb.client import Client as AdbClient
import os
import json
import urllib.request
import zipfile
from colorama import Fore, Style
import shutil
import tkinter as tk
from tkinter import ttk, Menu

package = "com.TrassGames.GodsOfGravity"
version = "3.0.0"
altver = 5
# fallbackconfig = '{"save_key": "false", "start-adb-auto": "true"}' // saved in case i readd config
if os.name == 'nt':
  win = True
else:
  win = false

headers = {
  'Accept': 'application/json',
  'X-Modio-Platform': 'Oculus'
}

apikey = 0
adbok = 0
client = 0
installed = 0
installbutton = 0
uninstallbutton = 0
headermenu = 0
# global buttons and variables

root = tk.Tk()
root.title(f"Gods of Modding {version}")

def throw_error(msg):
  print(f"\n{Style.BRIGHT}{Fore.RED}ERROR!{Style.RESET_ALL} {msg}")
  exit()

# thanks https://www.pythontutorial.net/tkinter/
window_width = 600
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.resizable(False, False)
if win:
  try:
    root.iconbitmap('./icon.ico')
  except:
    pass

menubar = Menu(root)
root.config(menu=menubar)
file_menu = Menu(menubar, tearoff=False)
help_menu = Menu(menubar, tearoff=False)
file_menu.add_command(label='Exit',command=root.destroy)
help_menu.add_command(label='Check for Updates',state=tk.DISABLED)
menubar.add_cascade(label="File",menu=file_menu)
menubar.add_cascade(label="Help",menu=help_menu)

def install():
  headermenu.destroy()
  installbutton.destroy()
  if(installed):
    uninstallbutton.destroy()
  print(f"{Style.BRIGHT}{Fore.YELLOW}NOTE!{Style.RESET_ALL} The app may appear frozen on the \"Select an option\" page, however it IS working!")
  infolog = ttk.Label(root,text="Uninstalling Gods of Gravity...",justify=tk.CENTER,wraplength=600)
  print(f"{Style.BRIGHT}{Fore.YELLOW}DEBUG!{Style.RESET_ALL} Uninstalling Gods of Gravity...")
  infolog.pack()
  if(installed==True):
    devices = client.devices()
    for device in devices:
      try:
        device.uninstall(package)
      except:
        throw_error("Uninstall failed.")
      for device in devices:
        insta2 = device.is_installed(package)
      if(insta2==True):
        throw_error("Uninstall failed.")
      elif(insta2==False):
        infolog.configure(text="Downloading modded zip file... (1/2)")
        print(f"{Style.BRIGHT}{Fore.YELLOW}DEBUG!{Style.RESET_ALL} Downloading modded zip file... (1/2)")
  else:
    infolog.configure(text="Downloading modded zip file... (1/2)")
    print(f"{Style.BRIGHT}{Fore.YELLOW}DEBUG!{Style.RESET_ALL} Downloading modded zip file... (1/2)")
  r = requests.get('https://api.mod.io/v1/games/5003/mods/2989636/files/3798676', params={'api_key': apikey}, headers = headers)
  ri = r.json()
  try:
    rib = ri["download"]
  except:
    throw_error("The needed file could not be downloaded. You probably put in an invalid API key, try deleting \"DO_NOT_SHARE_THIS_FILE_WITH_ANYBODY_EVER.txt\".")
  ribs = rib["binary_url"]
  infolog.configure(text="Downloading modded zip file... (2/2)")
  print(f"{Style.BRIGHT}{Fore.YELLOW}DEBUG!{Style.RESET_ALL} Downloading modded zip file... (2/2)")
  try:
    urllib.request.urlretrieve(ribs, "build.zip")
  except:
    throw_error("Could not retrieve zip file!")
  infolog.configure(text="Extracting zip file...")
  with zipfile.ZipFile("build.zip", 'r') as zip_ref:
    zip_ref.extractall("moddedapk")
  infolog.configure(text="Installing modded apk...")
  print(f"{Style.BRIGHT}{Fore.YELLOW}DEBUG!{Style.RESET_ALL} Installing modded apk...")
  devices = client.devices()
  for device in devices:
    try:
      prevdir = os.getcwd()
      os.chdir("moddedapk")
      device.install("build.apk")
    except:
      throw_error("An error occured during install. Try:\n- Making sure your headset is in developer mode (enabled in mobile app)\n- Making sure your headset is properly connected\n- You have enough storage space")
    infolog.configure(text="Cleaning up...")
    print(f"{Style.BRIGHT}{Fore.YELLOW}DEBUG!{Style.RESET_ALL} Cleaning up...")
    os.chdir(prevdir)
    try:
      os.remove("build.zip")
      shutil.rmtree("moddedapk")
    except:
      print(f"{Style.BRIGHT}{Fore.YELLOW}NOTE!{Style.RESET_ALL} Something went wrong during cleanup. Everything should be fine.")
    infolog.configure(text="Modded Gods of Gravity installed! Now:\n- Open the game on your headset\n- You will see the Trass Games logo then nothing\n- DO NOT TURN OFF YOUR HEADSET OR EXIT THE APP! Wait for the game to load\n- This will take a few minutes\n- Once you load in, your game should be modded!\n\nIt is now safe to exit the app.")

def uninstall():
  headermenu.destroy()
  installbutton.destroy()
  uninstallbutton.destroy()
  infolog = ttk.Label(root,text="Uninstalling Gods of Gravity...")
  infolog.pack()
  if(installed==True):
    devices = client.devices()
    for device in devices:
      try:
        device.uninstall(package)
      except:
        throw_error("Uninstall failed.")
      for device in devices:
        insta2 = device.is_installed(package)
      if(insta2==True):
        throw_error("Uninstall failed.")
      elif(insta2==False):
        infolog.configure(text="Uninstalled Gods of Gravity!\n\nIt is now safe to exit the app.")

def phase2():
  adbok.destroy()
  loading.pack_forget()
  try:
    global client
    client = AdbClient(host="127.0.0.1", port=5037)
  except:
    throw_error("Couldn't connect to adb.")
  devices = client.devices()
  loading.pack()
  loading.configure(text="Loading... (checking devices)")
  counter = 0
  for device in devices:
    counter += 1
    global installed
    installed = device.is_installed(package)
  if(counter==0):
    throw_error("Couldn't find any connected devices. Make sure your headset is plugged in and developer mode is enabled in the mobile app.")
  elif(counter>=2):
    throw_error("Multiple devices appear to be connected. Please only connect your headset.")
  print(f"{Style.BRIGHT}{Fore.YELLOW}DEBUG!{Style.RESET_ALL} Is installed: {installed}")
  loading.pack_forget()
  global headermenu
  headermenu = ttk.Label(root,text="Select an option below.")
  headermenu.pack()
  global installbutton
  installbutton = ttk.Button(root,text="Install",command=install)
  installbutton.pack()
  if(installed):
    global uninstallbutton
    uninstallbutton = ttk.Button(root,text="Uninstall",command=uninstall)
    uninstallbutton.pack()

def finishapikey():
  if(not os.path.exists("DO_NOT_SHARE_THIS_FILE_WITH_ANYBODY_EVER.txt")):
    global apikey
    apikey = key.get()
    apinote.destroy()
    keybox.destroy()
    enterapikey.destroy()
    keysave = open("DO_NOT_SHARE_THIS_FILE_WITH_ANYBODY_EVER.txt", "w")
    keysave.write(apikey)
    keysave.close()
  loading.pack()
  loading.configure(text="Loading... (connecting to adb)")
  try:
    os.system("adb start-server")
  except:
    try:
      os.system(".\adb start-server")
    except:
      print("Couldn't start adb.")
      exit()
  global adbok
  adbok = ttk.Button(root,text="OK",command=phase2)
  adbok.pack()
  loading.configure(text="An adb server has been automatically started. Please put on your headset and allow USB debugging. Once you're done, hit enter.")

loading = ttk.Label(root,text="",justify=tk.CENTER,wraplength=600)

if(os.path.exists("DO_NOT_SHARE_THIS_FILE_WITH_ANYBODY_EVER.txt")):
  keysave = open("DO_NOT_SHARE_THIS_FILE_WITH_ANYBODY_EVER.txt", "r")
  apikey = keysave.read()
  finishapikey()
else:
  apinote = ttk.Label(root, text="Hello! Thanks for using Gods of Modding. To get started, you'll need to put your API key in. We'll only use this to download the needed files from mod.io. Don't trust us? Look at the code for yourself.\n\nDon't have one?\nTo make one, follow these steps.\n1. Navigate to https://mod.io/me/access in a web browser\n2. Make sure you're logged in to mod.io.\n3. Make an API key, and paste it in here.\n4. DO NOT SHARE THIS API KEY!",justify=tk.CENTER,wraplength=600)
  apinote.pack()
  key = tk.StringVar()
  keybox = ttk.Entry(root,textvariable=key,show="*")
  keybox.pack()
  enterapikey = ttk.Button(root,text="OK",command=finishapikey)
  enterapikey.pack()

os.system('cls' if os.name == 'nt' else 'clear')
print(f"GUI starting!\n{Style.BRIGHT}{Fore.YELLOW}NOTE!{Style.RESET_ALL} To close the program, use the \"x\" button on the window or \"File > Exit\". Do not close the program during install!")
root.mainloop()