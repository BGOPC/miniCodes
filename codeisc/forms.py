from django import forms

from .models import *


class CreateQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['short_description', 'description', 'code']
        widgets = {
            'short_description': forms.TextInput(attrs={
                'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-sky-600 rounded py-3 '
                         'px-4 mb-3 leading-tight focus:outline-none focus:bg-gray-300 text-center'}),
            'description': forms.Textarea(attrs={
                'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-sky-600 rounded py-3 '
                         'px-4 mb-3 leading-tight focus:outline-none focus:bg-gray-300'}),
            'code': forms.CheckboxSelectMultiple(attrs={
                'class': 'bg-gray-200 text-gray-700 border border-sky-600 rounded py-3 '
                         'px-4 mb-3 focus:outline-none focus:bg-gray-300',
            }),
        }


class CreateCodeForm(forms.ModelForm):
    class Meta:
        model = Code
        fields = ['short_description', 'code_text', 'type']
        widgets = {
            'short_description': forms.TextInput(attrs={
                'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-sky-600 rounded py-3 '
                         'px-4 mb-3 leading-tight focus:outline-none focus:bg-gray-300 text-center'}),
            'code_text': forms.Textarea(attrs={
                'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-sky-600 rounded py-3 '
                         'px-4 mb-3 leading-tight focus:outline-none focus:bg-gray-300'}),
            'type': forms.Select(attrs={
                'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-sky-600 rounded py-3 '
                         'px-4 mb-3 leading-tight focus:outline-none focus:bg-gray-300 text-center'}),
        }


class CreateAnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ["short_description", "description", "question", "code"]
        widgets = {
            'short_description': forms.TextInput(attrs={
                'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-sky-600 rounded py-3 '
                         'px-4 mb-3 leading-tight focus:outline-none focus:bg-gray-300 text-center'}),
            'description': forms.Textarea(attrs={
                'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-sky-600 rounded py-3 '
                         'px-4 mb-3 leading-tight focus:outline-none focus:bg-gray-300'}),
            'code': forms.CheckboxSelectMultiple(attrs={
                'class': 'bg-gray-200 text-gray-700 border border-sky-600 rounded py-3 '
                         'px-4 mb-3 focus:outline-none focus:bg-gray-300',
            }),
        }
