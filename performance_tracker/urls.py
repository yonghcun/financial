from django.contrib import admin
from django.urls import path, include
import tracker.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tracker.urls')),  # 👈 tracker 앱의 urls.py를 연결
    path('export/', views.export_excel, name='export'),
]
