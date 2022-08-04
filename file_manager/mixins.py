from pathlib import Path

from account.models import User
from django.http import HttpResponseRedirect


class FormValidMixin():
    def form_valid(self, form):
        user = User.objects.get(username=self.request.user.username)
        if user.user_uploaded_volume <= 2e+9:  # 2e+9 == 2000000000
            self.obj = form.save(commit=False)
            self.obj.owner = self.request.user
            self.obj.format = Path(str(form.cleaned_data['file'])).suffix

            user.user_uploaded_volume += int(form.cleaned_data['size'])
            user.save()
        else:
            return HttpResponseRedirect('/')

        return super().form_valid(form)
