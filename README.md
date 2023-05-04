# Hood Availabilty Script

This is a silly little script for checking the hood availability in main TC WHD by using LIVAD MWS credentials to login to SafteyNet programatically and do a quick-and-dirty plot of whether the hood is available or not.

## Setup

You'll need Python installed for this to work

After installing Python, run the following commands:

# Linux/MacOS
```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python do_it.py
```
# Windows

For windows a .bat file is included. Navigate to the correct folder and run
 ```bash
 hoods.bat
 ```

This makes a virtual environment, enters it, installs the requirements and then runs the script. If something goes wrong, email me!

## Running the script

The script asks for your username and password - these are ~~sent to me to compromise your account~~ only used temporarily in the Python script so should be perfectly safe. Don't believe me? Look at the code! That said, use at your own risk and please don't do anything stupid like use this program as part of any larger work.

You can change the equipment montiored by changing the values in `config.json` to the equiptment codes as entered in SafetyNet. This is a bit of a pain to do because they might not be exactly the same as on the website. If you want to do this, let me know!