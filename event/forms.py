from django import forms
from event.models import EventDetail, EventReg
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

class EventForm(forms.ModelForm):

    CHOICES = ( 
    ('', ''),
    ('solo', 'Solo'),
    ('dual', 'Dual'),
    ('squad', 'squad'),
    )


    title = EventDetail.title
    email = forms.EmailField(required=True)
    fullname = forms.CharField(max_length=255, required=True)
    contact = forms.CharField(max_length=255, required=True)
    squadname = forms.CharField(max_length=255, required=True)
    membernumber = forms.ChoiceField(choices = CHOICES, required=True)

    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['fullname'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['contact'].widget.attrs['class'] = 'form-control'
        self.fields['squadname'].widget.attrs['class'] = 'form-control'
        self.fields['membernumber'].widget.attrs['class'] = 'form-control'
        self.fields['p1name'].widget.attrs['class'] = 'form-control'
        self.fields['p1userid'].widget.attrs['class'] = 'form-control'
        self.fields['p2name'].widget.attrs['class'] = 'form-control'
        self.fields['p2userid'].widget.attrs['class'] = 'form-control'
        self.fields['p3name'].widget.attrs['class'] = 'form-control'
        self.fields['p3userid'].widget.attrs['class'] = 'form-control'
        self.fields['p4name'].widget.attrs['class'] = 'form-control'
        self.fields['p4userid'].widget.attrs['class'] = 'form-control'
    
    class Meta:
        model = EventReg
        fields = (
             "title",
             "fullname",
             "email", 
             "contact",
             "squadname", 
             "membernumber", 
             "p1name", 
             "p1userid", 
             "p2name", 
             "p2userid",
             "p3name", 
             "p3userid",
             "p4name", 
             "p4userid",
             )

    def clean_email(self):
        email = self.cleaned_data.get('email')

        try:
            validate_email(email)
        except ValidationError:
            raise ValidationError("Enter Correct Email Address")
        
        if EventReg.objects.filter(email = email).count()>0:
            raise ValidationError("Email Already Exists. Enter New Email Address.")
        return email
            

    
  
