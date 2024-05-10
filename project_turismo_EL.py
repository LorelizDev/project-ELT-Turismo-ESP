# %%
import numpy as np
import pandas as pd
import pandas_gbq.schema
import requests
from google.oauth2 import service_account
import pandas_gbq
import unicodedata

# %%
def get_data(url, path):
    """
    Funcion que descarga un archivo desde una URL y lo guarda en un archivo local.
    Args:
        url (str): URL del archivo a descargar.
        path (str): Ruta del archivo local donde guardar el archivo descargado.

    Returns:
        None
    """
    # Realizamos la solicitud HTTP para descargar el archivo
    r = requests.get(url)

    # Verificamos que la solicitud fue exitosa (código de estado 200)
    if r.status_code == 200:
        # Guardamos la información descargada en el archivo local
        with open(path, 'wb') as f:
            f.write(r.content)
        print(f"Archivo descargado exitosamente en: {path}")
    else:
        print(f"Error al descargar el archivo. Código de estado: {r.status_code}")

def format_data(path):
    df = pd.read_csv(path, delimiter=';')
    
    df = df.rename(columns=lambda x: x.lower().replace(' ', '_'))
    df = df.rename(columns=lambda x: unicodedata.normalize('NFKD', x).encode('ascii', 'ignore').decode('utf-8'))
    df = df.replace({'..':np.nan}).replace({'.':np.nan})

    for col in df.columns:
        if col == 'periodo':
            df[col] = pd.to_datetime(df[col], format='%YM%m')
        elif col == 'total':
            df[col] = df[col].str.replace('.', '').str.replace(',', '.').astype(float)
        elif col == 'comunidades_y_ciudades_autonomas':
            df[col] = df[col].fillna('Total Nacional').reset_index(drop=True).astype(str)

    df.to_csv('data/tourism_spain_dataset_formatted.csv', index=False)
        
    return df

def load_to_bigquery(path):
    credentials = service_account.Credentials.from_service_account_file(
        'credentials/project-elt-turismo-esp-98a96a2f8468.json',
    )

    df = format_data(path) 
    pandas_gbq.to_gbq(
    df, 'bronze_tourism.tourism_spain_raw', project_id='project-elt-turismo-esp', if_exists='replace', credentials=credentials
    )

#%%
URL = 'https://www.ine.es/jaxiT3/files/t/csv_bdsc/48423.csv'
PATH = 'data/tourism_spain_dataset.csv'
# %%
get_data(URL, PATH)
load_to_bigquery(PATH)
# %%
