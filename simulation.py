#this is for randomly generated data instead of the randomly generated data the code can be replaced to connect it to a real time live data source  

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import clear_output
import time
num_points = 60       
delay = 0.5           
threshold = 100        
source_mean = 1000    
timestamps, src_list, end_list, theft_flags = [], [], [], []
print(" Simulating live data... please wait a few seconds.")
for t in range(num_points):
    src = np.random.normal(source_mean, 20)
    end = src - np.random.normal(20, 10)
    if np.random.rand() < 0.1:
        end -= np.random.uniform(120, 250)
    diff = src - end
    theft = 1 if diff > threshold else 0
    timestamps.append(t)
    src_list.append(src)
    end_list.append(end)
    theft_flags.append(theft)
    clear_output(wait=True)
    plt.figure(figsize=(12,6))
    plt.plot(timestamps, src_list, 'b-', linewidth=2, label='Source Flow')
    plt.plot(timestamps, end_list, 'g-', linewidth=2, label='End Flow')
    theft_idx = [i for i, f in enumerate(theft_flags) if f == 1]
    theft_src = [src_list[i] for i in theft_idx]
    theft_end = [end_list[i] for i in theft_idx]

    plt.scatter(theft_idx, theft_src, s=200, facecolors='none',
                edgecolors='red', linewidths=2.5)
    plt.scatter(theft_idx, theft_end, s=200, facecolors='none',
                edgecolors='red', linewidths=2.5, label='Theft Detected')

    plt.title(" Real-Time Water Flow Simulation with Theft Detection", fontsize=14)
    plt.xlabel("Time Step")
    plt.ylabel("Flow (L/min)")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.show()
    time.sleep(delay)
