#!/usr/bin/python3
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class Search:

    cred = credentials.Certificate("stust-game-firebase-adminsdk-z8f9e-565f1cf637.json")
    firebase_admin.initialize_app(cred)

    def search(self):

        db = firestore.client()
        #Get Collection
        doc_ref = db.collection('Q1', 'DOC1', 'Q2')
        docs = doc_ref.get()
        for doc in docs:
            print(u'{} => {}'.format(doc.id, doc.to_dict()))

        #Get Doc
        doc_ref = db.collection('Q1', 'DOC1', 'Q2').document('DOC2')
        docs = doc_ref.get()
        print('姓名 => {}'.format(doc.to_dict()['姓名']))
        print('體溫 => {}'.format(doc.to_dict()['體溫']))
        print('狀態 => {}'.format(doc.to_dict()['狀態']))

        print('Done')

        """
        $ python Firebase-Read.py
        DOC2 => {'年紀': '23', '工作': '魔法師', '姓名': '劉德華'}
        姓名 => 劉德華
        年紀 => 23
        工作 => 魔法師
        Done
        """