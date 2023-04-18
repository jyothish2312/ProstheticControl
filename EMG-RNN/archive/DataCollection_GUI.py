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
import multiprocessing

# Creating GUI Window
root = tk.Tk()
root.title("EMG Data Collection")

menu= tk.Frame(root, bg="black", borderwidth=6) # Menu Bar
menu.pack(side = tk.TOP, fill="x", pady=1)
menua= tk.Frame(menu, bg="grey", )
menua.pack(side = tk.TOP, fill="x", pady=1, expand=tk.TRUE) # Menu Sub Bar
gifwindow= tk.Frame(root, bg="lightblue", borderwidth=6) # Left Window for the GIF Animation
gifwindow.pack(side = tk.LEFT, pady=0, fill = "y", expand=tk.TRUE)
graphwindow= tk.Frame(root, bg="white", borderwidth=6 ) # Right Window for showing the plot
graphwindow.pack(side = tk.LEFT, pady=0 ,fill = tk.BOTH, expand=tk.TRUE)
textwindow= tk.Frame(graphwindow, bg="darkgrey", borderwidth=6 ) # Terminal OUtput
graphwindow.pack(side = tk.BOTTOM, pady=0 ,fill = "x", expand=tk.TRUE)



# Initiating Arduino Communictation
port = "COM6"
board = Arduino(port)
pin1 = board.get_pin('a:0:i')
pin2 = board.get_pin('a:1:i')
it = pyfirmata.util.Iterator(board)
it.start()

# Variables for data handling
que1 = deque(maxlen=100)
que2 = deque(maxlen=100)
xaxis= [None]*100
for z in range(100):
    xaxis[z]=z+1

# Log starting date and time
now = datetime.now()
curr_date_time = now.strftime("%d-%b-%Y %I:%M:%S %p")

event = '' # Event being recorded
#Initializing data logging
storagepath = r'C:\Users\jyoth\Desktop\Code\EMG_DataCollection\data_test.csv'
print(storagepath)
with open(storagepath, 'a', encoding= 'UTF8') as f:
    writer = csv.writer(f)
    print_out='Data logging initiated'
    textwindow.update()
    print("Data logging initiated")
    print(curr_date_time)
    heading = ['DateTime','TimeCoordinate','Channel_1','Channel_2', event]
    writer.writerow(heading)

flexiongif="Flextion.gif"
info = Image.open(flexiongif)
framesf = info.n_frames  # gives total number of frames that gif contains
imf = [tk.PhotoImage(file=flexiongif,format=f"gif -index {i}") for i in range(framesf)] # creating list of PhotoImage objects for each frames

extensiongif="Extension.gif"
info = Image.open(extensiongif)
framese = info.n_frames  # gives total number of frames that gif contains
ime = [tk.PhotoImage(file=extensiongif,format=f"gif -index {i}") for i in range(framese)] # creating list of PhotoImage objects for each frames

count = 0
anim = None
anima = None
row = ''

