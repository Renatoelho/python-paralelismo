

def consulta_id(id: int) -> bool:
    with open("./bases/base_consulta.txt", "r+") as arquivo:
        base_consulta = [int(id.strip("\n")) for id in arquivo.readlines()]
    if id in base_consulta:
        return True
    else:
        return False