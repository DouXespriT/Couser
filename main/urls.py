from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.home.as_view(), name='home'),
    path('courses/', views.courses.as_view(), name='courses'),
    path('profile/<int:user_id>/', login_required(views.profile.as_view()), name='profile'),
    path('contact_us/', login_required(views.contact.as_view()), name='contact'),
    path('login/', views.login.as_view(), name='login'),
    path('logout_request/', views.logout_request.as_view(), name='logout_request'),
    path('subscribe/', views.subscribe.as_view(), name='subscribe'),
    path('transaction/<int:course_id>/', login_required(views.transaction.as_view()), name='transaction'),
    path('profile/course_applied/<int:user_id>/', login_required(views.course_applied.as_view()), name='course_applied'),
    path('profile/my_course/<int:user_id>/', login_required(views.my_course.as_view()), name='my_course'),
    path('profile/my_transaction/<int:user_id>/', login_required(views.my_transaction.as_view()), name='my_transaction'),
    
]