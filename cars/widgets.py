from django import forms


class NoClearableFileInput(forms.ClearableFileInput):
    def clear_checkbox_label(self, initial):
        return ''

    def render(self, name, value, attrs=None, renderer=None):
        self.template_with_clear = ''
        return super().render(name, value, attrs, renderer)
