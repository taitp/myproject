from django.http import HttpResponse
from django.shortcuts import render, get_list_or_404
from .models import Question

def index(request):
    # return HttpResponse("Hello mấy cưng")
    myname = "Trần Phúc Tài"
    taisan1 = {"Điện thoại", "Máy tính", "Máy bay"}
    context = {"name": myname, "taisan": taisan1}
    return render(request,"polls/index.html", context)

def viewList(request):
    # list_question = get_list_or_404(Question, pk=0)
    list_question = Question.objects.all()
    context = {"dsquest": list_question}
    return render(request,"polls/question_list.html", context)

def detailView(request,question_id):
    q = Question.objects.get(pk=question_id)
    return render(request,"polls/detail_question.html", { "qs": q})
