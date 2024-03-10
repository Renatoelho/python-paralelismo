from joblib import Parallel, delayed

lista_de_um_bilhao_itens = [numero for numero in range(1, 50_000_001)]

def numero_par(numero: int) -> bool:
    if numero % 2 == 0:
        return True
    else:
        return False


print(lista_de_um_bilhao_itens[:6],"\n", lista_de_um_bilhao_itens[-6:-1])
print(len(lista_de_um_bilhao_itens))

#resultados = [numero_par(num) for num in lista_de_um_bilhao_itens]
resultados = Parallel(n_jobs=-1)(delayed(numero_par)(num) for num in lista_de_um_bilhao_itens)

print(resultados[:6],"\n", resultados[-6:-1])
print(len(resultados))