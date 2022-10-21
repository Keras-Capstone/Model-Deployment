from django.shortcuts import render

import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

def diagnose(input_data, filename):
    """Make prediction based on inputed data"""
    # Load the saved model
    loaded_model = pickle.load(open(filename, 'rb'))
    data = pd.DataFrame({'mean_radius': [input_data[0]],
                        'mean_texture': [input_data[1]],
                        'mean_perimeter': [input_data[2]],
                        'mean_area': [input_data[3]],
                        'mean_smoothness': [input_data[4]]})

    prediction = loaded_model.predict(data)[0]

    if prediction == 0:
        diagnosis = 'The tumor is Benign i.e not malignant'
    elif prediction == 1:
        diagnosis = 'The tumor is Malignant'

    return diagnosis

# Create your views here.

def index(request):
    """Input page"""

    return render(request, 'deployment/index.html')


def predict(request):
    """Prediction Results"""

    print(request.POST)
    mean_radius = float(request.POST.get('mean_radius'))
    mean_texture = float(request.POST.get('mean_texture'))
    mean_perimeter = float(request.POST.get('mean_perimeter'))
    mean_area = float(request.POST.get('mean_area'))
    mean_smoothness = float(request.POST.get('mean_smoothness'))

    input_data = [mean_radius, mean_texture, mean_perimeter, mean_area, mean_smoothness]
    diagnosis = diagnose(input_data, filename = 'finalized_model_BreastCancer.h5')

    # 

    return render(request, 'deployment/predict.html', {'prediction': diagnosis})