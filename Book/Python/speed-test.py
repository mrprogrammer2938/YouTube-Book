# pip install tk-tools
# pip install speedtest-cli

from tkinter import *
from speedtest import Speedtest

class myapp(object):
    def __init__(self):
        super().__init__()

        self.root = Tk()

        self.root.title('Speed Test')
        self.photo = PhotoImage(file = 'speedtest-logo.png')

        self.scan = Button(self.root,text='Scan',width=9,height=3,command=self.scan_internet)
        self.scan.pack()
        self.scan.place(bordermode=OUTSIDE,x=115,y=80)
        self.exit = Button(self.root,text='Exit',width=9,height=3,command=self.ext)
        self.exit.pack()
        self.exit.place(bordermode=OUTSIDE,x=115,y=140)


        self.root.iconphoto(False,self.photo)
        self.root.resizable(0,0)
        self.root.geometry("300x300")
        self.root.configure(background='cyan')
        self.root.mainloop()
    

    def scan_internet(self):
        ch = Speedtest()
        global down
        global up
        down = Label(self.root,text=f"Download: {ch.download()}",bg='cyan')
        down.pack()
        down.place(bordermode=OUTSIDE,x=60,y=10)
        up = Label(self.root,text=f"Upload: {ch.upload()}",bg='cyan')
        up.pack()
        up.place(bordermode=OUTSIDE,x=60,y=38)

        self.scan.configure(text='Try',command=self.clear_label)



    def ext(self):
        self.root.destroy()
        exit()


    def clear_label(self):
        down.destroy()
        up.destroy()
        self.scan_internet()



if __name__ == '__main__':
    window = myapp()
