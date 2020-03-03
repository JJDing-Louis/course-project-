#!/usr/bin/python3
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("D:\course-project-\jjnetnewapp-firebase-adminsdk-jc4tw-0abdc5dbd0.json")
project_id = "file"
firebase_admin.initialize_app(cred)
db = firestore.client()
import random as rd


class Database:

    def insert(self, name, temp, state):
        '''建立電腦ID自動產生碼'''
        lst = []
        id = rd.randint(1, 1000000)
        while True:
            if id not in lst:
                lst.append(id)
                break
            else:
                continue

        ''''''

        doc_ref = db.collection('file').document(str(id))  # id須轉型成字串
        data = {
            'id': id,
            '姓名': name,
            '體溫': temp,
            '狀態': state,
        }
        doc_ref.set(data)
        print('Done')

    def update(self, id, name, temp, state):
        db = firestore.client()
        doc_ref = db.collection('file').document(id)
        data = {
            '姓名': name,
            '體溫': temp,
            '狀態': state,
        }
        doc_ref.update(data)
        print('Done')

    def searchAll(self):  # 此步驟會輸出所有資料表的dic

        db = firestore.client()
        doc_ref = db.collection('file')
        docs = doc_ref.get()
        for doc in docs:
            print('姓名 => {}'.format(doc.to_dict()['姓名']))
            print('體溫 => {}'.format(doc.to_dict()['體溫']))
            print('狀態 => {}'.format(doc.to_dict()['狀態']))
            print('////////////////////////////////////////')
        print('Done')

    def search(self,id):     # 此步驟會輸出單一資料
        db = firestore.client()
        doc_ref = db.collection('file').document(id)
        doc = doc_ref.get()
        print('姓名 => {}'.format(doc.to_dict()['姓名']))
        print('體溫 => {}'.format(doc.to_dict()['體溫']))
        print('狀態 => {}'.format(doc.to_dict()['狀態']))
        print('////////////////////////////////////////')
        print('Done')

        """
        $ python Firebase-Read.py
        DOC2 => {'年紀': '23', '工作': '魔法師', '姓名': '劉德華'}
        姓名 => 劉德華
        年紀 => 23
        工作 => 魔法師
        Done
        """

    def delete(self, id):
        db = firestore.client()

        # Delete Document
        doc_ref = db.collection('file').document(id)
        doc_ref.delete()

        print('Done')
