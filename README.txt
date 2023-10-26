Author: Xiangyu(Leo) Shi
Project Start Date: October 18, 2023

Version History:
V0: Oct 18, implemented basic features for trial sequence permutation generating.
V1: Oct 25, added bias feature.
V2: Oct 25, improved efficiency
V3: Oct 26, added invalid entry directions
V4: Oct 26, added executable

HOW TO USE
0. Make sure you are using MacOS. (Only Mac for now)

1. Download zipfile from Code tab.

1. Executing
    a. Unzip Trial-Sequence-main.zip
    b. Enter Trial-Sequence-main folder
    c. Enter dist folder
    d. Double click executable trialSeq
        - Takes around 20 seconds

2. Using the application
    Upon executing trialSeq, an application window should spawn.
    From top to bottom:
        a. Entry for trial balance factors (i.e. 6 6 12 12 12)
            - Enter 6, 12, 18, or 24 in a sequence with one single space between each factor.
        b. Entry for bias factor
            - Enter -1 for no bias, or 5 - 10 for any bias.
            - The biased trials will be grouped.
        c. Spawn trials button
            - Generates a random trial sequence given balance factors and bias.
        d. Copy trials button
            - Copies current generated trial sequence to clipboard for pasting.
        e. Trial Text-Widget
            - Text box that displays generated trial sequence
        f. Back, Delete, Forward
            - Check last generated sequence
            - Delete current sequence
            - Check next generated sequence

Last Updated: V4 Oct 26, 2023
        
