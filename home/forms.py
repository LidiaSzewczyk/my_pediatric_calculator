from datetime import date, timedelta

from django import forms
from django.core.validators import MaxValueValidator
from django.forms import DecimalField, ChoiceField, NullBooleanField


class CalcForm(forms.Form):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),
                                 required=None,
                                 label='OBLICZ WIEK - podaj datę urodzenia',
                                 validators=[MaxValueValidator(limit_value=(date.today() - timedelta(days=1)),
                                                               message='Podaj datę z przeszłości')])
    bmi = NullBooleanField(label='OBLICZ BMI - podaj wagę i wzrost', widget=forms.CheckboxInput, required=None)
    weight = DecimalField(label='WAGA w kg', decimal_places=1, min_value=1, max_value=300, required=None)
    height = DecimalField(label='WZROST w cm', decimal_places=1, min_value=40, max_value=250, required=None)

    glucose_unit = ChoiceField(label='GLUKOZA', choices=(('mg/dl', 'mg/dl'), ('mmol/l', 'mmol/l')), initial='mmol/l',
                               widget=forms.RadioSelect, required=None)
    glucose_val = DecimalField(label='', decimal_places=1, min_value=0, max_value=2000, required=None)
    rr = DecimalField(label='EKG - aby obliczyć  akcję serca podaj odległość RR w mm i przesuw papieru', decimal_places=1, min_value=0, max_value=200, required=None)
    speed = ChoiceField(label='przesuw papieru', choices=(('25', '25 mm/s'), ('50', '50 mm/s')), initial='50',
                        widget=forms.RadioSelect, required=None)
    qt = DecimalField(label='EKG -aby obliczyć QTc podaj odległość QT w mm oraz uzupełnij wyżej odległość RR i przesuw papieru ', decimal_places=1, min_value=0, max_value=200, required=None)
