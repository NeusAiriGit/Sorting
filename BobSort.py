import random
import matplotlib.pyplot as plt
import numpy as np
import time
from pysinewave import SineWave

finNum = random.randrange(1,101)

unSorteddList = np.random.choice(range(1, finNum + 1), size=finNum, replace=False)
x = np.arange(0,finNum,1)

print(unSorteddList)
n = len(unSorteddList)


sinewave = SineWave(pitch = 0)
sinewave.set_volume(75)


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
    
if sorted_flag:

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
  

    
    

plt.show()


SortedList = unSorteddList.copy()
print("----------------")
print(SortedList)