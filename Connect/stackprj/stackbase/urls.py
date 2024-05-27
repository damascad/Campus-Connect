from django.urls import path ,include
from stackbase import views
# from poll import views as poll_views

app_name="stackbase"

urlpatterns = [
    path("",views.home,name="home"),
    path("home/",views.home,name="home"),
    path("base/",views.base,name="about"),
    path("questions/",views.QuestionListView.as_view(), name="question-list"),
# ye mujhe upar wala view as view krke isliye bhejna pada kyunki ye class hai?
    path("questions/<int:pk>/",views.QuestionDetailView.as_view(),name="question-detail"),
    path("questions/new",views.QuestionCreateView.as_view(),name="question-create"),
    path("questions/<int:pk>/update",views.QuestionUpdateView.as_view(),name="question-update"),  # ye path create view wali hi automatically template use krlega ye inbuilt views hain django ke aise hi kaam krte hain , defualt mein
    path("questions/<int:pk>/delete",views.QuestionDeleteView.as_view(),name="question-delete"), 
    path("questions/<int:pk>/comment",views.AddComment.as_view(),name="question-comment"), 



    # additonal pools and goodies
    # path("polls/",views.polls,name="polls"),

    path("goodies/",views.goodies,name="goodies"),
    path("like/<int:pk>", views.like_view, name="like_post"),

    
    # poll section
    # # path('', poll_views.home, name='home'),
    path('poll/list/', views.list, name='poll_list'),
    # path('poll/create/', views.create, name='poll_create'),
    path('vote/<poll_id>/', views.vote, name='poll_vote'),
    path('results/<poll_id>/',views.results, name='poll_results'),
 
    
]


# question_confirm_delete.html apne aap ye iss html page pe search krne lg gya toh isse hi file bana de rha jab yhi search kr rha hai bo toh