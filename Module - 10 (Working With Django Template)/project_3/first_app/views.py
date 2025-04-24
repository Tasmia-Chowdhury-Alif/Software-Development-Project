from django.shortcuts import render
import datetime

d = {"name" : "Rohim", "age" : 22, "courses" : 
     [
        {
            "id" : 1,
            "name" : "python",
            "fee" : 20000,
        },
        {
            "id" : 2,
            "name" : "Django",
            "fee" : 50000,
        },
        {
            "id" : 3,
            "name" : "Machine Learning",
            "fee" : 70000,
        },
     ], "lst" : ['python', 'is', 'fun'], 'birthday' : datetime.datetime.now(), "unsafe_html" : "<p>This <em>should be</em> fun!</p>" ,
     }

def home(request):
    return render(request, 'first_app/home.html', context= d )