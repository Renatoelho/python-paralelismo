# Paralelismo no Python

O paralelismo no Python é uma técnica que permite a execução de várias tarefas ***simultaneamente***, aumentando a eficiência e a velocidade de processamento. Tarefas intensivas de uso de CPU geralmente não paralelizam de forma eficiente, enquanto tarefas de I/O têm melhor desempenho na paralelização, devido aos momentos de ociosidade da CPU, tornando o processo de paralelização mais efetivo.

No entanto, é importante observar que o Python tem uma limitação conhecida como Global Interpreter Lock (GIL), que impede várias threads de executar código Python simultaneamente em um único processo.

Uma maneira de implementar o paralelismo em Python é utilizando a biblioteca joblib. O joblib fornece ferramentas simples para paralelizar tarefas em Python com facilidade, especialmente para processamento em lote. Com o joblib, é possível paralelizar facilmente um loop ou uma função, distribuindo as iterações ou chamadas de função entre múltiplos núcleos de CPU.


# Apresentação em vídeo

<p align="center">
  <a href="https://youtu.be/C8B8ZLvHUWs" target="_blank"><img src="thumbnail/Paralelismo-Python.png" alt="Vídeo de apresentação"></a>
</p>


# Código de Implementação

```python

from joblib import Parallel, delayed


def numero_par(numero: int) -> bool:
    """
    Esta função, por utilizar a CPU de maneira intensa,
    não paraleliza de forma eficiente. Para mais detalhes,
    pesquise sobre: Python Global Interpreter Lock (GIL).
    """
    if numero % 2 == 0:
        return True
    else:
        return False


def consulta_numero(numero: int) -> bool:
    """
    Esta função, por fazer uso de recursos de I/O, o que por
    sua vez torna a CPU ociosa por alguns instantes, permite
    que a paralelização seja mais eficiente. Para mais detalhes,
    pesquise sobre: Python Global Interpreter Lock (GIL).
    """
    with open("./base_consulta.txt", "r+") as arquivo:
        base_consulta = [int(id.strip("\n")) for id in arquivo.readlines()]
    if numero in base_consulta:
        return True
    else:
        return False

lista_numeros = [id for id in range(0, 5_000_000)]

"""Funções que utilizam intensamente de CPU (Cálculos matemáticos) não paralelizam muito bem."""

# Execução em uma única thread
# resultado = [numero_par(numero) for numero in lista_numeros] 

# Execução em multiplas threads
# resultado = Parallel(n_jobs=10)(delayed(numero_par)(id) for id in lista_numeros)

"""Funções que utilizam de recuros de I/O paralelizam de forma mais eficiente."""

# Execução em uma única thread
#resultado = [consulta_numero(numero) for numero in lista_numeros] 

# Execução em multiplas threads
resultado = Parallel(n_jobs=10)(delayed(consulta_numero)(id) for id in lista_numeros)


print(f'A quantidade de itens da lista são: {len(lista_numeros)}')
print(f'Os 10 primeiros itens da lista são: {lista_numeros[:10]}...')
print(f'O resultado da aplicação da função é: {resultado[:10]}...')

```


# Referências:

Joblib: running Python functions as pipeline jobs, ***Joblib***. Disponível em: <https://joblib.readthedocs.io/en/stable/>. Acesso em: 22 mar. 2024.

Global Interpreter Lock - GIL, ***Python***. Disponível em: <https://wiki.python.org/moin/GlobalInterpreterLock> Acesso em: 22 mar. 2024.