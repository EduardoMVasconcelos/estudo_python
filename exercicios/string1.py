print("Compara duas strings")
string1 = input("String 1:")
string2 = input("String 2:")

print(f"Tamanho de: {string1}: {len(string1)}")
print(f"Tamanho de: {string2}: {len(string2)}")

if len(string1) == len(string2):
    print("As strings são do mesmo tamanho")
elif len(string1) != len(string2):
    print("As duas strings são de tamanhos diferentes")
    
if string1 == string2:
    print("As duas strings possuem o mesmo conteudo!")
    
elif string1 != string2:
    print("As duas strings possuem conteudo diferente!")