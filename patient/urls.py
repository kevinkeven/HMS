from django.urls import path
from . import views

app_name = 'patient'
urlpatterns = [
    path('', views.PatientListView.as_view(), name='all_patient'),
    path('info/<uuid:pk>/<slug:slug>', views.PatientDetailView.as_view(), name='patient_info'),
    path('new/', views.PatientCreateView.as_view(), name='new_patient'),
    path('new/<uuid:pk>/condition/', views.ConditionCreateView.as_view(), name='patient_condition'),
    path('update/<uuid:pk>/<slug:slug>', views.PatientUpdateView.as_view(), name='patient_update'),
]