# Snippeter

This tool is used to sample 50 snippets from a specifically formatted excel or csv file.
See SAMPLE_INPUT file in the "input" folder.


## Using this repo

This repo is intended to simply store the code used to build an executable file but
could be used in a command line to actually process data as well.

You must first have Python 3 installed to do this:
https://www.python.org/

Install the requirements:
pip install -r requirements.txt

And then running the main file:
python3 snippeter.py


## Build Information

A simple executable can be generated for use on any machine by doing the following in a command line.

You must first have Python 3 installed to do this:
https://www.python.org/

Install the requirements:
pip install -r requirements.txt

Run pyinstaller to generate executable:
pyinstaller -F snippeter.py

The executable can then be copied from the "dist" folder.

Note: The executable will only work with the type of OS that created it (ie Windows, Mac, or Linux).
So to make it available on a different OS you will need to build with a version of that OS.
