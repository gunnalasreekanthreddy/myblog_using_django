from django.urls import path
from myblog import views


urlpatterns = [

    path('he/',views.hello),
    path('he2/',views.hello2),
    path('he3/',views.hello3),
    path('he4/',views.hello4),
    path('he5/',views.hello5),
]
