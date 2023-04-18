import tkinter as tk
from PIL import Image
from collections import deque
import pyfirmata
from pyfirmata import Arduino
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time
import csv
from numpy import interp 
from datetime import datetime
import pandas as pd



# from tkinter import ttk

# import matplotlib
# matplotlib.use("TkAgg")
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# from matplotlib.figure import Figure
# import matplotlib.animation as animation
# from matplotlib import style



# LARGE_FONT = ("Verdana", 12)
# style.use("ggplot")
event = 'Real_extension'

# def initiate(lable):
#     event = lable
#     startrecording()

# def startrecording():
#     print("connect me")
#     while True:
#     # key = readchar.readkey()
#     # if key == readchar.key.SPACE:
#     #     with open(storagepath, 'a', encoding= 'UTF8') as f:
#     #         row = '------------------------------------'
#     #         writer = csv.writer(f)
#     #         writer.writerow(row)
#     #         print (row)
#     # else:
#     #     continue
#         channel1 = pin1.read()
#         que1.append(channel1)
#         global x1
#         x1 = list(que1)
#         lenx = len(x1)
#         while lenx < 100:
#             x1.append(0)
#             lenx = len(x1)
    
#         channel2 = pin2.read()
#         que2.append(channel2)
#         global x2
#         x2 = list(que2)
#         lenx2 = len(x2)
#         while lenx2 < 100:
#             x2.append(0)
#             lenx2 = len(x2)

#         row = [ curr_date_time, channel1, channel2, event]
        
#         with open(storagepath, 'a', encoding= 'UTF8') as f:
#             writer = csv.writer(f)
#             writer.writerow(row)
#             print (row)

# st.heading("EMG Data Collection")
# st.text("Recording data for:")
# st.button('Flexion', on_click=initiate, args=("Flexion",))

port = "COM6"
board = Arduino(port)
pin1 = board.get_pin('a:0:i')
pin2 = board.get_pin('a:1:i')

it = pyfirmata.util.Iterator(board)
it.start()

que1 = deque(maxlen=100)
que2 = deque(maxlen=100)
xaxis= [None]*100
for z in range(100):
    xaxis[z]=z+1


# now = datetime.now()
# curr_date_time = now.strftime("%d-%b-%Y %I:%M:%S %p")

def progressbar(current_value,total_value,bar_lengh,progress_char): 
    percentage = int((current_value/total_value)*100)                                                # Percent Completed Calculation 
    progress = int((bar_lengh * current_value ) / total_value)                                       # Progress Done Calculation 
    loadbar = "Progress: [{:{len}}]{}%".format(progress*progress_char,percentage,len = bar_lengh)    # Progress Bar String
    print(loadbar, end='\r') 

storagepath = r'C:\Users\jyoth\Desktop\Code\EMG_DataCollection\data_test_1504_1.csv'
print(storagepath)
with open(storagepath, 'a', encoding= 'UTF8') as f:
    writer = csv.writer(f)
    print_out='Data logging initiated'
    print("Data logging initiated")
    heading = ['DateTime','TimeCoordinate','Channel_1','Channel_2', event]
    writer.writerow(heading)
iteration = 0

while True:
    iteration += 1
    print(f'Sample number: {iteration}')
    n= 0
    while n<20:
        # key = readchar.readkey()
        # if key == readchar.key.SPACE:
        #     with open(storagepath, 'a', encoding= 'UTF8') as f:
        #         row = '------------------------------------'
        #         writer = csv.writer(f)
        #         writer.writerow(row)
        #         print (row)
        # else:
        #     continue
        channel1 = pin1.read()
        que1.append(channel1)
        global x1
        x1 = list(que1)
        lenx = len(x1)
        while lenx < 100:
            x1.append(0)
            lenx = len(x1)
        channel2 = pin2.read()
        que2.append(channel2)
        global x2
        x2 = list(que2)
        lenx2 = len(x2)
        while lenx2 < 100:
            x2.append(0)
            lenx2 = len(x2)
        row = [n, channel1, channel2, event]
        with open(storagepath, 'a', encoding= 'UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(row)
            print (f'{row} /n', end='/r') 
            
        
        progressbar(n,20,30,'■')
        n += 1
        # time.sleep(0.2)

        plt.plot( xaxis, x1, xaxis , x2)
        plt.ylim(0.0,1.0)
        plt.draw()
        plt.pause(0.2)
        plt.clf()
        # time.sleep(0.005)
    row = ['-','-','-','-']
    with open(storagepath, 'a', encoding= 'UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(row)
        print (row)

# data1 = {'country': ['A', 'B', 'C', 'D', 'E'],
#          'gdp_per_capita': [45000, 42000, 52000, 49000, 47000]
#          }
# df1 = pd.DataFrame(data1)

# data2 = {'year': [1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010],
#          'unemployment_rate': [9.8, 12, 8, 7.2, 6.9, 7, 6.5, 6.2, 5.5, 6.3]
#          }  
# df2 = pd.DataFrame(data2)

# data3 = {'interest_rate': [5, 5.5, 6, 5.5, 5.25, 6.5, 7, 8, 7.5, 8.5],
#          'index_price': [1500, 1520, 1525, 1523, 1515, 1540, 1545, 1560, 1555, 1565]
#          }
# df3 = pd.DataFrame(data3)



# figure1 = plt.Figure(figsize=(6, 5), dpi=100)
# ax1 = figure1.add_subplot(111)
# bar1 = FigureCanvasTkAgg(figure1, root)
# bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
# df1 = df1[['country', 'gdp_per_capita']].groupby('country').sum()
# df1.plot(kind='bar', legend=True, ax=ax1)
# ax1.set_title('Country Vs. GDP Per Capita')

# figure2 = plt.Figure(figsize=(5, 4), dpi=100)
# ax2 = figure2.add_subplot(111)
# line2 = FigureCanvasTkAgg(figure2, root)
# line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
# df2 = df2[['year', 'unemployment_rate']].groupby('year').sum()
# df2.plot(kind='line', legend=True, ax=ax2, color='r', marker='o', fontsize=10)
# ax2.set_title('Year Vs. Unemployment Rate')

# figure3 = plt.Figure(figsize=(5, 4), dpi=100)
# ax3 = figure3.add_subplot(111)
# ax3.scatter(df3['interest_rate'], df3['index_price'], color='g')
# scatter3 = FigureCanvasTkAgg(figure3, root)
# scatter3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
# ax3.legend(['index_price'])
# ax3.set_xlabel('Interest Rate')
# ax3.set_title('Interest Rate Vs. Index Price')

# root.mainloop()




# from tkinter import ttk

# import matplotlib
# matplotlib.use("TkAgg")
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# from matplotlib.figure import Figure
# import matplotlib.animation as animation
# from matplotlib import style



# LARGE_FONT = ("Verdana", 12)
# style.use("ggplot")


  

    # time.sleep(0.1)
