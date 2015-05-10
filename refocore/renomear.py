# coding: utf-8

import os            

def Renomear(caminho, extencao, nome=""):
    """Esta Funcao recebe como parametros um diretorio, uma extencao e um nome.
        Ela renomeia todos os arquivos desntro deste diretorio e com a extencao recebida para o nome recebido ordenando de acordo com otamanho de cada arquivo
    """    
    arquivos={}
    ta=0
    for nomearq in os.listdir(caminho):
        if nomearq[len(nomearq)-3:] ==  extencao or nomearq[len(nomearq)-3:] ==  extencao.upper():
            ta+=1
            arquivos[nomearq]=int(os.path.getsize(caminho+"/"+nomearq))
    
    lista=arquivos.keys()
    
    for x in reversed(sorted(arquivos.values())):
        for y in lista:
            if x == arquivos[y]:
                try:
                    os.rename(caminho+"/"+y, caminho+"/"+nome+str(ta)+"."+extencao)
                    lista.remove(y)
                    ta-=1
                except:
                    return 0

    return 1
