# [Testes de Software] Prática 2 - PUCMinas

Prática de automação de testes!
Faça o que se pede:
- baixe o arquivo sample-exercise.html
- faça automação do seguinte cenário usando Selenium Webdriver
com Python:
- Abra a página no browser de sua preferência
- Clique no botão “generate”. Um código será gerado abaixo do
botão como na figura ao lado
- Capture o código e preencha o campo de texto com ele
- Clique no botão “test”
- Um alerta com o texto “Done!” será exibido
- Feche o alerta
- Uma mensagem no formato “It workls! <código>!” será
exibida
- Capture a mensagem e verifique se o valor está correto
- faça um vídeo do teste sendo executado 3 vezes seguidas e envie
para o professor
- envie o código fonte do script para o professor
Data: próxima aula
Valor: 10 pontos

# Setup

## Envrironment

```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Install the Selenium Webdriver

For Firefox you can use [geckodriver](https://github.com/mozilla/geckodriver). For other browsers you can check in the [Selenium Documentation](https://selenium-python.readthedocs.io/installation.html)Mainteined by the community.

# Running

Just execute the code below to run the test case:

```sh
python -m unittest main.py
```