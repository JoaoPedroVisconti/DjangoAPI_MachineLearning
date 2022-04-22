from keras.models import load_model

import pandas as pd
import joblib

# Load scaler
scaler, dummies_frame = joblib.load(
    'F:\\Visconti\\DevProgram\\Tutorial\\Django\\MachineLearning\\DjangoAPI_MachineLearning\\machine_learning\\model\\scaler.jbl')


print('Running Scaler ...')


def scale_data(data):
  df = pd.DataFrame(data)
  df = pd.get_dummies(df)
  df = df.reindex(columns=dummies_frame, fill_value=0)

  unit = scaler.transform(df)

  return unit