def write(row):
    with open(storagepath, 'a', encoding= 'UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(row)
        print (row)
#Setting up for multiprocessing
proc_write = multiprocessing.Process(target=write, args=(row))

def read(event):
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
    row = [ curr_date_time, channel1, channel2, event] 
    with open(storagepath, 'a', encoding= 'UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(row)
        print (row)
   # proc_write.start()
#Setting up for multiprocessing
proc_read = multiprocessing.Process(target=read, args=(event,))

def plot():
    # data= {'Serial' : xaxis, 'Values': x}
    # dt = pd.DataFrame(data)

    figure = plt.figure(figsize=(10, 8), dpi=100)
    figure.add_subplot(111).plot(xaxis,x1, xaxis, x2)
    chart= FigureCanvasTkAgg(figure, graphwindow)
    chart.get_tk_widget().grid(row = 5, column = 0)
    plt.grid()
    axes = plt.axes()
    axes.set_xlim([0,101])
    axes.set_ylim([0.0, 1.0])

    # line = FigureCanvasTkAgg(figure, root)
    # line.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    # dt = dt[['Values', 'Serial']].groupby('Values').sum()
    # dt.plot(kind='line', legend=True, ax=ax, color='r', marker='o', fontsize=10)
    # ax.set_title('Values Vs. Coordinate') 

    plt.plot( xaxis, x1, xaxis , x2)
    # plt.ylim(0.0,1.0)
    # plt.draw()
    # plt.pause(0.1)
    # plt.clf()

    # plt.plot(que2, color="blue")
    # plt.ylim(0.0,1.0)
    # plt.draw()
    # plt.pause(0.05)
    # plt.clf()
#Setting up for multiprocessing
proc_plot = multiprocessing.Process(target=plot, args=())




def animation1(count):
    count= count
    global anim
    im2 = imf[count]

    gif_label.configure(image=im2)
    count += 1
    if count == framesf:
        count = 0
        row = "---------------------------------------------------"
        with open(storagepath, 'a', encoding= 'UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(row)
            print (row)
        time.sleep(1)

    event = 'Flexion'
    read(event)
    plot()
    menu.update()
        
    anim = root.after(10,lambda :animation1(count))

def animation2(count):
    global anima
    im3 = ime[count]
    
    gif_label.configure(image=im3)
    count += 1
    if count == framese:
      
        count = 0
        row = "---------------------------------------------------"
        with open(storagepath, 'a', encoding= 'UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(row)
            print (row)
        time.sleep(1)
    event = 'Extension'
    read(event)
   
    plot()
    menu.update()
    anima = root.after(50,lambda :animation2(count))   
    




    # plt.plot(que1, color="red")
    # plt.ylim(0.0,1.0)
    # plt.draw()
    # plt.pause(0.1)
    # plt.clf()
    # plt.plot(que2, color="blue")
    # plt.ylim(0.0,1.0)
    # plt.draw()
    # plt.pause(0.05)
    # plt.clf()

def stop_animation():
    try:
        row = "========================================"
        with open(storagepath, 'a', encoding= 'UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(row)
            print (row)
        root.after_cancel(anim)
    except:
        row = "========================================"
        with open(storagepath, 'a', encoding= 'UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(row)
            print (row)
        root.after_cancel(anima)
       




gif_label = tk.Label(gifwindow,image="")
gif_label.pack()

flexion=tk.Button(menua, text="Flextion", font="Helvetica 10 bold", relief=tk.GROOVE, command=lambda :animation1(count) )
flexion.pack(side=tk.LEFT,  pady= 25, fill="y", expand=tk.TRUE)

extension=tk.Button(menua, text="Extension", font="Helvetica 10 bold", relief=tk.GROOVE, command=lambda :animation2(count) )
extension.pack(side=tk.LEFT, pady= 25, fill="y", expand=tk.TRUE)

pronation=tk.Button(menua, text="Pronation", font="Helvetica 10 bold", relief=tk.GROOVE )
pronation.pack(side=tk.LEFT, pady= 25, fill="y", expand=tk.TRUE)

supernation=tk.Button(menua, text="Supernation", font="Helvetica 10 bold", relief=tk.GROOVE )
supernation.pack(side=tk.LEFT, pady= 25, fill="y", expand=tk.TRUE)

end=tk.Button(menu, bg="darkgrey", text="End Session", font="Helvetica 15 bold", relief=tk.SUNKEN, command=stop_animation)
end.pack(side=tk.TOP, pady= 10)


# start = tk.Button(root,text="Flexion",command=lambda :animation1(count))
# start.pack(side = 'left')

# start = tk.Button(root,text="Extension",command=lambda :animation2(count))
# start.pack(side = 'left')

# stop = tk.Button(root,bg="red", borderwidth=6, relief='sunken', text="stop",command=stop_animation)
# stop.pack(side = 'bottom', fill="x")

root.mainloop()