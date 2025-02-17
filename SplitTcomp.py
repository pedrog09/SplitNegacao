def split_negation(texto, delimitador):
    saida = []
    buffer = ""
    secaoDelimitador = False
    
    i = 0
    while i < len(texto):
        if texto[i:i+len(delimitador)] == delimitador:
            if buffer:
                saida.append(buffer)
                buffer = ""
            secaoDelimitador = True
            buffer += delimitador
            i += len(delimitador)
        else:
            if secaoDelimitador:
                saida.append(buffer)
                buffer = ""
                secaoDelimitador = False
            buffer += texto[i]
            i += 1
    
    if buffer:
        saida.append(buffer)
    
    return saida

# Exemplo de uso
texto_teste = "abc#def#ghi#jkl"
delimitador = "#"
print(split_negation(texto_teste, delimitador))
