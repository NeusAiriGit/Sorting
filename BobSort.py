import random
import matplotlib.pyplot as plt
import numpy as np
import time
from pysinewave import SineWave
import tkinter as tk
from tkinter import ttk


finNum = random.randrange(1,101)

unSorteddList = np.random.choice(range(1, finNum + 1), size=finNum, replace=False)
x = np.arange(0,finNum,1)

print(unSorteddList)
n = len(unSorteddList)

sinewave = SineWave(pitch = 0)
sinewave.set_volume(75)

def bubleSort(unSorteddList,x,n):
    for i in range(0,n):
        pitch = (int(n/12)+i)
        sinewave.set_pitch(pitch)
        sorted_flag = True  
        for j in range(0, n - i - 1):
            bars = plt.bar(x, unSorteddList)
            bars[j].set_color("red")
            plt.pause(0.0001)
            plt.clf()
            if unSorteddList[j] > unSorteddList[j + 1]:
                sorted_flag = False
                unSorteddList[j], unSorteddList[j + 1] = unSorteddList[j + 1], unSorteddList[j]
                sinewave.stop()
        sinewave.play()


def selectionSort(unSorteddList,x,n):
    for i in range(0,n):
        min_idx = i
        pitch = (int(n/12)+i)
        sinewave.set_pitch(pitch)
        sorted_flag = True
        for j in range(i+1, n):
            bars = plt.bar(x, unSorteddList)
            bars[j].set_color("red")
            plt.pause(0.0001)
            plt.clf()
            if unSorteddList[j] < unSorteddList[min_idx]:
                min_idx = j
                sorted_flag = False
                sinewave.stop()
        unSorteddList[i], unSorteddList[min_idx] = unSorteddList[min_idx], unSorteddList[i]
        sinewave.play()


def insertionSort(unSorteddList,x,n):
    for i in range(1, n):
        pitch = (int(n/12)+i)
        sinewave.set_pitch(pitch)
        sorted_flag = True
        key = unSorteddList[i]
        j = i-1
        while j >= 0 and key < unSorteddList[j] :
                bars = plt.bar(x, unSorteddList)
                bars[j].set_color("red")
                plt.pause(0.0001)
                plt.clf()
                unSorteddList[j + 1] = unSorteddList[j]
                j -= 1
                sorted_flag = False
                sinewave.stop()
        unSorteddList[j + 1] = key
        sinewave.play()


def endSec():    
    if True:

        bars = plt.bar(x, unSorteddList)
        for bar in bars:
            bar.set_color("green")
        plt.pause(0.5)
        for times in range(5):
            for i in range(0,n):
                bars[i].set_color("white")
                bars[i-1].set_color("green")
                plt.pause(0.0005)
            bars[-1].set_color("green")
        sinewave.stop()
    plt.close()

def on_select(event):
    selected_item = combo_var.get()

def accept_selection():
    selected_item = combo_var.get()
    selected_variable.set(selected_item)
    combo_box.event_generate('<FocusOut>')
    if selected_item == "Bubble Sort" or selected_item == "Selection Sort" or selected_item == "Insertion Sort":
        root.destroy()
    else:
        print("No Method selected")

# Create the main window
root = tk.Tk()
root.title("Dropdown Selector with Button")

# Create a control variable for the combobox
combo_var = tk.StringVar()

# Create the combobox
combo_box = ttk.Combobox(root, textvariable=combo_var)
combo_box['values'] = ('Bubble Sort', 'Selection Sort', 'Insertion Sort')
combo_box.bind("<<ComboboxSelected>>", on_select)
combo_box.pack(pady=10)

# Button to accept the selection
accept_button = ttk.Button(root, text="Accept Selection", command=accept_selection)
accept_button.pack()

# Label to display the selection
result_label = ttk.Label(root, text="")
result_label.pack()

# Variable to store the selection
selected_variable = tk.StringVar()
selected_label = ttk.Label(root, textvariable=selected_variable)
selected_label.pack()

# Start the main event loop of the application
root.mainloop()

if selected_variable.get() == "Bubble Sort":
    bubleSort(unSorteddList,x,n)
elif selected_variable.get() == "Selection Sort":
    selectionSort(unSorteddList,x,n)
elif selected_variable.get() == "Insertion Sort":
    insertionSort(unSorteddList,x,n)
   
endSec() 
plt.show()

SortedList = unSorteddList.copy()
print("----------------")
print(SortedList)