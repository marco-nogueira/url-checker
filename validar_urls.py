import csv
import requests

urls_acessadas = 0
urls_com_erro = 0

def validar_acesso_url(url):

    try:
        response = requests.get(url)
        if response.status_code == 200:
            global urls_acessadas
            urls_acessadas += 1
            print(f"Funcionamento correto para a URL: {url} [VALIDADOS {urls_acessadas}]")
        else:
            global urls_com_erro
            urls_com_erro += 1
            print(f"Erro ao tentar acessar a URL: {url} [ERROS {urls_com_erro}]")
    except requests.exceptions.ConnectionError:
        print(f"Erro de conexão ao tentar acessar a URL: {url}")

with open("lista-de-urls.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        url = row[0]
        validar_acesso_url(url)

print(f"Foram verificadas {urls_acessadas + urls_com_erro} URLs.")
print(f"Funcionando adequadamente há {urls_acessadas}.")
print(f"Outras {urls_com_erro} retornaram erro.")
