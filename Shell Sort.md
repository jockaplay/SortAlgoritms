### **Explicação**:

<br>
O shell sort compara dois elementos em uma certa distância, se o elemento da direita for menor que o da esquerda, trocam-se as posições e verifica o elemento anterior com a mesma distância, até o elemento da direita estar no final da lista, depois disso, a distância é dividida pela metade e o processo se repete até a lista estar totalmente ordenada.

<br>

` Basicamente o insertion sort com uma distância fixa. `

<br>

### **Representação literal**:
<br>

```Python
[2, 1]
tamanho [2, 1] = 2
distancia = tamanho // 2 :1
tamanho maior que 0?
    sim -> j = distancia
    j:0 menor que tamanho:1?
        sim -> i = j:1 - distancia:1
        i é 0 ou maior? 
            sim -> [<i:0+distancia:1>:[2]] maior que [1]?
                não -> troca de posição [1, 2]
        j += 1
    j:1 menor que tamanho:1?
        não -> tamanho = tamanho // 2 :0
tamanho:0 maior que 0?
    não -> fim
```