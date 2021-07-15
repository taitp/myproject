from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    # return HttpResponse("Hello mấy cưng")
    myname = "Trần Phúc Tài"
    taisan1 = {"Điện thoại", "Máy tính", "Máy bay"}
    context = {"name": myname, "taisan": taisan1}
    return render(request,"polls/index.html", context)

