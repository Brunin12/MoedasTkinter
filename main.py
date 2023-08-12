import requests
from tkinter import *
from time import sleep


def obter_cotacoes():
    url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"

    try:
        response = requests.get(url)
        data = response.json()

        cotacoes = {
            'dolar': data['USDBRL']['bid'],
            'euro': data['EURBRL']['bid'],
            'bitcoin': data['BTCBRL']['bid']
        }

        return cotacoes
    except Exception as e:
        print(f"Erro ao obter as cotações: {e}")
        return None


def mostrar_cotacao():
    cotacoes = obter_cotacoes()
    cotacao['text'] = f'''
    Dólar: R$ {cotacoes['dolar']}
    Euro: R$ {cotacoes['euro']}
    Bitcoin: R$ {cotacoes['bitcoin']}'''


janela = Tk()

janela.title("Cotação Moedas")
# janela.geometry("250x100")

orientacao = Label(janela, text="Clique para ver as cotações (USD, EUR, BTC)")
orientacao.grid(column=0, row=0, padx=10, pady=10)

botao_cotacao = Button(janela, text="Pegar Cotação", command=mostrar_cotacao)
botao_cotacao.grid(column=0, row=1, padx=10, pady=10)

cotacao = Label(janela)
cotacao.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop()

# Janela 2
janela2 = Tk()
janela2.title("Olá Mundo")
ola_mundo = Label(janela2, text="Olá Mundo!", padx=10, pady=10)
ola_mundo.grid(column=0, row=0)

janela2.mainloop()
