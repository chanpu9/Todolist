from django.urls import path
from .views import *                    # * ดึงมาทุกฟังก์ชันใน views.py

urlpatterns = [
    path('', Home),
    path('api/view-todolist/', view_todolist),
    path('api/create-todolist/', create_todolist),
    path('api/update-todolist/<int:TID>', update_todolist),
    path('api/delete-todolist/<int:TID>', delete_todolist)
]
