# Readme.md

> You can check out the process of creating project on the following Youtube Channel: [https://youtu.be/ayQszTHwpJA](https://youtu.be/ayQszTHwpJA)
> 

# Usage

1. Define the path for the log file for saving the keystrokes locally
2. Define the path for the log file for saving the system information locally
3. Have a webserver running to catch the webrequest from the script
4. Run the script!

> Press `Esc` to quit out of the script
> 

# Making executable

1. Install the `pyinstaller` module using pip: `pip install pyinstaller`
2. Move into the same directory as the script
3. Convert to executable using the following command: `pyinstaller -F -w <script name or path to script>`
4. With the `-i` option you can add an icon
5. The executable will be located in the `dist` folder that appears

> Press `Esc` to stop the program
>