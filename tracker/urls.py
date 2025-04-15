from django.urls import path
from . import views

urlpatterns = [
    path('input/', views.input_view, name='input'),
    path('update/<int:id>/', views.update_view, name='update'),
    path('view/', views.view_view, name='view'),
    path('export/', views.export_excel, name='export'),
    path('stats/', views.stats_view, name='stats'),
    path('summary/', views.dynamic_summary_view, name='dynamic_summary'),
]