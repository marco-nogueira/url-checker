# url-checker

Este aplicativo serve para verificar o funcionamento das urls de uma página.

Após o python e as bibliotecas necessárias ao uso estiverem instaladas.

Abrir o prompt de comando e executar o arquivo:

- python url_checker-v3.py
  
Então abrirá uma janela para inserir a URL que quer pesquisar, por exemplo https://google.com.br.

O sistema vai varrer a página e identificar todos os links/urls que existem na página. Criará e salvará a lista no arquivo lista_de_urls.csv na pasta resultados.

No próximo passo o sistema vai verificar, tentar abrir cada link/url salvo na lista_de_urls.csv.

O resultado do teste de tentativa de acesso é escrito no arquivo urls_status_report.txt.

