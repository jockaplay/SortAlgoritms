### **Explicação**:

<br>
O shell sort compara dois elementos em uma certa distância, se o elemento da direita for menor que o da esquerda, trocam-se as posições e verifica o elemento anterior com a mesma distância, até o elemento da direita estar no final da lista, depois disso, a distância é dividida pela metade e o processo se repete até a lista estar totalmente ordenada.

<br>

` Basicamente o insertion sort com uma distância fixa. `

<br>

### **Representação literal**:
<br>

```Python
    [4, 2, 1]
    tamanho [2, 4, 1] = 3
    distancia = tamanho // 2 :1
    tamanho maior que 0?
        sim -> 
        j = distancia:1 :1
        j:1 menor que tamanho:3?
            sim -> 
            i = j:1 - distancia:1 :0
            i:0 é 0 ou maior? 
                sim -> 
                [<i:0+distancia:1>:[4]] maior que [<i:1>:2]?
                    não -> 
                    troca [4, 2] de posição :[2, 4, 1]
                    i = i:0 - distancia:1 :-1
            i:-1 é 0 ou maior?
                não -> 
                para
            j += 1 :2
        j:2 menor que tamanho:3?
            sim -> 
            i = j:2 - distancia:1 :1
            i:1 é 0 ou maior? 
                sim -> 
                [<i:1+distancia:1>:[1]] maior que [<i:1>:[4]]?
                    não -> 
                    troca [4, 1] de posição :[2, 1, 4]
                    i = i:1 - distancia:1 :0
            i:0 é 0 ou maior?
                sim -> 
                [<i:0+distancia:1>:[1]] maior que [<i:0>:[2]]?
                    não -> 
                    troca [2, 1] de posição :[1, 2, 4]
                    i = i:0 - distancia:1 :-1
            i:-1 é 0 ou maior?
                não -> 
                para
            j += 1 :3
        j:2 menor que tamanho:3?
            não ->
            para
    tamanho:0 maior que 0?
        não -> 
        para
    fim
    [1, 2, 4]
```