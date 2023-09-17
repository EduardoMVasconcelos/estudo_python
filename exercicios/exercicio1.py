#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salario: "))
sexo = input("Informe seu sexo (f ou m): ")
estado_civil = input("Informe seu estado civil: (s, c, v ou d): ")

if len(nome) > 3 and idade >=0 and idade <=150 and salario < 0 and sexo == 'f' or salario == "m" and estado_civil == 's' or estado_civil == 'c' or estado_civil == 'v' or estado_civil == 'd':
    print("Dados validos")