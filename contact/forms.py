from django import forms
from django.core.exceptions import ValidationError
from contact.models import Contact
from typing import Any


class ContactForm(forms.ModelForm):

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a classe-b',
                'placeholder': 'Aqui veio do init'
            }
        ),
        label='Primeiro nome',
        help_text='Escreva seu primeiro nome aqui'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields['first_name'].widget.attrs.update({
        #     'class': 'classe-a classe-b',
        #     'placeholder': 'Aqui veio do init'
        # })

    class Meta:
        model = Contact
        fields = (
            'first_name', 'last_name', 'phone'
        )
        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'class': 'classe-a classe-b',
        #             'placeholder': 'Escreva aqui'
        #         }
        #     )
        # }

    def clean(self) -> dict[str, Any]:
        # cleaned_data = self.cleaned_data

        self.add_error(
            'first_name',
            ValidationError(
                'Mensagem de erro',
                code='invalid'
            )
        )

        self.add_error(
            'first_name',
            ValidationError(
                'Mensagem de erro 2',
                code='invalid'
            )
        )

        return super().clean()
