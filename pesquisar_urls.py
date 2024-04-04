import csv
import time
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

    # Salvar o HTML de retorno em um arquivo
    with open("retorno.html", "wb") as f:
        f.write(response.content)

    # Localizar todas as URLs relacionadas ao texto href
    soup = BeautifulSoup(response.content, "html.parser")
    urls = [a["href"] for a in soup.find_all("a", href=True) if "http" in a["href"]]

    # Criar um arquivo CSV com as URLs
    with open("lista-de-urls.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["URL"])
        writer.writerows(urls)

    # Exibir mensagem de sucesso e fechar a janela
    messagebox.showinfo("Sucesso", "Pesquisa finalizada! As URLs foram salvas no arquivo lista-de-urls.csv.")
    root.destroy()

# Criar a interface gráfica
root = Tk()
root.title("Pesquisar URLs")

# Criar a caixa de texto para a URL
url_label = Label(text="Digite a URL:")
url_label.pack()

url_entry = Entry(width=50)
url_entry.pack()

# Criar o botão para iniciar a pesquisa
pesquisar_button = Button(text="Pesquisar URLs do domain name", command=pesquisar_urls)
pesquisar_button.pack()

# Iniciar a interface gráfica
root.mainloop()
