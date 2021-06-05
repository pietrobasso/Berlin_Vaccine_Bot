# Berlin_Vaccine_Bot
python bot looking for available appointments at vaccination centers in Berlin
Download and install appropriate python version from https://www.python.org/downloads/
Instructions for Windows devices:
Download python file (berlin_vaccine_bot.py)
Open command prompt from the explorer address bar where you saved the file (howto: https://helpdeskgeek.com/how-to/open-command-prompt-folder-windows-explorer/)
Install requests module by typing in: 
      python -m pip install requests
Run bot by typing in:
      python berlin_vaccine_bot.py
You can stop bot by pressing ctrl+c on the keyboard
For mac, python 3 needs to be set as the default path and requests need to installed following instrucitons here: https://www.geeksforgeeks.org/how-to-install-requests-in-python-for-windows-linux-mac/


When the bot finds an appointment, it opens up a new tab on the active browser where you can choose the date and time and book the slot. The bot also pauses for 30 seconds when it finds an appointment to allow for the booking to complete. It will automatically resume after 30 seconds and keep looking for a slot
