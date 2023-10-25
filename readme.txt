Author: Xiangyu(Leo) Shi
Project Start Date: October 18, 2023
Description: This Python script uses numpy and tkinter to create a user interface
for generating trial sequences for fan maze experiments at Dr. Rangel's Lab. (Edit)

Version History:
V0: Oct 18, implemented basic features for trial sequence permutation generating.
V1: Oct 25, added bias feature.


HOW TO USE
0. Download trialSeq.py to Desktop folder

1. Executing trialSeq.py
    a. Open terminal
    b. type in: cd ~/Desktop/
    c. type in: python -m trialSeq.py
        - You may or may not need to download extra packages
            i. type in: pip install numpy
            ii. type in: pip install tkinter

2. Using the application
    Upon executing trialSeq.py, the application window should spawn.
    From top to bottom:
        a. Entry for trial balance factors (i.e. 6 6 12 12 12)
            - Enter 6, 12, 18, or 24 in a sequence with spaces between.
        b. Entry for bias factor
            - Enter -1 for no bias, or 6 - 10 for any bias.
        c. Spawn trials button
            - Generates a random trial sequence given balance factors and bias.
        d. Copy trials button
            - Copies current generated trial sequence to clipboard to paste.
        e. Trial Text-Widget
            - Text box that displays generated trial sequence
        f. Back, Delete, Forward
            - Check last generated sequence
            - Delete current sequence
            - Check next generated sequence

Last Updated: Oct 25, 2023
        