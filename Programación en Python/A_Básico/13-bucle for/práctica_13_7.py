# Listas de frutas y verduras
frutas = ["manzana", "naranja", "plátano"]
verduras = ["zanahoria", "apio", "espinaca"]

# Vamos a combinar cada fruta con cada verdura para hacer jugos
print("Ideas de jugos combinados:")

for fruta in frutas:
    for verdura in verduras:
        print("- Jugo de " + fruta + " y " + verdura)

# Listas de Frutas y Verduras: 
# Definimos dos listas, una con frutas y otra con verduras.
# Bucle For Externo: 
# Este bucle recorre cada elemento en la lista de frutas.
# Bucle For Interno: 
# Dentro del bucle de frutas, hay otro bucle que recorre cada elemento en la lista de verduras.
# Imprimir Combinaciones: 
# Para cada par de fruta y verdura, imprimimos una sugerencia de jugo combinado.