'''
micadena = "hola mundo"
print((micadena[::]))

name ="Pam"
ultimas_letras = name[1:]
print('P'+ultimas_letras)

letra ='z'
letra = letra * 10

print(letra)

x = 'hola mundo'
x = x.split()
print (x)

print('Esta es una cadena de {}'.format('TEXTO'))


print('Esta {0} {1} {2}'.format('es','una','cadena'))

resultados = 100/888
print("Los resultados son {r:1.3f}".format(r=resultados))

mi_lista =['uno','dos','tres']
otra_lista = ['cuatro','cinco']
nueva_lista = mi_lista + otra_lista
nueva_lista[0] = 'Eric'
print(nueva_lista)

mi_lista = ['a','z','x','b','d']
num_lista = [4,1,5,7,3]

mi_lista_ordenada = mi_lista.sort()
print(mi_lista)


# Diccionario
mi_diccionario = {'manzanas':'2.90','kekes':['manzana','platano'],'leche':'5.90'}
print(mi_diccionario['kekes'])

t = ('a','a','b')
lista = [1,2,3]
print(t.count('a'))


hambre = True
sed = True

if hambre and not sed:
    print("Tenemos hambre")
elif hambre ==True and sed == True:
    print("Tenemos hambre y Sed")
    
else:
    print('Estamos LLenos')

d = {'y1':3,'y2':1,'y3':22}

for llave,valor in d.values():
    print(valor)
'''
dia = 0
semana = ['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']
while dia < 7:
    print("Hoy es " + semana[dia])
    dia += 1