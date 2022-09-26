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
    def __init__(self, accmethod, settmethod, username):
        self.accstream = UserInfo.child("users").child(username).child("Accounts").stream(accmethod)
        self.settstream = UserInfo.child("users").child(username).child("PasswordSettings").stream(settmethod)
    def close_streams(self):
        self.accstream.close()
        self.settstream.close()

def DB_Login(email, password):
    user = auth.sign_in_with_email_and_password(email, password)
    return user

def get_id_and_username(token):
    userinf = auth.get_account_info(token)
    userid = userinf['users'][0]['localId']
    username = UserInfo.child("users").get()
    for user in username.each():
                try:
                    if user.val()['userinfo']['UID'] == userid:
                        username = user.key()
                except (KeyError):
                    pass
    return userid, username

def get_accounts(username):
        accounts = UserInfo.child("users").child(username).child("Accounts").get()
        return accounts

def create_new_user(email, password):
    newuser = auth.create_user_with_email_and_password(email, password)
    return newuser

def update_user_info(data, token):
    UserInfo.child("users").update(data, token)


def add_store(data, token, username):
    UserInfo.child("users").child(username).child("Accounts").update(data, token)

def nuke_info(token, username):
    UserInfo.child("users").child(username).remove(token)
    auth.delete_user_account(token)

def save_password_settings(data, username, token):
    UserInfo.child("users").child(username).child("PasswordSettings").update(data, token)

def verify_email(token):
    auth.send_email_verification(token)

def reset_password(email):
    auth.send_password_reset_email(email)
    

def get_new_account(path, username, token):
    newaccount = UserInfo.child("users").child(username).child("Accounts").child(path).get(token)
    return newaccount