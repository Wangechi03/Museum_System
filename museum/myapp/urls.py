from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # General Pages
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('explore/', views.explore, name='explore'),

    # User Authentication
    path('admin_login/', views.admin_login, name='admin_login'),
    path('user_login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('success/', views.success_view, name='success'), 

    # Visitor Management
    path('visitorpage/', views.visitorpage, name='visitorpage'),
    path('visitor_reg/', views.visitor_reg, name='visitor_reg'),
    path('visitor_dashboard/', views.visitor_dashboard, name='visitor_dashboard'),
    path('accounts/profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),

    # Booking and Feedback
    path('feedback/', views.feedback, name='feedback'),
    path('feedback/thank-you/', views.feedback_thank_you, name='feedback_thank_you'),
    path('admin_feedback/', views.admin_feedback, name='admin_feedback'),
    path('stkpush/', views.stkpush, name='stkpush'),  # Added trailing slash for consistency
    # Artifact and Artist Management
    path('artifacts/', views.artifacts, name='artifacts'),
    path('artist_artifact/', views.artist_artifact, name='artist_artifact'),
    path('department_artifact/', views.department_artifact, name='department_artifact'),

    # Administration
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('view_booking/', views.view_booking, name='view_booking'),
     path('edit-booking/<int:booking_id>/', views.edit_booking, name='edit_booking'),
    path('delete_booking/', views.delete_booking, name='delete_booking'),
    path('visitor_details/', views.visitor_details, name='visitor_details'),
    path('artist_reg/', views.artist_reg, name='artist_reg'),
    path('artifact_reg/', views.artifact_reg, name='artifact_reg'),
    path('emp_reg/', views.emp_reg, name='emp_reg'),
    path('department_reg/', views.department_reg, name='department_reg'),
]
