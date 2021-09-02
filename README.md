# A API Conjunto foi desenvolvida para resolver as operações da Teoria de Conjuntos

## Funcionalidades:
- Inserir um Conjunto
- Inserir um Elemento em um Conjunto
- Obter o tamanho de um Conjunto
- Identificar se um conjunto contém um Elemento
- Identificar se um Conjunto é Subconjunto de 
- União de Conjuntos
- Interseção de Conjuntos
- Encontrar o complemento de um Conjunto
- Obter a diferença entre dois Conjuntos
- Encontrar o Conjunto das partes de um Conjunto

## Baixando a API e dependências.
- Fazer o clone do repositório:
```
git clone https://github.com/vinisantt/ApiConjuntos.git
```

- Executar testes de unidade:

```
python -m unittest discover tests -v
```

# Exemplos de utilização:
Para usar a API, abra o arquivo `usaConjunto.py` em um editor de código de sua preferencia.
Como descrito acima a API disponibiliza alguma funcionalidades que resolvem algumas operações da Teoria de Conjuntos.

Um Conjunto é uma estrutura que agrupa objetos e constitui uma base para construir estruturas mais complexas.
Segue uma definição mais formal: Um conjunto é uma coleção de zero ou mais objetos distintos, chamados elementos do conjunto, os quais não possuem qualquer ordem associada. Dessa forma, os elementos (que podem ser qualquer coisa: números, pessoas, frutas) são indicados por letra minúscula e definidos como um dos componentes do conjunto.
Um Conjunto também tem como componente um nome e tamanho. Os elementos de um Conjunto são separados por vírgula e normalmente dentro de chaves, como por exemplo: `A = {a, e, i, o, u}`.

## Inserir um Conjunto:
Para inserir um novo Conjunto deve-se adicionar uma variável que vai receber a instância de um novo objeto do tipo Conjunto, como parâmetro do objeto deve ser passado o Nome seguido dos Elementos do Conjunto.
### Exemplo:
```
A = Conjunto("A", 5, 3, 1)
```
*Os Elementos de um Conjunto não se repetem, então essa funcionalidade além de adicionar um novo Conjunto, ela também verifica se o próximo Elemento Contém no Conjunto que está sendo criado.*

## Inserir um Elemento em um Conjunto:
Antes de inserir um Elemento em um Conjunto, primeiro deve ter sido criado um elemento antes, como é demonstrado em Inserir um Conjunto. Com o conjunto criado vamos chamar a função inserir() na variável que o Conjunto foi instanciado e passar como parâmetro os elementos que deseja adicionar
### Exemplo:
```
A.inserir(4)
```
*Os Elementos de um Conjunto não se repetem, então essa funcionalidade além de adicionar os novos Elementos no Conjunto, ela também verifica se o Elemento Contém no conjunto.*

## Imprimir um Conjunto:
Para visualizar o Conjunto basta chamar a função imprimir(), ela não requer nenhum parâmetro e retorna a impressão do Conjunto.
### Exemplo:
```
A = Conjunto("A", 5, 3, 1)
A.imprimir()
```
#### Retorno:
```
A = {5, 3, 1}
```

## Obter tamanho de um Conjunto: 
Para obtermos o tamanho de conjunto basta chamar a função tamanho, ela não requer nenhum parâmetro e retorna a quantidade de elementos que o Conjunto que está chamando possui.
### Exemplo: 
```
A = Conjunto(“A”, 3, 4, 5)
A.tamanho().imprimir()
```
#### Retorno:
```
3
```

## Identificar se um Conjunto possui um elemento:
Para verificarmos se um elemento possui na lista precisamos utilizar a função possui, passando como parâmetro o elemento no qual deseja verificar, ao fazer isso, esta funcionalidade percorre sua lista de elementos à procura de um que seja igual ao elemento passado como parâmetro, caso encontre, retorna True (verdadeiro), caso não, retorna False (falso).
### Exemplo:
```
A = Conjunto(“A”, 3, 4, 5)
print(A.possui(5))
```
#### Retorno:
```
True
```

## Identificar se um Conjunto é Subconjunto de outro
Para verificar se um Conjunto é Subconjunto de outro Conjunto, deve chamar a função contem(), e passar como parâmetro um Conjunto ao qual deseja verificar se é um Subconjunto do Conjunto instanciado. Essa função retorna um boolean, se o Conjunto passado no parâmetro for Subconjunto do Conjunto instanciado, retornar true, caso contrário retorna false.
### Exemplo:
```
A = Conjunto("A", 1, 2, 3, (2, 9))
B = Conjunto("B", (2, 9))
print(A.contem(B))
```
#### Retorno:
```
True
```
*Para definir se um Conjunto é Subconjunto de um outro Conjunto deve verificar Se todos os elementos de um conjunto 𝐴 também são elementos de um conjunto 𝐵, então 𝐴 está contido em 𝐵, o que é representado por: 𝐴 ⊆ 𝐵. Isso também é lido como 𝐴 é subconjunto de 𝐵.*

## Verificar se um Conjunto esta Vazio
Para verificar se um Conjunto esta Vazio, deve chamar a função eh_vazio(), e passar como parâmetro o Conjunto que queira verificar. Essa função retorna um boolean, se o Conjunto passado no parâmetro for vazio, retornar true, caso contrário retorna false.
### Exemplo:
```
A = Conjunto("A", 1, 2, 3, (2, 9))
B = Conjunto("B", (2, 9))
print(A.eh_vazio())
```
#### Retorno:
```
False
```

