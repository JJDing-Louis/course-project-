#!evn01/Scripts/python3.8
""" docString"""
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox


def readText():
    print('button click')


def closeWindow(): #關閉視窗的MessgaeBox function
    ans=messagebox.askyesno('關閉視窗', '是否離開?')
    if ans == True:
        window.destroy()
    else:
        return

def interface(w):
    """ 建立介面 """
    w.option_add("*font", ('verdana', 16))
    w.title("體溫量測")  # 視窗標題
    w.geometry("520x420")  # 視窗大小

    name = Label(w, text='姓名:').place(x=10, y=10)
    temp = Label(w, text='體溫:').place(x=160, y=10)
    upload = Button(w, text='上傳').place(x=420, y=15)
    w.wm_resizable(height=False, width=False)

    '''建立區域擺放清單'''
    labFrame = LabelFrame(w, text='量測數據')
    tree = Treeview(labFrame, columns=('ID', '姓名', '體溫', '狀態'), show='headings')
    tree.column('ID', width=40)
    tree.column('姓名', width=40)
    tree.column('體溫', width=40)
    tree.column('狀態', width=40)
    tree.heading('ID', text='ID')
    tree.heading('姓名', text='姓名')
    tree.heading('體溫', text='體溫')
    tree.heading('狀態', text='狀態')
    tree.place(x=10, y=10, width=480, height=320)
    labFrame.place(x=10, y=50, width=500, height=360)

    yscrollbar = Scrollbar(tree)  # y軸scroller物件
    yscrollbar.pack(side=RIGHT, fill=Y)  # y軸scroller包裝顯示
    yscrollbar.config(command=tree.yview)  # y軸scroller




if __name__ == "__main__":
    window = Tk()
    window.protocol('WM_DELETE_WINDOW', closeWindow) #關閉視窗的MessgaeBox
    interface(w=window)
    window.mainloop()
