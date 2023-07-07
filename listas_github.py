print("1. FUNCION DUPLICAR UN VALOR EN LA LISTA CON DICHO INDICE DADO")
def doble_index(lista, index):
    if index >= len(lista):
            return lista
    else:
            nueva_lista = lista[0:index]
            nueva_lista.append(lista[index] * 2)
            nueva_lista = nueva_lista + lista[index + 1:]
            return nueva_lista
print("------------------------")
print(doble_index([2, 8, -8, 24], 2))


print("2. CON ESTA FUNCION EL PROGRAMA NOS DIRÁ CUAL ES EL NUMERO DE LA LISTA SE REPITE")
def mas_repetido(lista, objeto1, objeto2):
  if lista.count(objeto1) >= lista.count(objeto2):
    return objeto1
  else:
    return objeto2
print("------------------------")
print("MAS REPETIDO: ")
print(mas_repetido([7, 7, 8, 8, 7, 8, 8, 8, 9], 8, 9))


print("3. USO DE LA FUNCION .RANGE() PARA QUE LA LISTA QUE EMPIECE DESDE EL 81 Y VAYA HASTA EL 100 DE DOS EN DOS")
def final(contador):
    contador = list(range(contador, 102, 2))
    return contador
print("------------------------")
print(final(81))


print("4. FUNCION QUE DEVUELVE EL VALOR CENTRAL DE UNA LISTA SI ES IMPAR, PERO DEVUELVE LA MEDIA DE DOS ELEMENTOS CENTRALES SI ES PAR.")
def mediana(lista):
  if len(lista) % 2 == 0:
    lista_final = lista[int(len(lista)/2)]+ lista[int(len(lista)/2)-1]
    return lista_final
  else:
    return lista[int(len(lista)/2)]
print("------------------------")
print(mediana([1, 2, 3, 4, -4, -5, 10, -8, 8, 7]))
print(mediana([-3, 7, -9, 12, 1, -5, 6, -2, 4]))


print("5. FUNCION .ZIP() QUE PERMITE ADJUNTAR DOS LISTAS Y LAS CONVIERTE EN UNA LISTA 2D")
nombre = ["Emma", "Liam", "Sophia", "Noah", "Olivia"]
edad = [25, 42, 18, 37, 55]
datos = zip(nombre, edad)
print("------------------------")
print(list(datos))

