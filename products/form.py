from django import forms

from products.models import Review


class ReviewForm(forms.ModelForm)
    class meta:
        model = Review
        fields = ['']