from django import forms
from .models import *


class CreateQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['short_description', 'description', 'code', 'score']
        widgets = {
            'short_description': forms.TextInput(attrs={
                'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 '
                         'px-4 mb-3 leading-tight focus:outline-none focus:bg-white text-center'}),
            'description': forms.Textarea(attrs={
                'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 '
                         'px-4 mb-3 leading-tight focus:outline-none focus:bg-white'}),
            'code': forms.CheckboxSelectMultiple(attrs={
                'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 '
                         'px-4 mb-3 leading-tight focus:outline-none focus:bg-white'}),
        }
