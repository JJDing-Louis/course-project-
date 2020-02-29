#!evn01/Scripts/python3.8
""" docString"""
from tkinter import *

def readText():
    print('button click')

def interface(w):
    """ 建立介面 """
    w.option_add("*font",('verdana',16))
    w.title("體溫量測") #視窗標題
    w.geometry("900x600") #視窗大小
    w.wm_resizable(height=False, width=False)

    menuFrame = Frame(w,bg='purple',width=200)

    
    lineFrame = Frame(menuFrame, borderwidth=2, relief=GROOVE, width=200, bg='purple')
    Button(lineFrame,text='讀入text',command=readText).pack(fill=BOTH,expand=TRUE)
    Button(lineFrame, text='ok2').pack(fill=BOTH,expand=TRUE,pady=5)
    Button(lineFrame, text='ok3').pack(fill=BOTH,expand=TRUE)
    lineFrame.pack(expand=YES, fill=BOTH,padx=10,pady=10)
    menuFrame.pack(side=LEFT, expand=YES,fill=BOTH)

    menuFrame.pack(side=LEFT, expand=YES,fill=BOTH)

    rightFrame = Frame(w, bg='gray',width=400)

    rightFrame.pack(side=LEFT, expand=YES, fill=BOTH)



if __name__ == "__main__":
    window = Tk()
    interface(w=window)
    window.mainloop()