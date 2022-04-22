from keras.models import load_model

import pandas as pd
import joblib

import os

path_parent = os.path.dirname(os.getcwd())  # Grab the previous path from the current directory
path_model = (path_parent + '\\machine_learning\\model\\loan_model')
path_scaler = (path_parent + '\\machine_learning\\model\\scaler.jbl')


# Load model and scaler
model = load_model(path_model)
scaler, dummies_frame = joblib.load(path_scaler)


def scale_data(data):
  # Grab the input data from the request, convert to DataFrame
  df = pd.DataFrame(data, index=[0])

  df = pd.get_dummies(df)
  df = df.reindex(columns=dummies_frame, fill_value=0)

  unit = scaler.transform(df)

  return unit


def submit_candidature(data):

  unit = scale_data(data)

  # Run model to predict
  y_pred = model.predict(unit)
  y_pred = (y_pred > 0.55)

  new_df = pd.DataFrame(y_pred, columns=['Status'])
  new_df = new_df.replace({True: 'Approved', False: 'Rejected'})

  return 'Your Status is {}'.format(new_df.values)
