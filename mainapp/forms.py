from django import forms
from .models import URL
from django.contrib.auth.forms import UserCreationForm

class URLForm(forms.ModelForm):
    class Meta:
        model = URL
        fields=['Title','URL','Date']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(URLForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(URLForm, self).save(commit=False)
        instance.user = self.user
        if commit:
            instance.save()
        return instance
# In your forms.py (inside the 'bookmarks' app)
class UserCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        # Remove help_text for specific fields
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

