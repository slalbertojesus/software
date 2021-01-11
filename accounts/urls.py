from django.urls import path, include 


from .views import (
        #Auth
        display_login,
)

app_name = 'accounts'

urlpatterns = [
        path('login', display_login, name="login"),
]
