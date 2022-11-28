import pyrebase
from django.contrib import messages
from django.core.files.storage import default_storage
from fiction_fans.models import FictionTitle


firebase_config = {
  "apiKey": "AIzaSyDkgqDdQOOy2lMa_4EHpF3CSO04dM20MMQ",
  "authDomain": "fiction-fans.firebaseapp.com",
  "projectId": "fiction-fans",
  "storageBucket": "fiction-fans.appspot.com",
  "messagingSenderId": "1037444476423",
  "appId": "1:1037444476423:web:a9dec3b3c2ea21272f84a2",
  "measurementId": "G-1ZWVGGLKSD",
  "databaseURL": ""
}

firebase = pyrebase.initialize_app(firebase_config)
storage = firebase.storage()

def upload(request):
    file = request.FILES['image']
    file_save = default_storage.save(file.name, file)
    storage.child("images/" + file.name).put("images/"+file.name)
    print("upload success")
    url = storage.child("images/"+file.name).get_url(token=None)
    return url