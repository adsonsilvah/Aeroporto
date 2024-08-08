## Sobre o projeto
Este foi desenvolvido para a materia de algoritimos e estrutura de dados.
A ideia consistiu em um sistema de gerenciamento de passagens aéreas, aplicando os
conceitos da disciplina. Todo o projeto foi desenvolvido em Python e foi usado a biblioteca Numpy.

## O projeto possui a seguinte estrutura:
- Checkin.py: classe para adicionar e deletar um passageiro a fila
- aeroporto_main.py: principal arquivo, é onde roda toda a aplicação, chamando funções classes e também a interação com o terminal através de inputs
- assentos.py: classe para escolha de assentos no avião
- checkout.py: classe para que seja feito o checkout dos passageiros após a chegada do voo
- escolhas.py: Neste arquivo existem duas classes, onde uma classe, escolhas, vai mostrar as cidades de origem e destino e permitir a escolha para o passageiro.
  essa classe utiliza mais duas classes, a classe quicksort, para ordenar a lista de voos disponíveis e classe buscabinaria, para buscar a cidade pretendida pelo passageiro.

## Como rodar
Todo o projeto foi feito para rodar localmente via terminal, basta fazer o clone e executar o arquivo aeroporto_main.py
