from django.forms import ModelForm
from .models import Room

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        # exclude = ['created_at', 'updated_at']
        # widgets = {
        #     'name': {
        #         'attrs': {
        #             'class': 'form-control'
        #         }
        #     },
        #     'description': {
        #         'attrs': {
        #             'class': 'form-control'
        #         }
        #     },
        #     'capacity': {
        #         'attrs': {
        #             'class': 'form-control'
        #         }
        #     },
        #     'price': {
        #         'attrs': {
        #             'class': 'form-control'
        #         }
        #     },
        #     'image': {
        #         'attrs': {
        #             'class': 'form-control'
        #         }
        #     }
        # }