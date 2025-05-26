from django import forms

class ContactForm(forms.Form):
    feedback = forms.CharField(
        label='Contactează-ne',  # Changed the label here
        widget=forms.Textarea(attrs={
            'rows': 4,
            'cols': 50,
            'placeholder': 'Scrie aici mesajul tau ...',
            'id': 'feedback'
        }),
        min_length=20
    )