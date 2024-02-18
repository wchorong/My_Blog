from django import forms
from ckeditor.widgets import CKEditorWidget

from main.models import Sub_blog

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Sub_blog
        fields = ('content',)