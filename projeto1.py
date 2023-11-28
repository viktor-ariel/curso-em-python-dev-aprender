from datetime import date
import random

nomeFunc = input("Digite seu nome: ")
idadeFun = input("Me fale sua idade (Somente número): ")
dataDoCadastroDoUsuario = date.today()


cartoes = ['R$ 50,00','R$ 250,00','R$ 120,00']
valorSorteado = random.choice(cartoes)

dataDeAniversario = input("Me sua data de aniversário (dd/mm/aaaa): ")

data_em_texto = dataDoCadastroDoUsuario.strftime('%d/%m/%Y')

print(f"Óla {nomeFunc}, seu regitro foi concluido no dia {data_em_texto}, e houve um sorteio e você ganhou {valorSorteado}")




