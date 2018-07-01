from django.shortcuts import redirect, render
from django.views import View


class LoginView(View):
    """Login management view to handle login."""

    def get(self, request):
        """Login template view to user."""
        return render(request, 'account/login.html')


class JoinView(View):
    """Join to our web-service."""

    def get(self, request):
        """Join template view to user."""
        return render(request, 'account/join.html')


def logout(request):
    """Logout user and redirect to login page."""
    # TO-DO: logout user
    return redirect('/account/login/')
