#O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, 
# que já é um sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa que monta a tabela 
# de preços de pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário,
# conforme o exemplo abaixo:

preco = float(input("Preço do pão: "))
unidade = preco
contador = 1

while contador <= 50:
    print(f"{contador} - R$ {preco:.2f}")
    contador += 1
    preco += unidade