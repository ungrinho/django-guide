from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect   # 다른 주소로 넘기기


# 127.0.0.1:8000 뒤에 어떻게 이루어지는지

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),
    path('', view=lambda request: redirect("/myapp/"))
]

