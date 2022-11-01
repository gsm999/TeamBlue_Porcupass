from asyncio.windows_events import NULL
from pydoc import plain
import time
import pyrebase
import json

firebaseConfig = {
  'apiKey': "AIzaSyA1NFf0XKFE3ItD3M5LYMGv3FKbm2mQwSs",
  'authDomain': "porcupass-1d1cb.firebaseapp.com",
  'projectId': "porcupass-1d1cb",
  'storageBucket': "porcupass-1d1cb.appspot.com",
  'messagingSenderId': "798965436291",
  'appId': "1:798965436291:web:9b33dedac329461f3670b6",
  'measurementId': "G-SBBX0HG3XR",
  'databaseURL': "https://porcupass-1d1cb-default-rtdb.firebaseio.com"
}


firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()
UserInfo = firebase.database()
class startStream():
    def __init__(self, accmethod, settmethod, uid, token):
        self.accstream = UserInfo.child("users").child(uid).child("Accounts").stream(accmethod, token)
        self.settstream = UserInfo.child("users").child(uid).child("PasswordSettings").stream(settmethod, token)
    def close_streams(self):
        self.accstream.close()
        self.settstream.close()

def DB_Login(email, password):
    user = auth.sign_in_with_email_and_password(email, password)
    return user

def get_id_and_verify(token):
    userinf = auth.get_account_info(token)
    userid = userinf['users'][0]['localId']
    emailverified = userinf['users'][0]['emailVerified']
    return userid, emailverified

def get_accounts(uid, token):
        accounts = UserInfo.child("users").child(uid).child("Accounts").get(token)
        return accounts

def create_new_user(email, password):
    newuser = auth.create_user_with_email_and_password(email, password)
    return newuser

def update_user_info(data, token):
    UserInfo.child("users").update(data, token)


def add_store(data, token, uid):
    UserInfo.child("users").child(uid).child("Accounts").update(data, token)

def nuke_info(token, uid):
    UserInfo.child("users").child(uid).remove(token)
    auth.delete_user_account(token)

def save_password_settings(data, uid, token):
    UserInfo.child("users").child(uid).child("PasswordSettings").update(data, token)

def verify_email(token):
    auth.send_email_verification(token)

def reset_password(email):
    auth.send_password_reset_email(email)
    

def get_new_account(path, uid, token):
    newaccount = UserInfo.child("users").child(uid).child("Accounts").child(path).get(token)
    return newaccount

def get_plaintext(uid, token):
    plaintext = UserInfo.child("users").child(uid).child("Plaintext").get(token)
    if plaintext.val() is None:
        plaintext = get_plaintext(uid,token)
    return plaintext

def decrypt_password(uid, account, token):
    UserInfo.child("users").child(uid).child("Accounts").child(account).child("isEncrypted").set(False, token)
    plaintext = get_plaintext(uid, token)
    return plaintext.val()

def decrypt_cleanup(uid, account, token):
    UserInfo.child("users").child(uid).child("Plaintext").remove(token)
    UserInfo.child("users").child(uid).child("Accounts").child(account).child("isEncrypted").set(True, token)

def update_password(uid, account, token, newpassword, now):
    data = {"Created_On" : now, "Password": newpassword, "isEncrypted" : False}
    UserInfo.child("users").child(uid).child("Accounts").child(account).update(data, token)

def delete_store(uid, account, token):
    UserInfo.child("users").child(uid).child("Accounts").child(account).remove(token)