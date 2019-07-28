from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.PostList.as_view()), # as_view형식으로 전달
    #path('<int:pk>/',views.post_detail)
    path('<int:pk>/',views.PostDetail.as_view()),
]
