from pathlib import Path
from os.path import getsize

class FormValidMixin():
	def form_valid(self, form):
		self.obj = form.save(commit=False)
		self.obj.owner = self.request.user
		self.obj.format = Path(str(form.cleaned_data['file'])).suffix
		return super().form_valid(form)