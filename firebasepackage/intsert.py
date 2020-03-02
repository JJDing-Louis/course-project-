#!/usr/bin/python3
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class Insert:

    cred = credentials.Certificate("stust-game-firebase-adminsdk-z8f9e-565f1cf637.json")
    firebase_admin.initialize_app(cred)


    def new(self):
        '''建立電腦ID自動產生碼'''
        db = firestore.client()
        doc_ref = db.collection('Q1', 'DOC1', 'Q2').document('DOC2')
        data = {
            'id':'xxxx',
            '姓名': '劉德華',
            '體溫': '36.5',
            '狀態': '正常',
        }
        doc_ref.set(data)
        print('Done')