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

dia = 0
semana = ['Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']
while dia < 7:
    print("Hoy es " + semana[dia])
    dia += 1

x = "Eric"

for letter in x:
    if letter == 'i':
        continue
print(letter)

contador_indice = 0
palabra = 'hola'

for letter in palabra:
    print(palabra[contador_indice])
    contador_indice +=1

palabra = 'hola'
for index,letter in enumerate(palabra):
    print(index)
    print(letter)
    print('\n')

# Creacion de Funciones

# Funcion Decir Hola
def decir_hola():
    print('Hola')
    print('como')
    print('estas')
decir_hola()

def suma(num1,num2): # Funcion para Sumar 2 numeros
    total = num1 + num2
    print(total)

suma(1,2)

def chequear_numero_par_en_lista(num_lista):
    for number in num_lista:
        if number % 2 == 0:
            print('True')
            return True
            
        else:
            pass
        print('False')
        return False

chequear_numero_par_en_lista([1,3,6])

def func(*args):
    #Retornar el 5 % de a y b
    return print(sum(args) * 0.05)
 
func(40,60,760)

def funcion(**kwargs):
    if 'fruta' in kwargs:
        print('Mi fruta escogida es {}'.format(kwargs['fruta']))
    else:
        print('No hay fruta')
funcion(fruta= 'manzana', veggie = 'lechuga')

def func (*args, **kwargs):
    print(args)
    print(kwargs)
    print('Me gustaria {}{}'.format(args[0], kwargs['comida']))

func(10,30,50, comida ='leche', animal = 'perro')

numeros = [1,2,3,4,5]

def square(num):
    result = num**2
    return result

for item in map(square,numeros):
        print(item)
        
numeros = [1,2,3,4,5]

def square(num):
    result = num**2
    return result
print(list(map(square,numeros)))        


numeros = [1,2,3,4,5,6,7,8,10]
def chekar_pares(num):
    return num%2 == 0

for n in filter(chekar_pares,numeros):
    print(n)


name = 'VARIABLE GLOBAL'

def saludo():
        name = 'erick Alexander'
        
        def hola():
            print('Hola ' + name)
        hola()
            
saludo()

'''
x = 50

def func():
    global x
    print(f'X es {x} el valor GLOBAL')
    x = 'NUEVO VALOR'
    print(f'Fui Localmente cambiada de X a {x}')
    
func()
print(x)
    
    