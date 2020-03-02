#!/usr/bin/python3
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class Update:

    cred = credentials.Certificate("stust-game-firebase-adminsdk-z8f9e-565f1cf637.json")
    firebase_admin.initialize_app(cred)

    def update(self,id):
        db = firestore.client()
        doc_ref = db.collection('Q1', 'DOC1', 'Q2').document(id)
        data = {
            '體溫': '36.5',
        }
        doc_ref.update(data)
        print('Done')