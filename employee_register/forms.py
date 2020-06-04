from django import forms
from . models import Employee

class EmployeeForm(forms.ModelForm):

     class Meta:
        model = Employee
        fields = ('name','mobile','emp_code','position')
        labels = {
           'name':'Full Name',
           'moobile':'Mobile',
           'emp_code':'Emp Code',
           'position':'Position'
        }

     def __init__(self,*args,**kwargs):
         super(EmployeeForm,self).__init__(*args,**kwargs)
         self.fields['position'].empty_label = "Select"
         self.fields['emp_code'].required = False

          
          

