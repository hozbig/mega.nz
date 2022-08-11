from config.settings import EMAIL_FROM
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from .forms import NewUserForm
from .models import User
from .tokens import account_activation_token


def register_new_user(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(
                request, "Registration successful. Please confirm you email.")
            return redirect("file_manager:dashboard")
        messages.error(
            request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="registration/register.html", context={"form": form})


@login_required
def send_activation_email(request, email):
    if not request.user.email_activation:
        user = request.user
        current_site = get_current_site(request)
        mail_subject = 'Datashields email activation.'
        message = render_to_string('acc_active_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        send_mail(
            mail_subject,
            message,
            EMAIL_FROM,
            [email],
            fail_silently=False,
        )
        messages.success(request, "Activation email is just send.")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        raise Http404("Access Denide!")


@login_required
def get_activation_token(request, uidb64, token):
    if not request.user.email_activation:
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            user.email_activation = True
            user.save()
            messages.success(request, "Your email activate successfuly.")
            return redirect("file_manager:dashboard")
        else:
            return HttpResponse('Activation link is invalid!')
    else:
        raise Http404("Access Denide!")
