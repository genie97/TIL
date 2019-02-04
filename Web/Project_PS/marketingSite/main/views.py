from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, TemplateView
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator

def index(request):
    # The content of context is rendered in the templates
    # using {{ }} delimiters

    return render(request, 'login.html')

class UserCreateView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('common:register_done') # 네임스페이스 정확하게

class UserCreateDoneTemplateView(TemplateView):
    template_name = 'registration/register_done.html'

class UserActivateView(TemplateView):
    logger = logging.getLogger(__name__)
    template_name = 'registration/user_activate_complete.html'

    def get(self, request, *args, **kwargs):
        self.logger.debug('UserActivateView.get()')

        uid = force_text(urlsafe_base64_decode(self.kwargs['uidb64']))
        token = self.kwargs['token']

        self.logger.debug('uid: %s, token: %s' % (uid, token))

        try:
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            self.logger.warning('User %s not found' % uid)
            user = None

        if user is not None and PasswordResetTokenGenerator().check_token(user, token):
            user.is_active = True
            user.save()
            self.logger.info('User %s(pk=%s) has been activated.' % (user, user.pk))

        return super(UserActivateView, self).get(request, *args, **kwargs)