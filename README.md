# Fix Duplicate File Names
This code fixes the Windows file duplicate names. Normally, duplicates are saved as ```(x)``` where ```x``` is the iteration. However, it's sorted only by the first digit, meaning ```1``` will be followed by ```10``` through ```19``` instead of ```2```. Running this script will require you to input the full path of the folder where the files are located and the applicable file extension.

This will convert each iteration to its applicalbe four digit number. Meaning ```(1)``` will be ```0001```, ```(10)``` will be ```0010```, ```(100)``` will be ```0100```, etc.
