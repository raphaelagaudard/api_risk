# API para analise de risco de fraude

## Conteudos
* [Info](#info)
* [Technologia](#technologia)
* [Rodando a API](#rodando_api)

## Info
O projeto é uma **api** que que avalia uma transação de um e-commerce e devolve um *score* de 0 a 100 de risco, sendo 0 (sem indícios de fraude) e 100 (com máximo risco de fraude). 

A api tem um **endpoint** que recebe via **POST** e como resultado mostra o ID de transação, nome e o score de risco do cliente.
	
## Technologia

O projeto foi criado com:

* Python 3

	
## Rodando a API

Pre-requisitos para rodar a api:

- Python 3 + Gerenciador de pacotes PIP

- Módulo requests:

$ pip3 install requests

Para rodar a api:

python3 api_risk.py

## Demonstração:

![Demonstração](./demo.gif)
