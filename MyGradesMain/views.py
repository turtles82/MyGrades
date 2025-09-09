from django.http import HttpResponse

def login_page(request):
    with open('/home/averagecoder/MyGrades/MyGrades/MyGradesMain/HTML/LoginPage.html', 'r') as f:
        html = f.read()
    return HttpResponse(html)
