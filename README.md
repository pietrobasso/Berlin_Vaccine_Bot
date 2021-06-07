# Berlin_Vaccine_Bot
This bot looks for available appointments **in the next 14 days** at the following places:
- Berlin Vaccination Centers
- GKH Havelhöhe 

When the bot finds an appointment, it opens up a new tab on the active browser where you can choose the date and time and book the slot. The bot also pauses for 30 seconds when it finds an appointment to allow for the booking to complete. It will automatically resume after 30 seconds and keep looking for a slot **in the next 14 days**.

## Dependencies 
Please install these dependencies before rolling.
- `python3 -m pip install requests`
- `python3 -m pip install asyncio`

Please use Python3. https://www.python.org/downloads/

## Usage
Open your command line and type:

      python3 /path/to/file/berlin_vaccine_bot.py

## Customize
If you're looking for appointments further than 14 days, just change the `goalDate` parameter in the `berlin_vaccine_bot.py` file.


## Instructions for Windows
- Download python file (berlin_vaccine_bot.py)
- Open command prompt from the explorer address bar where you saved the file (howto: https://helpdeskgeek.com/how-to/open-command-prompt-folder-windows-explorer/)

You can stop bot by pressing ctrl+c on the keyboard

## Instructions for Mac
Please install Python 3 and follow the `Usage` section above.
