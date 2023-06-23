from django import forms

from .models import *


class CreateQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['short_description', 'description', 'code']
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


class CreateCodeForm(forms.ModelForm):
    class Meta:
        model = Code
        fields = ['short_description', 'code_text', 'type']
        widgets = {
            'short_description': forms.TextInput(attrs={
                'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 '
                         'px-4 mb-3 leading-tight focus:outline-none focus:bg-white text-center'}),
            'code_text': forms.Textarea(attrs={
                'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 '
                         'px-4 mb-3 leading-tight focus:outline-none focus:bg-white'}),
            'type': forms.Select(attrs={
                'class': 'appearance-none block w-full bg-gray-200 text-gray-700 border border-red-500 rounded py-3 '
                         'px-4 mb-3 leading-tight focus:outline-none focus:bg-white text-center'}),
        }


class CreateAnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ["short_description", "description", "question", "code"]
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
