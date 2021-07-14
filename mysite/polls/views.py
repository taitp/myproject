from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello mấy cưng")

def ham1(request):
    return HttpResponse("<h1>Hàm linh tinh</h1><p>Xin chào</p>")
