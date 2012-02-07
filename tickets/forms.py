from django import forms
from tickets import models

def optional(choices):
    return (('',''),) + choices
class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea,
            required=False)
    change_status = forms.ChoiceField(
            choices=optional(models.TICKET_STATUS_CHOICES), 
            required=False)
    closed_reason = forms.ChoiceField(
            choices=optional(models.TICKET_CLOSED_REASONS),
            required=False)
