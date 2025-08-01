from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Div, Field
from django import forms

from accounts.models import UserProfile


class UserBaseForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'password', 'email', 'profile_image']
        help_texts = {}


class UserCreateForm(UserBaseForm):
    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('username', css_class='form-group col-md-6'),
                Column('email', css_class='form-group col-md-6'),
            ),
            'profile_image',
            'password',

            'profile_image',
            'password',
        )
        for field_name in self.fields:
            self.fields[field_name].help_text = None
class UserEditForm(UserBaseForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'profile_image', 'bio']
        help_texts = {}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['profile_image'].widget.clear_checkbox_label = ''
        self.fields['profile_image'].widget.clear_checkbox = False

        for field in self.fields.values():
            field.help_text = ''