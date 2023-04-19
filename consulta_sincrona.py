import time

import requests
from faker import Faker

fake = Faker('pt-BR')

# Gerando uma lista de ceps para utilizar na consulta
ceps = []
for _ in range(10):
    ceps.append(fake.postcode(formatted=False))

resultados = []

inicio = time.time()

for cep in ceps:
    print(f'Consultando CEP: {cep}')
    resultados.append(requests.get(f'https://viacep.com.br/ws/{cep}/json/'))

fim = time.time()
tempo_total = fim - inicio
print(
    f'Levou {round(tempo_total, 3)} segundos para consultar {len(ceps)} CEPs na API'
)
print(f'Ou seja,  {round(tempo_total / len(ceps), 2)} segundos por CEP')
print('Terminamos!')
