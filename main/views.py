from django.http import HttpResponse

def hello_view(request):
    # Замените 'Имя' на ваше имя
    return HttpResponse("<h1>Hello, Alex!</h1>")
