import json
import requests

resposta = requests.get("http://jsonplaceholder.typicode.com/todos")
if not resposta.status_code == 200:
    print("ERRO")
    exit(1)

lista_tarefa = json.loads(resposta.content.decode())

completas = []
incompletas = []

for tarefa in lista_tarefa:
    if tarefa["completed"]:
        completas.append(tarefa)
    else:
        incompletas.append(tarefa)

print("{} de {} tarefas estão completas.".
      format(len(completas), len(lista_tarefa)))

with open("completas.json", "w") as comp:
    json.dump(completas, comp, separators=(',', ':'))

with open("incompletas.json", "w") as incomp:
    json.dump(incompletas, incomp, separators=(',', ':'))
