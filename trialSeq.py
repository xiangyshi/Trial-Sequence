"""
Author: Xiangyu(Leo) Shi
Date: October 18, 2023
Description: This Python script uses numpy and tkinter to create a user interface
for generating trial sequences for...

Oct 24 Log: Added bias feature.
Oct 25 Log: Greatly improved permutation efficiency.
"""


import numpy as np
import tkinter as tk

# Trial balances default sequence
six = np.array([(5, 8), (6, 9), (7, 10), (8, 5), (9, 6), (10, 7)])
twelve = np.concatenate((six, six), axis=0)
eighteen = np.concatenate((six, twelve), axis=0)
twentyfour = np.concatenate((twelve, twelve), axis=0)

# Constants and Messages
START_MSG = '''Welcome to Trial Sequence V'''
ERR_MSG = '''Please enter the balance values (6, 12, 18, 24)\nExample:\n6 6 6 12 12'''

# Trial Generation
# Recursively generate trials based on given rule

def isFlip(tup1, tup2):
    if tup1[0] == tup2[1] and tup1[1] == tup2[0]:
        return True
    return False

def getIdx(pair):
    if pair[0] == 5:
        return 0
    elif pair[0] == 6:
        return 1
    elif pair[0] == 7:
        return 2
    elif pair[0] == 8:
        return 3
    elif pair[0] == 9:
        return 4
    elif pair[0] == 10:
        return 5
    else:
        raise Exception("Illegal Bias")

def checkProperty(arr):
    if len(arr) < 2:
        return True
    for i in range(len(arr) - 2):
        if isFlip(arr[i], arr[i+1]) or isFlip(arr[i], arr[i+2]):
            return False
    return True

def balanceBySix():
    np.random.shuffle(six)
    while not checkProperty(six):
        np.random.shuffle(six)
    return six

def balanceByTwelve():
    np.random.shuffle(twelve)
    while not checkProperty(twelve):
        np.random.shuffle(twelve)
    return twelve

def balanceByEighteen():
    np.random.shuffle(eighteen)
    while not checkProperty(eighteen):
        np.random.shuffle(eighteen)
    return eighteen

def balanceByTwentyFour():
    np.random.shuffle(twentyfour)
    while not checkProperty(twentyfour):
        np.random.shuffle(twentyfour)
    return twentyfour

def biasTwelve(pair):
    #bias setup
    bias = pair[0]
    plug = np.array([pair, pair])
    six = np.array([(5, 8), (6, 9), (7, 10), (8, 5), (9, 6), (10, 7)])
    idx = getIdx(pair)
    six = np.delete(six, idx, axis=0)


    twelve = np.concatenate((six, six), axis=0)
    np.random.shuffle(twelve)
    while not checkProperty(twelve):
        np.random.shuffle(twelve)
    
    randIdx = np.random.randint(0, len(twelve))
    twelve = np.insert(twelve, randIdx, plug, axis=0)
    return twelve

def biasEighteen(pair):
    #bias setup
    bias = pair[0]
    plug = np.array([pair, pair, pair])
    six = np.array([(5, 8), (6, 9), (7, 10), (8, 5), (9, 6), (10, 7)])
    idx = getIdx(pair)
    six = np.delete(six, idx, axis=0)

    eighteen = np.concatenate((six, six, six), axis=0)
    np.random.shuffle(eighteen)
    while not checkProperty(eighteen):
        np.random.shuffle(eighteen)
    
    randIdx = np.random.randint(0, len(eighteen))
    eighteen = np.insert(eighteen, randIdx, plug, axis=0)
    return eighteen

def biasTwentyfour(pair):
    #bias setup
    bias = pair[0]
    plug = np.array([pair, pair, pair, pair])
    six = np.array([(5, 8), (6, 9), (7, 10), (8, 5), (9, 6), (10, 7)])
    idx = getIdx(pair)
    six = np.delete(six, idx, axis=0)

    twentyfour = np.concatenate((six, six, six, six), axis=0)
    np.random.shuffle(twentyfour)
    while not checkProperty(twentyfour):
        np.random.shuffle(twentyfour)
    
    randIdx = np.random.randint(0, len(twentyfour))
    twentyfour = np.insert(twentyfour, randIdx, plug, axis=0)
    return twentyfour

def checkBias(arr, pair, k):
    cnt = 0
    for p in arr:
        if cnt == k:
            return True
        if p[0] == pair[0]:
            cnt += 1
        else:
            cnt = 0
    return cnt == k

def permutation(balance, bias):
    pair = (-1, -1)
    if bias == -1:
        if balance == 6:
            return balanceBySix()
        elif balance == 12:
            return balanceByTwelve()
        elif balance == 18:
            return balanceByEighteen()
        elif balance == 24:
            return balanceByTwentyFour()
        else:
            raise Exception("Illegal Balance Factor: " + str(balance))
        
    if bias < 8:
        pair = (bias, bias + 3)
    else:
        pair = (bias, bias - 3)
    
    if balance == 6:
        return balanceBySix()
    elif balance == 12:
        twelve = biasTwelve(pair)
        while not checkProperty(twelve):
            twelve = biasTwelve(pair)
        return twelve
    elif balance == 18:
        eighteen = biasEighteen(pair)
        while not checkProperty(eighteen):
            eighteen = biasEighteen(pair)
        return eighteen
    elif balance == 24:
        twentyfour = biasTwentyfour(pair)
        while not checkProperty(twentyfour):
            twentyfour = biasTwentyfour(pair)
        return twentyfour
    raise Exception("Illegal Balance Factor: " + str(balance))

