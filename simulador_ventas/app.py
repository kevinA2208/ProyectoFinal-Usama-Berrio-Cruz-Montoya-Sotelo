import flask
from flask import Flask, render_template, request
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

# Cargamos el cerebro entrenado
model = joblib.load('simulador_ventas\modelo_ridge.pkl')
scaler = joblib.load('simulador_ventas\escalador.pkl')
model_columns = joblib.load('simulador_ventas\columnas_modelo.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Recibimos los datos crudos
            data = {
                'Item_Identifier': request.form['Item_Identifier'],
                'Item_Weight': float(request.form['Item_Weight']),
                'Item_Fat_Content': request.form['Item_Fat_Content'],
                'Item_Visibility': float(request.form['Item_Visibility']),
                'Item_Type': request.form['Item_Type'],
                'Item_MRP': float(request.form['Item_MRP']),
                'Outlet_Establishment_Year': int(request.form['Outlet_Establishment_Year']),
                'Outlet_Size': request.form['Outlet_Size'],
                'Outlet_Location_Type': request.form['Outlet_Location_Type'],
                'Outlet_Type': request.form['Outlet_Type']
            }
            
            # Convertimos a DataFrame (1 sola fila)
            df = pd.DataFrame([data])
            
            # Extraemos las dos primeras letras (FD, DR, NC) del ID del item
            df['Item_Category_Code'] = df['Item_Identifier'].apply(lambda x: x[:2])
            df = df.drop('Item_Identifier', axis=1)

            # B. Mapeo Manual (Ordinales y Binarias)
            map_size = {'Small': 0, 'Medium': 1, 'High': 2}
            map_loc = {'Tier 1': 0, 'Tier 2': 1, 'Tier 3': 2}
            map_fat = {'Low Fat': 0, 'Regular': 1}

            df['Outlet_Size'] = df['Outlet_Size'].map(map_size)
            df['Outlet_Location_Type'] = df['Outlet_Location_Type'].map(map_loc)
            df['Item_Fat_Content'] = df['Item_Fat_Content'].map(map_fat)

            # C. One-Hot Encoding (Nominales)
            # Aplicamos dummies
            df = pd.get_dummies(df)

            df = df.reindex(columns=model_columns, fill_value=0)

            # E. Escalado (MinMax)
            df_scaled = scaler.transform(df)

            # El modelo predice en LOGARITMO
            prediction_log = model.predict(df_scaled)
            
            # Convertimos a DINERO REAL (Exponencial)
            prediction_real = np.expm1(prediction_log)[0]
            resultado_texto = f"${prediction_real:,.2f}"

            return render_template('index.html', prediction_text=f'Ventas Estimadas: {resultado_texto}', original_input=data)

        except Exception as e:
            return render_template('index.html', prediction_text=f'Error en el cálculo: {str(e)}')

if __name__ == '__main__':
    app.run(debug=True)