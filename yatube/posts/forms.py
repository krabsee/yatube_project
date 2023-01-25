from django import forms
from .models import Post, Group


class PostForm(forms.ModelForm):
    """Creates a new form."""

    # Get a list of groups from the database.
    group = forms.ModelChoiceField(queryset=Group.objects.all(),
                                   required=False,
                                   )

    class Meta:
        model = Post
        fields = ('text', 'group')

    def clean_text(self):
        data = self.cleaned_data['text']
        if data == '':
            raise forms.ValidationError('Заполните поле')
        return data
