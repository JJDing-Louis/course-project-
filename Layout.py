#!evn01/Scripts/python3.8
""" docString"""
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import tkinter as tk
from firebasepackage.database import Database as db
from gpiozero import Button
from sensorpackage.Melexis import Melexis as m #0309修改過

'''全域變數'''
#變數局域問題待修改


def closeWindow():  # 關閉視窗的MessgaeBox function
    ans = messagebox.askyesno('關閉視窗', '是否離開?')
    if ans == True:
        window.destroy()
    else:
        return


def interface(w):  # 建立視窗畫面
    """ 建立介面 """
    w.option_add("*font", ('verdana', 16))
    w.title("體溫量測")  # 視窗標題
    w.geometry("620x465")  # 視窗大小

    '''輸入姓名、ID'''
    strId = StringVar()  # 宣告字串變數
    id = strId.get()  # 取的字串視窗內容
    strName = StringVar()  # 宣告字串變數
    name = strName.get()  # 取的字串視窗內容
    Label(w, text='ID:').place(x=10, y=10)  # ID標籤
    Label(w, text='姓名:').place(x=10, y=55)  # 姓名標籤
    Entry(w, textvariable=strId, width=8).place(x=65, y=10)  # 建立字串視窗
    Entry(w, textvariable=strName, width=8).place(x=65, y=55)  # 建立字串視窗

    '''量測溫度、判定狀態'''
    txtTemp = tk.StringVar()
    txtState = tk.StringVar()
    txtTemp.set('體溫:', )
    txtState.set('狀態:', )
    tk.Label(w, textvariable=txtTemp).place(x=180, y=10)  # 體溫標籤
    tk.Label(w, textvariable=txtState).place(x=180, y=55)  # 狀態標籤

    '''建立數值輸入(測量)(3/9是做測試)'''
    temp=m.btnPress()
    if temp >= 37.5:
        state = '發燒'
        txtTemp.set('體溫:', temp)
        txtState.set('狀態:', state)
    else:
        state = '正常'
        txtTemp.set('體溫:', temp)
        txtState.set('狀態:', state)
    '''sensor = Melexis()
    button = Button(18)  # 按鈕的角位
    if button.is_pressed: #此步驟設定按鈕偵聽量測
        temp = sensor.readObject1()
        a = sensor.readAmbient()
        '''




    Button(w, text='新增', command=db.insert(name,temp,state)).place(x=420, y=15)  # 新增按鈕
    Button(w, text='刪除', command=db.delete(id)).place(x=420, y=65)  # 刪除按鈕
    Button(w, text='查詢', command=db.search(id)).place(x=520, y=15)  # 查詢按鈕
    Button(w, text='修改', command=db.update(id, name, temp, state)).place(x=520, y=65)  # 修改按鈕
    w.wm_resizable(height=False, width=False)  # 固定視窗大小



    '''建立List'''
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
    tree.place(x=10, y=10, width=580, height=320)
    labFrame.place(x=10, y=95, width=600, height=360)
    '''建立List內容(試做)'''
    tree.insert("",0,text="line1" ,values=("134135","Jack","fever","37.5"))

    '''視窗滾輪'''
    yscrollbar = Scrollbar(tree)  # y軸scroller物件
    yscrollbar.pack(side=RIGHT, fill=Y)  # y軸scroller包裝顯示
    yscrollbar.config(command=tree.yview)  # y軸scroller


if __name__ == "__main__":
    window = Tk()
    interface(w=window)
    db.searchAll() #執行階段就搜尋
    window.protocol('WM_DELETE_WINDOW', closeWindow)  # 關閉視窗的MessgaeBox
    window.mainloop()
