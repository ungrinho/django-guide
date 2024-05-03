from django.urls import path
from . import views

# urlpatterns : 어떤 주소로 요청이 들어오면, 요청에 대한 뷰를 매핑하는 속성명
# 127.0.0.1:8000()
urlpatterns = [
    path('', views.index)
]