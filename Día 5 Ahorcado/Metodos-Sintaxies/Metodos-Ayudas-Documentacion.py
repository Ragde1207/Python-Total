#La documentacion es el ver las guias que pycharm ofrece, para esto se debe colocar el puntero sobre
#una funcion y el mismo pycharm mostrara la ayuda

lista = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
print(lista.lstrip(",:_#%"))

frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(3,"naranja")
print(frutas)

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
print(marcas_smartphones.isdisjoint(marcas_tv))