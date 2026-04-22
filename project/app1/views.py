from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("Hello, World!")

def add_numbers(request):
    a = int(request.GET.get('a', 0))
    b = int(request.GET.get('b', 0))
    return HttpResponse(f"Result: {a + b}")