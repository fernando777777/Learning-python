'''
API Aplicacion Programing Interface
Nasa: get comets cometas del espacio 
Nasa API https://api.nasa.gov/
api_key Nasa: Vi62rU7uo64O2fsMWnNEuUWWyQ5XqMintLcRWPK9
DEVELOPER: EDWIN F. B.
DATA 24012024
SCRIPT DESCRIPTION: OBTENER Y LEER DATOS DE COMETAS DE LA NASA
'''
import requests
import os

os.system('clear')
def get_comet_data(api_key):
    print("::: COMET INFORMATION :::")
    url = f"https://api.nasa.gov/neo/rest/v1/neo/3726712?api_key={api_key}"

    try:
        #Realizar la solicitud a la API
        response = requests.get(url)
        response.raise_for_status() #=> Valida si se presenta algún error en la petición
        #Convertir la respuesta a formato JSON (JS Object Notation)
        datos = response.json()

        print(f"Comet name: {datos['name']}")
        print(f"Absolute magnitude: {datos['absolute_magnitude_h']}")
        print(f"Estimated diameter max (KM): {datos['estimated_diameter']['kilometers']['estimated_diameter_max']}")
        print(f"Estimated diameter max (FT): {datos['estimated_diameter']['feet']['estimated_diameter_max']}")

    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la petición a la API de NASA: {e}") 



api_key_nasa = 'Vi62rU7uo64O2fsMWnNEuUWWyQ5XqMintLcRWPK9'
get_comet_data(api_key_nasa)