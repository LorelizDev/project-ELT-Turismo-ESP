# %%
import pandas as pd
import requests
from google.oauth2 import service_account
import pandas_gbq
# %%
def get_data(url, path):
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

def load_to_bigquery(path):
    credentials = service_account.Credentials.from_service_account_file(
        'credentials/project-elt-turismo-esp-98a96a2f8468.json',
    )
    df = pd.read_csv(path, delimiter=';')
    df['Periodo'] = pd.to_datetime(df['Periodo'], format='%YM%m')

    pandas_gbq.to_gbq(
    df, 'bronze_tourism.bronze_tourism_raw', project_id='project-elt-turismo-esp', if_exists='append', credentials=credentials
    )

#%%
URL = 'https://www.ine.es/jaxiT3/files/t/csv_bdsc/48423.csv'
PATH = 'data/tourism_spain_dataset.csv'
# get_data(URL, PATH)
load_to_bigquery(PATH)
# %%
