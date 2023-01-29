from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Review
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class ProductForm(forms.ModelForm):
    """
    Form to add products
    """
    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-color rounded'


class ReviewForm(forms.ModelForm):
    """ Form for users to add reviews of products"""
    class Meta:
        model = Review
        fields = ('description', 'star_rating')
        widgets = {
            'description': SummernoteWidget,
            'star_rating': forms.NumberInput(attrs={'min': 1, 'max': '5', })
        }
