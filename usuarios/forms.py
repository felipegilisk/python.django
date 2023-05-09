from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label="Nome de Usuario",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': "form-control",
                'placeholder': "João da Silva"
            }
        )
    )
    senha = forms.CharField(
        label="Senha",
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'class': "form-control",
                'placeholder': "digite sua senha"
            }
        )
    )


class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label="Nome de Usuario",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': "form-control",
                'placeholder': "João da Silva"
            }
        )
    )
    email = forms.EmailField(
        label="E-mail",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': "form-control",
                'placeholder': "joao.silva@mail.com"
            }
        )
    )
    senha_1 = forms.CharField(
        label="Senha",
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'class': "form-control",
                'placeholder': "digite sua senha"
            }
        )
    )
    senha_2 = forms.CharField(
        label="Confirme sua senha",
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'class': "form-control",
                'placeholder': "digite sua senha novamente"
            }
        )
    )
