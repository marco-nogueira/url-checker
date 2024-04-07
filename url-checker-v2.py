import csv
import os
from tkinter import *
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup

def pesquisar_urls():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Erro", "Digite uma URL válida.")
        return

    # Fazer request para obter o HTML de retorno
    try:
        response = requests.get(url)
    except requests.exceptions.ConnectionError:
        messagebox.showerror("Erro", "Falha na conexão com a internet.")
        return
    except requests.exceptions.HTTPError:
        messagebox.showerror("Erro", "Erro HTTP: " + str(response.status_code))
        return

    if os.path.isdir('results') == False:
        dirTemp = './results'
        try:
            os.mkdir(dirTemp)
        except OSError:
            os.rmdir(dirTemp)
            os.mkdir(dirTemp)

    # Salvar o HTML de retorno em um arquivo
    with open("results/retorno.html", "wb") as f:
        f.write(response.content)

    # Localizar todas as URLs relacionadas ao texto href
    soup = BeautifulSoup(response.content, "html.parser")
    urls = [a["href"] for a in soup.find_all("a", href=True) if "http" in a["href"]]

    # Criar um arquivo CSV com as URLs
    # Remover URLs duplicadas
    url_set = set()
    with open("results/lista-de-urls.csv", "w", newline="") as f:
        writer = csv.writer(f)
        for url in urls:
            if url not in url_set:
                writer.writerow([url])
                url_set.add(url)

    # Validar as URLs
    validar_urls()

    # Exibir mensagem de sucesso e fechar a janela
    messagebox.showinfo("Sucesso", "Pesquisa finalizada! As URLs foram salvas no arquivo lista-de-urls.csv, na pasta '/results'. Foram encontradas {} URLs.".format(len(url_set)))
    root.destroy()

def validar_urls():

    global urls_acessadas
    global urls_com_erro
    urls_acessadas = 0
    urls_com_erro = 0

    with open("results/lista-de-urls.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            url = row[0]
            validar_acesso_url(url)

    print(f"Foram verificadas {urls_acessadas + urls_com_erro} URLs, {urls_acessadas} funcionando e {urls_com_erro} com erro. ")

def validar_acesso_url(url):

    try:
        response = requests.get(url)
        if response.status_code == 200:
            global urls_acessadas
            urls_acessadas += 1
            print(f"Funcionamento correto para a URL: {url} [VALIDADOS = {urls_acessadas}]")
        else:
            global urls_com_erro
            urls_com_erro += 1
            print(f"Erro ao tentar acessar a URL: {url} [ERROS = {urls_com_erro}]")
    except requests.exceptions.ConnectionError:
        print(f"Erro de conexão ao tentar acessar a URL: {url}")

# Criar a interface gráfica
root = Tk()
root.title("Pesquisar e Validar URLs")

# Criar a caixa de texto para a URL
url_label = Label(text="Digite a URL:")
url_label.pack()

url_entry = Entry(width=50)
url_entry.pack()

# Criar o botão para iniciar a pesquisa
pesquisar_button = Button(text="Pesquisar e Validar URLs", command=pesquisar_urls)
pesquisar_button.pack()

# Iniciar a interface gráfica
root.mainloop()
