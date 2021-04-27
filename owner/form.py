from django import forms

from .models import Product

# class LoginForm(forms.Form):
#     username = forms.CharField(label='', widget=forms.TextInput(attrs ={"placeholder": "Username"}))
#     password = forms.CharField(label='', widget=forms.TextInput(attrs ={"placeholder": "Password"}))
    # class Meta:
    #     fielsd = [
    #         'username',
    #         'password'
    #     ]
    # def clean_username(self, *args, **kwargs):
    #     username = self.cleaned_data.get("username")


class ProductForm(forms.ModelForm):
    title = forms.CharField(label='', 
                    widget=forms.TextInput(attrs ={"placeholder": "Your Title"}))
   # email = forms.EmailField()
    description = forms.CharField(required=False, widget=forms.Textarea(
                                                    attrs = {
                                                        "placeholder": "Your descprition",
                                                        "rows": 20,
                                                        "cols": 120
                                                    }
    ))
    price = forms.DecimalField(initial=199.9)
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        # if not "CFE" in title:
        #     raise forms.ValidationError("This is an invalid title")
        for instance in Product.objects.all():
            if instance.title == title:
                raise forms.ValidationError("this is a title named " + title)
        return title
    
    # def clean_email(self, *args, **kwargs):
    #     email = self.cleaned_data.get("email")
    #     if not email.endswith("edu"):
    #         raise forms.ValidationError("This is an invalid email")
    #     return email
            

class RawProductForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs ={"placeholder": "Your Title"}))
    description = forms.CharField(required=False, widget=forms.Textarea)
    price = forms.DecimalField(initial=199.9)
