# Hood Availabilty Script

This is a silly little script for checking the hood availability in main TC WHD by using LIVAD MWS credentials to login to SafteyNet programatically and do a quick-and-dirty plot of whether the hood is available or not.

## Setup

You'll need Python installed for this to work. A Javascript version is possible to work as a website but I am not paid enough for that 🤷.

After installing Python, run the following commands:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 do_it.py
```

This makes a virtual environment, enters it, installs the requirements and then runs the script. If something goes wrong, email me!

## Running the script

The script asks for your username and password - these are ~~sent to me to compromise your account~~ only used temporarily in the Python script so should be perfectly safe. Don't believe me? Look at the code! That said, use at your own risk and please don't do anything stupid like use this program as part of any larger work.

## FAQ

* Why?

Because it's a pain to login to SafteyNet just to check if all the hoods are booked in MainTC.

* How?

We use `twill` to login and save the data to JSON, then parse and show the plot using `matplotlib`.

* Help! Something's gone wrong - the plot is lying!

Email me.

* Can you do this for other rooms?

Email me and buy me a coffee.