palavra = input("insira a palavra: ")
busca = 'a'
contador = 0
for letra in palavra:
    if letra == busca:
        contador +=1
if contador == 0:
    print(f"não há letras {busca} na palavra {palavra}")
if contador == 1:
    print(f"foi encontrada {contador} repetição de {busca} na palavra {palavra}")
if contador > 1:
    print(f"foram encontrados {contador} repetições de {busca} na palavra {palavra}")