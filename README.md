##Hell-Triangle

Resolução do desafio "Hell Triangle"

##Problema
Dado o triângulo de números abaixo, encontrar o valor máximo total de cima para baixo. 

Exemplo:

```
    6
   3 5
  9 7 1
 4 6 8 4
```

Neste triângulo o valor máximo é:

```​
6 + 5 + 7 + 8 = 26
```

##Implementação

A implementação usou da estratégia de recursividade encontrando entre os nós esquerdos e direitos, o maior valor.

A linguagem Python foi escolhida para este algoritmo, pois é uma ótima linguagem com uma rica "standard lib", assim não precisamos da instalação de módulos/frameworks e podemos focar na resolução do problema.


Exemplo de consumo:

```
>>> hells_triangle = HellsTriangle()
>>> hells_triangle.max_sum_triangle([[6], [3, 5], [9, 7, 1], [4, 6, 8, 4]])
26
```

##Testes

Execução dos testes

```
python3.6 -m tests -v
```