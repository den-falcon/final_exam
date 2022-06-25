from django import forms

from webapp.models import Advertisement, Category


class SearchForm(forms.Form):
    search = forms.CharField(max_length=30, required=False, label="Найти")


class BaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update(
                {
                    'class': 'form-control input-default',
                    'placeholder': self.fields[field].label
                }
            )


class AdvertisementForm(BaseForm):
    class Meta:
        model = Advertisement
        fields = (
            'title',
            'description',
            'category',
            'price',
            'image',
        )


class CategoryForm(BaseForm):
    class Meta:
        model = Category
        fields = (
            'name',
            'description',
        )
