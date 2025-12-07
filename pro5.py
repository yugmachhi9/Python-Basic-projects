# internet speed test 

from tkinter import *
import speedtest

def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str (round(sp.download()/(10**6),3))+"Mbps"
    up = str (round(sp.upload()/(10**6),3))+"Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)


sp = Tk()
sp.title("Internet speed")
sp.geometry("500x600")
sp.config(bg="red")
lab = Label(sp,text="Internet Speed Test",font=("Time new roman",20,"bold"),bg="red")
lab.place(x=60,y=90,height=50,width=380)

lab = Label(sp,text="download speed",font=("Time new roman",20,"bold"),bg="red")
lab.place(x=60,y=180,height=50,width=380)

lab_down = Label(sp,text="00",font=("Time new roman",20,"bold"),bg="red")
lab_down.place(x=60,y=270,height=50,width=380)

lab = Label(sp,text="upload speed",font=("Time new roman",20,"bold"),bg="red")
lab.place(x=60,y=360,height=50,width=380)

lab_up = Label(sp,text="00",font=("Time new roman",20,"bold"),bg="red")
lab_up.place(x=60,y=450,height=50,width=380)

button = Button(sp,text="Check Speed",font=("Time new roman",20,"bold"),bg="blue",command=speedcheck)
button.place(x=60,y=540,height=50,width=380)



sp.mainloop()