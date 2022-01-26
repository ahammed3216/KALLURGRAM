from django import forms



from phonenumber_field.modelfields import PhoneNumberField


class ProfileForm(forms.Form):
    first_name=forms.CharField(widget=forms.TextInput())
    second_name=forms.CharField(widget=forms.TextInput())
    address=forms.CharField(widget=forms.Textarea())
    email=forms.EmailField()
    phonenumber=forms.IntegerField()
    panchayath=forms.CharField(widget=forms.TextInput())
    ward=forms.IntegerField()
    house_no=forms.IntegerField(widget=forms.NumberInput)
    image=forms.ImageField()
    



class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
