#!/usr/bin/python3
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class Delete:

    cred = credentials.Certificate("stust-game-firebase-adminsdk-z8f9e-565f1cf637.json")
    firebase_admin.initialize_app(cred)

    def delete(self,id):
        db = firestore.client()

        # Delete Document
        doc_ref = db.collection('Q1', 'DOC1', 'Q2').document(id)
        doc_ref.delete()

        print('Done')