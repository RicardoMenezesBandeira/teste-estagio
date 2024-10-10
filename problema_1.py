verificar = int(input("insira o número: "))#recebe e converte para inteiro
def fibonachi(x,y,z):
    if z == x:#verifica se é o número atual da sequencia
        print("o numero inserido faz parte da sequencia")
        exit()
    if x>z:#verifica se o numero a ser verificado é menor que o numero atual da sequencia
        print("o numero inserido não faz parte da sequencia")
        exit()
    if x==0:# verifica se o x esta como zero e inicia a sequencia
        #print(x)
        x=1
        #print(x)
        fibonachi(x,y,z)
    else:
        aux = x
        x = x+y
        y= aux
        #print(x)
        fibonachi(x,y,z)
fibonachi(0,0,verificar)
    
