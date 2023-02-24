from django.http import HttpResponse
from django.shortcuts import render
items = {
       'list': [
           {'id': 1, 'name': 'Smartphone', 'barcode': '372548362548', 'price': 23000},
           {'id': 2, 'name': 'Laptop', 'barcode': '882548362548', 'price': 60000},
           {'id': 3, 'name': 'Keyboard', 'barcode': '672548362548', 'price': 3000},
           {'id': 4, 'name': 'Mouse', 'barcode': '452548362548', 'price': 2500}
       ]
       }
def homePage(request):
    return render(request,'index.html',items)

def aboutMe(request):
    return HttpResponse("<b>About Me</b>")
def course(request):
    return HttpResponse("I am following a django course")
def courseDetails(request,courseId):
    return HttpResponse(courseId)
