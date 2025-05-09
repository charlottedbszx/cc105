from django import forms

class PredictionForm(forms.Form):
    pregnancy = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], label="Are you pregnant?")
    glucose_level = forms.ChoiceField(choices=[
        ('low', 'Low'), ('normal', 'Normal'), ('high', 'High')
    ], label="Glucose Level")
    blood_pressure = forms.ChoiceField(choices=[
        ('low', 'Low'), ('normal', 'Normal'), ('high', 'High')
    ], label="Blood Pressure")
    skin_thickness = forms.ChoiceField(choices=[
        ('normal', 'Normal'), ('swollen', 'Swollen')
    ], label="Skin Thickness")
    insulin = forms.FloatField(label="Insulin Level")
    bmi = forms.FloatField(label="BMI")
    diabetes_pedigree = forms.FloatField(label="Diabetes Pedigree Function")
    age = forms.IntegerField(label="Age")
