from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:question_id>', views.detailView, name='detail'),
    path('list', views.viewList, name='view_list'),
    path('<int:question_id>', views.vote, name='vote'),
    path('', views.index,name='index')
]