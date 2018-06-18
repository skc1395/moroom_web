from django.conf import settings
from accounts.models import Profile
from allauth.account.adapter import DefaultAccountAdapter

class MyAccountAdapter(DefaultAccountAdapter):

    def get_login_redirect_url(self, request):
        profile = Profile.objects.get(user=request.user.id)

        path = '/accounts/profile'

        if profile.is_updated:
            path = '/'

        return path


