from django import forms
from .models import Crime

MISDOMEANOR_CLASSES = [
    (-1, 'Misdomeanor Class...'),
    (1, 'Class 1'),
    (2, 'Class 2'),
    (3, 'Class 3'),
    (4, 'Class 4')
]

FELONY_CLASSES = [
    (-1, 'Felony Class...'),
    (1, 'Class 1'),
    (2, 'Class 2'),
    (3, 'Class 3'),
    (4, 'Class 4'),
    (5, 'Class 5'),
    (6, 'Class 6'),
]

class AddFelon(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'First name of felon', 'class':'form'}), required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Last name of felon', 'class':'form'}), required=True)
    crime_committed = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Crime Committed", 'class':'form'}), required=True)
    class_s = forms.ChoiceField(widget=forms.Select(attrs={'class':'choose'}, choices=FELONY_CLASSES), required=True)

class AddMisdomeanor(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'First name of person who committed misdomeanor', 'class':'form'}), required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Last name of person who committed misdomeanor', 'class':'form'}), required=True)
    crime_committed = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Crime Committed", 'class':'form'}), required=True)
    class_s = forms.ChoiceField(widget=forms.Select(attrs={'class':'choose'}, choices=MISDOMEANOR_CLASSES), required=True)

class AddCharge(forms.Form):
    crime_committed = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Crime Committed", 'class':'form'}), required=True)
    class_s = forms.IntegerField(max_value=6, min_value=1, required=True)