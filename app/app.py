
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