def balanceTrial(arrstr, bias):
    try:
        b = int(bias)
    except Exception as e:
        text_widget.config(state='normal')
        text_widget.delete(1.0, tk.END)
        text_widget.insert(tk.END, ERR_MSG)
        text_widget.config(state='disabled')
        print('bad bias')
        return [], []

    arr = arrstr.strip().split(' ')
    if len(arr) == 0:
        text_widget.config(state='normal')
        text_widget.delete(1.0, tk.END)
        text_widget.insert(tk.END, ERR_MSG)
        text_widget.config(state='disabled')
        print("len bad")
        return [], []
    
    try:
        arr = [int(i) for i in arr]
    except Exception as e:
        text_widget.config(state='normal')
        text_widget.delete(1.0, tk.END)
        text_widget.insert(tk.END, ERR_MSG)
        text_widget.config(state='disabled')
        print('except')
        return [], []

    total = np.array([])
    for n in arr:
        curr = permutation(n, b)
        if len(total) != 0:
            total = np.concatenate((total, curr), axis=0)
        else:
            total = curr

    if not checkProperty(total):
        return balanceTrial(arrstr, bias)
    return total, arr

def displayTrials(total, arr):
    global history
    global curr_idx

    if len(total) == 0 and len(arr) == 0:
        return
    cnt = 1
    sum = arr[0]
    result = ""
    for i in range(len(total)):
        if cnt <= len(arr) and sum == arr[cnt - 1]:
            if i != 0:
                result += '\n'
            if i == 0:
                result += "Balance by " + str(arr[cnt - 1]) + '\n'
            else:
                result += "Balance by " + str(arr[cnt]) + '\n'
            sum = 0
            cnt += 1
            if i == 0:
                cnt = 1
        result += "Trial #%d: (%d, %d)\n" % (i + 1, total[i][0], total[i][1])
        sum += 1
    text_widget.config(state='normal')
    text_widget.delete(1.0, tk.END)  # Clear the current content
    text_widget.insert(tk.END, result)
    history.append(result)
    curr_idx = len(history) - 1
    text_widget.config(state='disabled')


# History feature
history = []
curr_idx = 0
# Inteface features
def copy_text():
    text_widget.clipboard_clear()
    text_widget.clipboard_append(text_widget.get("1.0", "end"))
    text_widget.update()

# Go back one generation
def back():
    global history
    global curr_idx
    if len(history) == 0:
        return
    if curr_idx <= 0:
        return
    curr_idx -= 1
    text_widget.config(state='normal')
    text_widget.delete(1.0, tk.END)
    text_widget.insert(tk.END, history[curr_idx])
    text_widget.config(state='disabled')

# Go forward one generation
def forward():
    global history
    global curr_idx
    if len(history) == 0:
        return
    if curr_idx >= len(history) - 1:
        return
    curr_idx += 1
    text_widget.config(state='normal')
    text_widget.delete(1.0, tk.END)
    text_widget.insert(tk.END, history[curr_idx])
    text_widget.config(state='disabled')

# Delete current trial history
def delete():
    global history
    global curr_idx
    history.pop(curr_idx)
    text_widget.config(state='normal')
    text_widget.delete(1.0, tk.END)
    text_widget.insert(tk.END, "Cleared")
    text_widget.config(state='disabled')

# User Interface
window = tk.Tk()
window.title('Trial Sequence')
window.geometry("400x1000")

# User entry for trial balance and bias input
entry = tk.Entry(window, width=30)
bias = tk.Entry(window, width=10)

# Generate trial permutation based on entry
spawnTrials = tk.Button(window, text="Spawn Trials", command=lambda: displayTrials(*balanceTrial(entry.get(), bias.get())))

# Copy current trial sequence to clipboard
copy_button = tk.Button(window, text="Copy Trials", command=copy_text)

# Check prev permutation in history
back_button = tk.Button(window, text="< Back", command=back)

# Check next permutation in history
forward_button = tk.Button(window, text="Forward >", command=forward)

# Delete current history
delete_button = tk.Button(window, text="Delete", command=delete)

# Display window for generated permutation
text_widget = tk.Text(window, wrap=tk.WORD, height=45, width=60)
scrollbar = tk.Scrollbar(window, command=text_widget.yview)
text_widget.config(yscrollcommand=scrollbar.set)

# Position organization of components
entry.pack()
bias.pack()
spawnTrials.pack()
copy_button.pack()
text_widget.pack()
back_button.pack()
delete_button.pack()
forward_button.pack()
window.mainloop()

