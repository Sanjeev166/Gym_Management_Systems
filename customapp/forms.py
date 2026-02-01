from django import forms 
from .models import *


class Plans_Form(forms.ModelForm):
    class Meta:
        model = Plans
        fields = '__all__'
        widgets = {
            "Duration": forms.TextInput(attrs={"class":"p-add"}),
            "Price": forms.NumberInput(attrs={"class":"p-add"}),
            "Session": forms.TextInput(attrs={"class":"p-add"}),
        }

               
class Members_Form(forms.ModelForm):
    class Meta:
        model = Members        
        fields = ['user', 'Address', 'Mobile', 'Plan'] 
     

class Members_Details_Form(forms.ModelForm):
    class Meta:
        model = Members_Details  
        fields = '__all__'        
        
        
               