

from utils.paraleliza import consulta_id
from utils.nao_paraleliza import numero_par

from joblib import Parallel, delayed



lista_ids = [id for id in range(1, 1_000_000)]

"""Execução onde o processmanto é paralelizado (Utilização de I/O)"""

#execucao = [consulta_id(resultado) for resultado in lista_ids]
execucao = Parallel(n_jobs=-1)(delayed(consulta_id)(id) for id in lista_ids)


"""Execução onde o processmanto não paraleliza de forma eficiênte (Utilização de CPU)"""

#execucao = [numero_par(resultado) for resultado in lista_ids]
#execucao = Parallel(n_jobs=-1)(delayed(numero_par)(id) for id in lista_ids)


print(execucao[:10])