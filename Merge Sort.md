### **Explicação**:

<br>
Divide em duas partes, pegando o meio da lista e separando entre esquerda e direita e recursivamente faz o mesmo com cada sublista separada da lista, em seguida junta essas duas sublistas.

<br>

### **Representação literal**:
<br>

``` python
    [2, 4, 1] == tamanho 3
    tamanho:3 == 1?
        não -> 
        divide: [2] [4, 1]
        margeSort([2])
        mergeSort([4, 1])
        [2] == tamanho 1?
            sim -> [2]
        [4, 1] == tamanho 1?
            não -> 
            divide: [4] [1]
            margeSort([4])
            mergeSort([1])
            [4] == tamanho 1?
                sim -> [4]
            [1] == tamanho 1?
                sim -> [1]
            merge([4], [1])
            resultado = []
            len([4]) maior que i=0 e
            len([1]) maior que j=0?
                sim -> 
                [4] menor que [1]?
                    não -> 
                    resultado recebe [1] e j += 1
            resultado = [1]
            len([4]) maior que i=0 e
            len([1]) maior que j=1?
                não -> 
                stopLoop
            resultado += [4] do indice 1 pra frente: [4]
            resultado += [1] do indice 0 pra frente: []
            resultado = [1, 4]   
        merge([2], [1, 4])
            resultado = []
            len([2]) maior que i=0 e
            len([1, 4]) maior que j=0?
                sim -> 
                [2] menor que [1]?
                    não -> 
                    resultado recebe [1] e j += 1
            resultado = [1]
            len([2]) maior que i=0 e
            len([1, 4]) maior que j=1?
                sim -> 
                [2] menor que [4]?
                    sim -> 
                    resultado recebe [2] e i += 1
            resultado = [1, 2]
            len([2]) maior que i=1 e
            len([1, 4]) maior que j=1?
                nao -> 
                stopLoop
            resultado += [2] do indice 1 pra frente: []
            resultado += [1, 4] do indice 1 pra frente: [4]
            resultado = [1, 2, 4]
    final = [1, 2, 4]
```