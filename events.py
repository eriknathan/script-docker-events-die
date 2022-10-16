import docker
import datetime
import requests
import os

client = docker.DockerClient(base_url='unix://var/run/docker.sock')
webhook_url = "#aqui vai o link do seu webhook do canal do discord"

for event in client.events(decode=True, filters={"event": "die"}):
    container_id = event["id"]
    container_name = event["Actor"]["Attributes"]["name"]
    epoch_date = event["time"] 
    date_time = datetime.datetime.fromtimestamp(epoch_date)  

    response = {"content": f'O CONTAINER FOI DERRUBADO!!! {os.linesep}- ID do Container: {container_id} {os.linesep}- Nome do Container: {container_name} {os.linesep}- Data e Hora: {date_time}'}

    print(response)
    requests.post(webhook_url, data=response)
    
