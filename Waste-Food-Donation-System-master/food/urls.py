from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from food import views

urlpatterns=[
    path('', views.home_view, name='home_view'),

    path('ngoclick', views.ngoclick_view, name='ngoclick'),
    path('donarclick', views.donarclick_view, name='donarclick'),

    path('ngosignup', views.ngo_signup_view, name='ngosignup'),
    path('donarsignup', views.donar_signup_view, name='donarsignup'),
    path('ngologin', LoginView.as_view(template_name='ngologin.html')),
    path('donarlogin', LoginView.as_view(template_name='donarlogin.html')),
    path('fertilogin', LoginView.as_view(template_name='fertilogin.html')),

    path('afterlogin', views.afterlogin_view, name='afterlogin'),
    path('logout', LogoutView.as_view(template_name='index1.html'), name='logout'),

    path('ngo-dashboard', views.ngo_dashboard_view, name='ngo-dashboard'),
    path('ngo-donation', views.ngo_donation_view, name='ngo-donation'),
    path('ngo-notice', views.ngo_notice_view, name='ngo-notice'),
    path('claim-donation/<int:pk1>/<int:pk2>/<str:pk3>', views.claim_donation_view, name='claim-donation'),

    path('donar-dashboard', views.donar_dashboard_view, name='donar-dashboard'),
    path('donar-donation', views.donar_donation_view, name='donar-donation'),
    path('claimed-donation', views.claimed_donation_view, name='claimed-donation'),
    path('donar-donation-history', views.donar_donation_history_view, name='donar-donation-history'),

    path('aboutus', views.aboutus_view, name='aboutus'),
    path('contactus', views.contactus_view, name='contactus'),

    path('donar_donation_view',views.donar_donation_view,name="donar_donation_view"),
    path('ferti_signup_view',views.ferti_signup_view,name="ferti_signup_view"),
    path('ferti_dashboard_view',views.ferti_dashboard_view,name="ferti_dashboard_view"),
    path('ferti_food_view',views.ferti_food_view,name="ferti_food_view"),
    path('claim_donation_view_ferti/<int:pk1>/<int:pk2>/<str:pk3>',views.claim_donation_view_ferti,name="claim_donation_view_ferti"),
]