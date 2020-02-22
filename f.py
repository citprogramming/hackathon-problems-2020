import subprocess
import time

try:
    import firebase_admin

except ModuleNotFoundError:
    subprocess.call(['pip3', 'install', 'firebase_admin'])
    import firebase_admin
    
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('hackathon-submission-portal-firebase-adminsdk-j568z-6945d8da51.json')
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()

team_ref = db.collection(u'teams')

def main():
    print(team_ref.get())