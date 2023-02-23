from django.http import HttpResponse
from django.shortcuts import render
data = {
    'title' : 'HomePage',\
    'name' : 'kuch bhi'
}
def homePage(request):
    return render(request,'index.html',data)

def aboutMe(request):
    return HttpResponse("<b>About Me</b>")
def course(request):
    return HttpResponse("I am following a django course")
def courseDetails(request,courseId):
    return HttpResponse(courseId)
