from pathlib import Path
from account.models import User

class FormValidMixin():
	def form_valid(self, form):
		self.obj = form.save(commit=False)
		self.obj.owner = self.request.user
		self.obj.format = Path(str(form.cleaned_data['file'])).suffix

		user = User.objects.get(username=self.request.user.username)
		user.user_uploaded_volume += int(form.cleaned_data['size'])
		user.save()

		return super().form_valid(form)