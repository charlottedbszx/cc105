from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import PredictionForm
import joblib
import pandas as pd
import matplotlib.pyplot as plt

model = joblib.load('random_forest_model.pkl')

def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('predict')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def predict(request):
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            
            pregnancy = 1 if data['pregnancy'] == 'yes' else 0
            glucose_map = {'low': 80, 'normal': 120, 'high': 160}
            bp_map = {'low': 60, 'normal': 80, 'high': 100}
            skin_map = {'normal': 20, 'swollen': 40}

            glucose = glucose_map[data['glucose_level']]
            blood_pressure = bp_map[data['blood_pressure']]
            skin_thickness = skin_map[data['skin_thickness']]
            insulin = data['insulin']
            bmi = data['bmi']
            diabetes_pedigree = data['diabetes_pedigree']
            age = data['age']

            features = [
                pregnancy,
                glucose,
                blood_pressure,
                skin_thickness,
                insulin,
                bmi,
                diabetes_pedigree,
                age
            ]

            prediction = model.predict([features])
            result = "Diabetic" if prediction[0] == 1 else "Not Diabetic"

            return render(request, 'predict.html', {'form': form, 'prediction': result})
    else:
        form = PredictionForm()

    return render(request, 'predict.html', {'form': form})

@login_required
def dashboard(request):
    df = pd.read_csv('diabetes.csv')
    chart = df['Outcome'].value_counts().plot(kind='bar', title='Target Distribution')
    plt.savefig('predictor/static/chart.png')
    return render(request, 'dashboard.html', {'chart_url': 'chart.png'})
