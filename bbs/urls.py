from django.urls import path
from . import views

app_name = 'bbs'

urlpatterns = [
    #path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('strategy/', views.strategy, name='strategy'),
    path('strategy/<int:_id>/', views.strategy_detail, name='strategy_detail'),
    path('strategy/new/', views.strategy_new, name='strategy_new'),
]