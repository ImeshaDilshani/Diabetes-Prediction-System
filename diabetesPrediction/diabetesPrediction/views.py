from django.shortcuts import render
from joblib import load
from django.http import HttpResponse

# Load the trained model
trained_model = load('trained_model.joblib')

# Create your views here.
def index(request):
    if request.method == 'POST':
        # Get the form data
        Pregnancies = float(request.POST.get('Pregnancies'))
        Glucose = float(request.POST.get('Glucose'))
        BloodPressure = float(request.POST.get('BloodPressure')) 
        SkinThickness = float(request.POST.get('SkinThickness'))
        insulin = float(request.POST.get('insulin'))
        BMI = float(request.POST.get('BMI'))
        DiabetesPedigreeFunction = float(request.POST.get('DiabetesPedigreeFunction'))
        Age = int(request.POST.get('Age'))

        # Make prediction
        input_data = [[Pregnancies, 
                       Glucose, 
                       BloodPressure, 
                       SkinThickness, 
                       insulin,
                       BMI, 
                       DiabetesPedigreeFunction, 
                       Age]]  # Include all input features
        prediction = trained_model.predict(input_data)

        # Pass the prediction to the template
        return render(request, 'home.html', {'prediction': prediction[0]})
    
    return render(request,'home.html', {'prediction': None})