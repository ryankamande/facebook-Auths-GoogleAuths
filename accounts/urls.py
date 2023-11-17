from django.urls import path

from accounts.views import CreateAccount, AllUsers, CurrentUser

urlpatterns = [
    path('create/', CreateAccount.as_view(), name="create_user"),
    path('allusers/', AllUsers.as_view(), name="allusers"),
    path('currentuser/', CurrentUser.as_view(), name="current_user")
]