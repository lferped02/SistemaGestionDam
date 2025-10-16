#Nombre: LiLi Fernández Pedrosa 
# Grupo: 2ºDAM 

# 1. Crea tres listas con nombres de productos: ordenadores, periféricos y accesorios.
    #Hacemos una lista con todos los productos y después hay que imprimir,
    #ponemos lista [0], hasta el numero de lista que quieras, en cada lista hay que 
    #hay que hacer un print.
lista = ["Portatil", "Sobremesa", "Servidor"]
print (lista)
lista[0] = "Raton"
lista[1] = "Teclado"
lista[2] = "Monitor"
print (lista)
lista[0] = "Funda"
lista[1] = "Altavoces"
lista[2] = "Webcam"
print (lista)
#2. Crea un tupla con tres precios base distinto.
    #Creamos la tupla con la cantidad de precio que necesitas e imprimimos
tupla = (750, 1200, 2200)
print (tupla)

#3. Crea un diccionario llamado catalogo donde cada clave sea una categoría (“Ordenadores”, 
# “Periféricos”, “Accesorios”) y su valor sea la lista correspondiente.
    #Ponemos el nombre del diccionario = {y el nombre que queremos ponerle al diccionario}
    #e imprimimos lo que quieres que salga con el nombre del diccionario
ordenadores ={
    "Portatil": "Portatil ",
    "Sobremesa": "Sobremesa ",
    "Servidor" : "Servidor"
}
perifericos ={
    "Raton": "Raton",
    "Teclado": "Teclado",
    "Monitor": "Monitor"
}
accesorios={
    "Funda": "Funda ",
    "Altavoces": "Altavoces ",
    "Webcam": "Webcam"
}
print (ordenadores)
print (perifericos)
print (accesorios)

# 4. Muestra por pantalla:
#· Un acceso concreto: el segundo periférico.
    #Imprime el acceso que quieres, solo es poner el nombre del diccionario y el acceso.
print ("Segundo periferico: ", perifericos["Teclado"])