#coding utf=8
#Importando módulo json
import json
#Importando módulo regex
import re
#importando módulo requests
import requests

#Abrindo arquivo json
with open('transactions.json') as jsonFile:
    #Convertendo arquivo json para objeto python
    jsonFile = json.load(jsonFile)

for data in jsonFile[0:]:
    #Listando nomes de clientes
    name = data['customer']['name']
    #Listando nomes nos cartões dos clientes
    cardName = data['card_hold_name']
    #Listando estados/país dos clientes
    state = data['customer']['state']
    #Listando localização de IP da transação
    ip = data['ip_location']
    #Listando data de nascimento de clientes
    birthDate = data['customer']['birth_date']
    #Listando telefones de clientes
    phone = data['customer']['phone']
    #Listando ID da transação
    id = data['id']

    #Formatando para mostrar apenas o ano de nascimento do cliente
    birthYear = re.sub(r'\-.*','', birthDate)
    #Convertendo ano de nascimento de string para int
    birthYear = int(birthYear)

    #Formatando para mostrar apenas o DDD do telefone do cliente
    ddd = re.sub(r'\ 9.*', '', phone)
    #Convertendo DDD de string para int
    ddd = int(ddd)

    #Definindo score de risco
    risk_score = 0

    #Se o nome do cliente não for o mesmo que o nome do cartão o risco soma 25 pontos
    if name != cardName:
        risk_score = risk_score + 25

    #Se a localização do IP da transação for diferente do estado do cadastro do cliente o risco soma 25 pontos
    if ip != state:
        risk_score = risk_score + 25

    #Se o cliente for menor de 18 anos o risco soma 25 pontos
    if birthYear > 2002:
        risk_score = risk_score + 25

    #Definindo os DDDs de cada estado
    #Se o DDD do telefone do cliente for diferente do estado do cadastro o risco soma 25 pontos
    if ddd == 11:
        ddd = 'SP/BR'
        if ddd != state:
            risk_score = risk_score + 25
    elif ddd == 21:
        ddd = 'RJ/BR'
        if ddd != state:
            risk_score = risk_score + 25
    elif ddd == 41:
        ddd = 'PR/BR'
        if ddd != state:
            risk_score = risk_score + 25
    elif ddd == 47:
        ddd = 'SC/BR'
        if ddd != state:
            risk_score = risk_score + 25
    elif ddd == 48:
        ddd = 'SC/BR'
        if ddd != state:
            risk_score = risk_score + 25
    elif ddd == 51:
        ddd = 'RS/BR'
        if ddd != state:
            risk_score = risk_score + 25
    elif ddd == 65:
        ddd = 'MT/BR'
        if ddd != state:
            risk_score = risk_score + 25
    elif ddd == 71:
        ddd = 'BH/BR'
        if ddd != state:
            risk_score = risk_score + 25

    #Definindo as informações que quero enviar ao endpoint
    payload = {'customer': name, 'ID Transaction': id, 'Risk Score': risk_score}
    #URL do endpoint
    url = 'https://reqres.in/api/users'

    #Enviando as informações em metodo POST para o endpoint
    sendServer = requests.post(url, json=payload)

    #Imprimindo resposta do endpoint
    print(sendServer.text)
