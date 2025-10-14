import requests
import os.path

url = "https://www.ssp.sp.gov.br/assets/estatistica/transparencia/spDados/SPDadosCriminais_2025.xlsx"

path_dest = "data"

file_name = "SPDadosCriminais_2025.xlsx"

file_path = os.path.join(path_dest, file_name)

try:
    print("Download iniciado. Aguarde...")
    response = requests.get(url=url)
except:
    print("ERRO:Não foi possível finalizar o download.")

if response.status_code == 200:
    with open(file_path, "wb") as file:
        file.write(response.content)

    print("Download concluido!")
else:
    print(f"Falha no Download: status code {response.status_code}")