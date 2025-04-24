from django.shortcuts import render
import datetime


d = { "val_strw" : "Hello", "val_str" : "wellcome to Django's Template Filters", "num" : 10, "birthday" : datetime.datetime.now(), "html_tag" : "<p>hello <span>World</span> this is <b>Alif</button></b>", "file_size" : 12546545454, "lst" : ["apple", "mango", "orange", "pinaple"], "lst2" :  ['States', ['Kansas', ['Lawrence', 'Topeka'], 'Illinois']], "dict" : [
    {'name': 'zed', 'age': 19},
    {'name': 'amy', 'age': 22},
    {'name': 'joe', 'age': 31},
]}

# Create your views here.
def home(requerst):
    return render(requerst, 'first_app/home.html', context=d)