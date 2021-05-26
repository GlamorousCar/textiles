from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(min_value=1,label='',widget=forms.NumberInput(attrs={"value":"1",'min':'1','max':'25',"class":"myfield"}))
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
