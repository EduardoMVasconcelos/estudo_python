#FUNCAO RANGE
#por padrão, o range é definido como (start=0, stop, step=1)


for n in range(10):
    print(n)
    
for x in range(20, 10, -1):
    print(x)
    
# continue = pula para a proxima estrutura de repetição
# break = termina o laço

string = 'Python'
nova_string = ''

for letra in string: #na primeira execução, letra = p
    if letra == 't':
        # continue = faria a letra T não ser adicionada ao resultado final (PyHon)
        nova_string = nova_string + letra.upper() #.upper = transforma em maiusculo 
    elif letra == 'h':
        nova_string += letra.upper()
        #break = faria a letra H ser a ultima adicionada a string (PyTH)
    else:
        nova_string += letra # como a nova_string é uma variavel vazia, é adicionado nela a letra do for
print(nova_string)