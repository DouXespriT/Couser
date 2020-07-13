from django import forms

class contact_form(forms.Form):
    subject = forms.CharField(label='Subject', max_length=500, required=True)

class transaction_form(forms.Form):
    t_id = forms.CharField(label='Transaction ID ',min_length=15, max_length=15, required=True)