## Verificar se 2 Conjuntos são Iguais
Para verificar se um Conjunto esta é Igual a outro, deve chamar a função eh_igual, e passar como parâmetro os 2 Conjunto que queira verificar. Essa função retorna um boolean, se os Conjuntos passados nos parâmetros forem iguais, retornar true, caso contrário retorna false.
### Exemplo:
```
A = Conjunto("A", 1, 2, 3, (2, 9))
B = Conjunto("B", (2, 9))
print(A.eh_igual())
```
#### Retorno:
```
False
```

## Identificar se um Conjunto é Subconjunto próprio de outro:
Para verificar se um Conjunto  é Subconjunto próprio de outro, utilizamos a função contemProp, que recebe como parâmetro um Conjunto, que ao ser chamada verifica primeiramente se o Conjunto passado é um subconjunto do elemento que chamou a função utilizando a função contem(Conjunto), caso não seja já retorna False (falso), caso não verifica se o tamanho dos dois conjuntos são iguais, caso seja, retorna False (falso), caso não retorna True (verdadeiro, é um subconjunto próprio).
### Exemplo:
```
A = Conjunto("A", 1, 2, 3, (2, 9))
B = Conjunto("B", (2, 9))
print(A.contem_propriamente(B))
print(B.contem_propriamente(A))
```
#### Retorno: 
```
True
False
```
*Um subconjunto próprio é quando um Conjunto é subconjunto de outro e há alguma diferença entre a quantidade de elementos do Conjunto que chama a função com o Conjunto passado como parâmetro.*

## União de Conjuntos:
Para fazer a união entre dois conjuntos deve utilizar a função união(), como parâmetro deve ser passado o conjunto que deseja fazer a união. A função verifica se o Conjunto passado é igual ao que foi instanciado, verifica se está vazia e depois executa um laço de repetição que chama a função inserir() e passa os Elementos como parâmetro,, que por sua vez faz a verificação se o Elemento contém no Conjunto.
### Exemplo:
```
A = Conjunto("A", 1, 2, 3, (2, 9))
B = Conjunto("B", (2, 9))
C = A.uniao(B)
C.imprimir()
```
### Retorno:
```
A ∪ B = {1,2,3,{9,2}}
```
*Sejam 𝐴 e 𝐵 dois conjuntos. A união entre eles, 𝐴 ∪ 𝐵, é definida como: 
𝐴 ∪ 𝐵 = {𝑥 ∣ 𝑥 ∈ 𝐴 ∨ 𝑥 ∈ 𝐵}. 
Considerando a lógica, o conjunto 𝐴 pode ser definido como 𝑥 ∈ 𝐴 e o conjunto 𝐵 pode ser definido como 𝑥 ∈ 𝐵. Ou seja, a propriedade de pertinência é utilizada para indicar uma proposição lógica.

## Interseção de Conjuntos:
Para obter a interseção utilizamos a função intersecao(Conjunto), que recebe como parâmetro um Conjunto, que ao ser chamada primeiramente verifica se os dois conjuntos são iguais, caso sejam, retorna um Conjunto contendo os elementos do Conjunto que chamou a função. Caso não sejam iguais, a função verifica se essa operação já foi feita (se consta na lista de operações ), caso tenha sido feita, ela recupera esse Conjunto armazenado e retorna. 
Caso a operação nunca tenha sido realizada e nenhum dos Conjuntos estejam vazios ela percorre a lista de elementos do Conjunto passado como parâmetro e verifica se esses elementos pertencem ao Conjunto que chamou a função, se sim esses elementos são adicionados ao Conjunto intersecao. Após terminar de percorrer, a lista de operações é incrementada com a operação atual possuindo como valor o conjunto intersecao. Isso ocorre para que na próxima vez que a mesma operação seja chamada com os mesmos Conjuntos não seja repetida.
### Exemplo:
```
A = Conjunto("A", 1, 2, 3, (2, 9))
B = Conjunto("B", (2, 9))
A.intersecao(B).imprimir()
```
### Retorno:
```
A ∩ B = {{2,9}}
```

## Obter a diferença entre dois Conjuntos:
Para obter a diferença entre dois conjuntos nós utilizamos a função diferenca(), que recebe como parâmetro um outro Conjunto, ao ser chamada verifica se essa operação já foi feita (se consta no dicionário de operações ), caso tenha sido feita, ela recupera esse Conjunto armazenado e retorna. Caso não, ele cria um novo Conjunto e adiciona os Elementos que são diferentes do Conjunto instanciado com o Conjunto passado como parâmetro.
### Exemplo:
```
X = Conjunto("X", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
Z = Conjunto("Z", 2, 4, 6, 8)
Y = X.diferenca(Z).imprimir()
```
### Retorno:
```
X - Z = {0,1,3,5,7,9}
```
## Encontrar o Conjunto das partes de um Conjunto:
Para obter o conjunto das partes de um Conjunto  utilizamos a função conjunto_das_partes(), que não recebe nenhum parâmetro, e quando chamada retorna um Conjunto cujos elementos são todas as combinações possíveis dos elementos do Conjunto que chamou a função.
### Exemplo:
```
A = Conjunto("A", 1, 2, (2, 9))
A.conjunto_das_partes()
```
## Retorno:
```
<Conjunto object>
- Conjunto.nome = 'Conjunto das Partes'
- Conjunto.elementos = [{}, {1}, {2}, {{2 9}}, {1, 2}, {1, {2, 9}}, {2, {2, 9}}, {1, 2, {2, 9}}]
```


## Integrantes:
- Jonhtan Mota Dos Reis - [jomrs](https://github.com/jomrs)
- Vinicius Dias Dos Santos - [vinisantt](https://github.com/vinisantt)
- Vinícius Lima - [yuichivls](https://github.com/yuichivls)
