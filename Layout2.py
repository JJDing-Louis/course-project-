#!evn01/Scripts/python3.8
""" docString"""
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import tkinter as tk
from firebasepackage.database import Database as db
from gpiozero import Button
from sensorpackage.Melexis import Melexis as m #0309修改過


def closeWindow():  # 關閉視窗的MessgaeBox function
    ans = messagebox.askyesno('關閉視窗', '是否離開?')
    if ans == True:
        window.destroy()
    else:
        return


class App:
    '''全域變數'''

    # 變數局域問題待修改

    def __init__(self):
        # 定義共用屬性
        self.strId = StringVar()  # 宣告ID字串變數
        self.strName = StringVar()  # 宣告名字字串變數
        self.txtTemp = tk.StringVar()  # 宣告溫度字串變數
        self.txtState = tk.StringVar()  # 宣告狀態字串變數
        self.id = self.strId.get()  # 取得字串視窗內容
        self.name = self.strName.get()  # 取得字串視窗內容
        self.txtTemp.set('體溫:', )  # 設定字串內容
        self.txtState.set('狀態:', )  # 設定字串內容
        self.button=Button(18)



        # 建立window and Layout
        '''輸入姓名、ID'''
        Label(window, text='ID:').place(x=10, y=10)  # ID標籤
        Label(window, text='姓名:').place(x=10, y=55)  # 姓名標籤
        Entry(window, textvariable=self.strId, width=8).place(x=65, y=10)  # 建立字串視窗
        Entry(window, textvariable=self.strName, width=8).place(x=65, y=55)  # 建立字串視窗

        '''量測溫度、判定狀態'''
        tk.Label(window, textvariable=self.txtTemp).place(x=180, y=10)  # 體溫標籤
        tk.Label(window, textvariable=self.txtState).place(x=180, y=55)  # 狀態標籤

        Button(window, text='新增', command=db.insert(self.name, self.txtTemp, self.state)).place(x=420, y=15)  # 新增按鈕
        Button(window, text='刪除', command=db.delete(id)).place(x=420, y=65)  # 刪除按鈕
        Button(window, text='查詢', command=db.search(id)).place(x=520, y=15)  # 查詢按鈕
        Button(window, text='修改', command=db.update(id, self.name, self.txtTemp, self.state).place(x=520, y=65))  # 修改按鈕
        window.wm_resizable(height=False, width=False);  # 固定視窗大小

        '''建立List(需修改)''';
        labFrame = LabelFrame(window, text='量測數據');
        tree = Treeview(labFrame, columns=('ID', '姓名', '體溫', '狀態'), show='headings');
        tree.column('ID', width=40);
        tree.column('姓名', width=40);
        tree.column('體溫', width=40);
        tree.column('狀態', width=40);
        tree.heading('ID', text='ID');
        tree.heading('姓名', text='姓名');
        tree.heading('體溫', text='體溫');
        tree.heading('狀態', text='狀態');
        tree.place(x=10, y=10, width=580, height=320);
        labFrame.place(x=10, y=95, width=600, height=360);
        '''建立List內容(試做)''';
        tree.insert("", 0, text="line1", values=("134135", "Jack", "fever", "37.5"));

        '''視窗滾輪''';
        yscrollbar = Scrollbar(tree);  # y軸scroller物件
        yscrollbar.pack(side=RIGHT, fill=Y);  # y軸scroller包裝顯示
        yscrollbar.config(command=tree.yview);  # y軸scroller

        if self.button.is_pressed:
            t = m.readObject1()
            a = m.readAmbient()
            print("Object: {}C , Ambiant: {}C".format(round(t, 3), round(a, 3)))


    '''def btnMeasure(self):


        temp=m.btnPress()
        if temp >= 37.5:
            state = '發燒'
            self.txtTemp.set('體溫:', temp)
            self.txtState.set('狀態:', state)
        else:
            state = '正常'
            self.txtTemp.set('體溫:', temp)
            self.txtState.set('狀態:', state)
        sensor = Melexis()
        button = Button(18)  # 按鈕的角位
        if button.is_pressed: #此步驟設定按鈕偵聽量測
            temp = sensor.readObject1()
            a = sensor.readAmbient()
            ''' \



if __name__ == "__main__":
    window = Tk()
    """ 建立介面 """
    window.title("體溫量測")  # 視窗標題
    window.option_add("*font", ('verdana', 16))
    window.geometry("620x465")  # 視窗大小
    window.protocol('WM_DELETE_WINDOW', closeWindow)  # 關閉視窗的MessgaeBox
    window.mainloop()

