from django.urls import path
from user_activity.views import email_subscribe, news_letter, faq_view, about_us_view, terms_conditions

urlpatterns = [
    path('email-subscribe/', email_subscribe, name='email_subscribe'),
    path('news_letter/', news_letter, name='news_letter'),
    path('faq-view/', faq_view, name='faq_view'),
    path('about-us-view/', about_us_view, name='about_us'),
    path('terms-conditions/', terms_conditions, name='terms_conditions'),
]
