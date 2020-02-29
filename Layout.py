#!evn01/Scripts/python3.8
""" docString"""
from tkinter import *
from tkinter import ttk

def readText():
    print('button click')

def interface(w):
    """ 建立介面 """
    w.option_add("*font",('verdana',16))
    w.title("體溫量測") #視窗標題
    w.geometry("900x600") #視窗大小
    w.wm_resizable(height=False, width=False)

    Label( text='姓名').pack()
    Label( text='體溫').pack()
    Label(text='量測數據').pack()
    Button(text='上傳').pack()

    '''建立區域擺放清單(待處理)'''
    listView = Frame(window,borderwidth=100, relief=GROOVE)
    tree = ttk.Treeview(listView, columns=('col1', 'col2', 'col3'))
    tree.column('col1', width=100, anchor='center')
    tree.column('col2', width=100, anchor='center')
    tree.column('col3', width=100, anchor='center')
    tree.heading('col1', text='col1')
    tree.heading('col2', text='col2')
    tree.heading('col3', text='col3')

if __name__ == "__main__":
    window = Tk()
    interface(w=window)
    window.mainloop()