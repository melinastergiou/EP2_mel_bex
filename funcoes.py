# FUNÇÕES BASE DO EP2

def normaliza_bp(DADOS):
    bpaises = {}

    for continente in DADOS:
        pcont = DADOS[continente]
        for pais in pcont:
            infop = pcont[pais]
            infop['continente'] = continente

            bpaises[pais] = infop 

    return bpaises 