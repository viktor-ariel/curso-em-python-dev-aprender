#csv arquivo separados por virgula.
# with open('csv_exemplo.csv') as arquivo:
#     dados = arquivo.read()
#     print(dados)

#lendo dados csv
from csv import DictReader,DictWriter

# with open('csv_exemplo.csv') as arquivo:
#     dados = DictReader(arquivo)
#     for dado in dados:
#         print(dado["age"] + ' ' + dado["age"] )

#criar arquivo csv
# with open('computadores.csv','w',newline='',encoding='utf-8') as arquivo:
#     cabecalho = ['MArca', 'preço', 'Ano de Lançamento']
#     CSV_write =  DictWriter(arquivo, fieldnames=cabecalho)
#     CSV_write.writeheader()
#     CSV_write.writerow({
#         'MArca': 'Asus',
#         'preço': 2500,
#         'Ano de Lançamento': 2020,
#     }),
#     CSV_write.writerow({
#         'MArca': 'Dell',
#         'preço': 2500,
#         'Ano de Lançamento': 2020,
#     }),
#     CSV_write.writerow({
#         'MArca': 'apls',
#         'preço': 2500,
#         'Ano de Lançamento': 2020,
#     }),
#     CSV_write.writerow({
#         'MArca': 'nokia',
#         'preço': 2500,
#         'Ano de Lançamento': 2020,
#     })

#alterar csv, criando um novo
with open('computadores.csv','r',newline='',encoding='utf-8') as arquivo_original:
    dados_originais = DictReader(arquivo_original)
    computadores = list(dados_originais)
    with open('computadores_2.csv','w',newline='',encoding='utf-8') as novo_arquivo:
        cabecalho = ['Marca', 'Preço', 'Ano de Lançamento']
        CSV_write =  DictWriter(novo_arquivo, fieldnames=cabecalho)
        CSV_write.writeheader()
        for computador in computadores:
             CSV_write.writerow({
            'Marca': computador["MArca"],#nesse segundo marca tem q ficar igual ao cabeçalho do original
            'Preço': 'R$' + computador["preço"],
            'Ano de Lançamento': computador["Ano de Lançamento"],
            })














