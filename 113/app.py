import os

# para saber onde tem mais bibliotetas usar o site pypi existem vários

#criando diretorios
os.mkdir('Videos')
os.makedirs('Musicas' + os.sep + 'Ação')

print(os.path.isdir('Musicas'))

########################################################
#criar ler e modificar aruivos
with open('celulares.txt', 'w') as arquivo:
    arquivo.write('Olá meu nome é Viktor')

#update
nomes =['viktor','ana','maria']
with open('nomes.txt' ,'a', newline='') as arquivo:
    for nome in nomes:
        arquivo.write(nome + os.linesep)


# r le e r+ lê e escreve