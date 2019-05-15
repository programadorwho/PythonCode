
''' Verifica quantos multiplos de 2 existem num intervalo '''
def pot2(tamanho):
    i = 0
    multiplos = []
    while(2**i <= tamanho):
        multiplos.append(2**i)
        i += 1
    return multiplos, i


''' adiciona as paridades exe: p1, p2, p3... '''
def hamming_p(binario):
    hamming_code = []
    j = 0
    tamanho = len(binario)
    multiplos, i = pot2(tamanho)
    for value in range(i + tamanho):
        if (value + 1) not in multiplos:
            hamming_code.append(binario[j])
            j += 1
        else:
            hamming_code.append("p")
    print(hamming_code)
    return hamming_code


''' varre o codigo com pulos '''
def xy_xn(x, codigo_h):
    x1 = x
    x2 = x
    i = 0
    for value in range(x - 1, len(codigo_h)):
        if x > 0:
            if codigo_h[value] == "1":
                i += 1
            x -= 1
        else:
            if x1 > 0:
                x1 -= 1
                if x1 == 0:
                    x = x2
                    x1 = x2
    return i


def hamming(codigo, paridade):
    codigo_h = hamming_p(codigo)
    x = 1
    p = 0
    indice = 0
    for value in codigo_h:
        if value == 'p':
            i = xy_xn(x, codigo_h) #retorna a quantidade de 1
            if paridade == 0: #PAR
                if i % 2 == 0:
                    codigo_h[indice] = '0'
                else:
                    codigo_h[indice] = '1'
            p += 1
            x = 2**p
        indice += 1
    return codigo_h

    '''@programador_who'''
