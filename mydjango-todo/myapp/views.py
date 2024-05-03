from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Todo



# def index(request) : 

#     todo_qs = Todo.objects.all()

#     return render(
#         request=request,
#         template_name="myapp/index.html",
#         context={
#             "todo_qs":todo_qs
#         },
#     )
def index(request):
    return render(request, "myapp/index.html")