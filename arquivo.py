import hamming

manipulador = open('binario.txt', 'r')
escrever = open('hamming.txt', 'w')

print('metodo readline()\n')
i = 0
hamming_txt = []
while i < 12:
    binario = manipulador.readline()
    new_binario = []
    print(binario)
    for value in binario:
        if value != '\n':
            new_binario.append(value)
    print(new_binario)
    convertido = hamming.hamming(new_binario, 0)
    hamming_txt.append(convertido)
    print(convertido)
    print('-----------------------------------')
    i += 1
manipulador.close()
escrever.writelines(str(hamming_txt))

escrever.close()

'''@programador_who'''
