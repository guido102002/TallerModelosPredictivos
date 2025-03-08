#Transforme la cadena El mejor regalo? El perdón... en el mejor perdón utilizando 
#únicamente los métodos de listas que hemos visto. La nueva cadena debe guardarse en la variable nueva_frase:

def TransformarTexto():
    texto = "El mejor regalo? El perdón..."
    lista=texto.split()
    print(lista)
    
    lista.remove("regalo?")
    lista.pop(2)
    lista[0] = lista[0].lower()
    print(lista)
    
    #Se convierte la lista de palabras a lista de caracteres para 
    nueva_lista=[list(palabra) for palabra in lista]
    print(nueva_lista)
    #Se eliminan los puntos (...)
    nueva_lista[-1] = [caracter for caracter in nueva_lista[-1] if caracter not in ['.', '...']]
    print(nueva_lista)
    
    nueva_frase = " ".join(["".join(palabra) for palabra in nueva_lista])
    print(nueva_frase)
    
TransformarTexto()