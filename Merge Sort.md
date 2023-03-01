### **Explicação**:

<br>
Divide em duas partes, pegando o meio da lista e separando entre esquerda e direita e recursivamente faz o mesmo com cada sublista separada da lista, em seguida junta essas duas sublistas.

<br>

### **Representação literal**:
<br>

``` python
[2, 1] == tamanho 1?
não -> divide: [2] [1]
margeSort([2])
mergeSort([1])
    [2] == tamanho 1?
    sim -> [2]
    [1] == tamanho 1?
    sim -> [1]
merge([2], [1])
    resultado = []
    len([2]) maior que i=0 e
    len([1]) maior que j=0?
        sim -> [2] menor que [1]?
            não -> resultado recebe [1] e j += 1
    resultado = [1]
    len([2]) maior que i=0 e
    len([1]) maior que j=1?
        não -> stopLoop
        resultado += [2] index 0 pra frente = [2]
        resultado += [1] index 1 pra frente = []
final = [1, 2]
```