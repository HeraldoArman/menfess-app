from django import forms
from menfess_app.models import Menfess, Reply

class CreateMenfess(forms.ModelForm):
    class Meta:
        model = Menfess
        fields = ('from_name', 'to_name', 'message')
        
        widgets = {
            'from_name' : forms.TextInput(attrs={'class':'form-control', 
                                                 'placeholder': 'someone',
                                                 'name': 'from',
                                                 'id': 'from',
                                                 'type': 'text'}),
            'to_name' : forms.TextInput(attrs={'class': 'form-control',
                                               'placeholder': 'Crush',
                                                'name': 'to',
                                                'id': 'to',
                                                'type': 'text'}),
            'message' : forms.Textarea(attrs={'class': 'form-control',
                                               'placeholder': 'Hi, Love U',
                                                'name': 'message',
                                                'id': 'message',}),
            
        }
        
        
class ReplyMenfess(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('from_reply_name', 'reply_message')
        
        widgets = {
            'from_reply_name' : forms.TextInput(attrs={'class':'form-control', 
                                                 'placeholder': 'someone',
                                                 'name': 'from_reply_name',
                                                 'id': 'from_reply_name',
                                                 'type': 'text'}),
            'reply_message' : forms.Textarea(attrs={'class': 'form-control',
                                               'placeholder': 'Hi, Love U',
                                                'name': 'reply_message',
                                                'id': 'reply_message',
                                                'rows': 2}),
        }