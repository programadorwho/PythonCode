
''' Do livro aprendendo python - pag 125 '''
d2 = {'spam' : 2, 'ham' : 1, 'egga' : 3} #'spam' eh a chave, 2 o valor.
print d2['spam'] #busca valor pela chave
print len(d2) #numero de entradas do dicionario
print d2.has_key('ham') #teste de participacao de chave como membro
if 'ham' in d2: #teste alternativo de participacao
    print 'contem'
print d2 #imprimi dicionario
'''
Obs: os dicionarios sao mutaveis
No Pythin, todos os tipos de dados de colecao podem ser aninhados dentro
de outros, arbitrariamente.
'''
d2['ham'] = ['grill', 'bake', 'fry'] #altera a entrada
print d2 #{'egga': 3, 'ham': ['grill', 'bake', 'fry'], 'spam': 2}
del d2['egga'] #exclui entrada
print d2 #{'ham': ['grill', 'bake', 'fry'], 'spam': 2}
d2['brunch'] = 'bacon' #adiciona uma nova entrada (no inicio)
print d2 #{'brunch': 'bacon', 'ham': ['grill', 'bake', 'fry'], 'spam': 2}

''' Ordenando dicionario '''
d = {'b' : 2, 'a' : 1, 'd' : 4, 'c' : 3}
ordenada = list(d.keys()) #cria uma nova lista com as chaves
print(ordenada) #['a', 'c', 'b', 'd'] imprimi sem ordem
ordenada.sort() #coloca as chaves em ordem
print(ordenada) #['a', 'b', 'c', 'd'] imprimi ordenada
for value in ordenada:
    print(value, "=", d[value]) #('a', '=', 1)... d[value] > imprimi o valor relacionado a chave
for value in sorted(d): #outro modo de ordenar, mais pratico.
    print(value, "=", d[value])
''' @programador_who '''
'''
 aulas particulares de programação - 85 999273805
'''
