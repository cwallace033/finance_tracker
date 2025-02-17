import os
import firebase_admin
from firebase_admin import credentials, firestore

def initialize_db():
    # Initialize Firebase
    firebase_key = os.getenv('FIREBASE_KEY')
    cred = credentials.Certificate(firebase_key)
    firebase_admin.initialize_app(cred)
    return firestore.client()