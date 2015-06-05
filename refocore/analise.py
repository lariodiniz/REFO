# coding: utf-8

from datetime import datetime
import os
import hashlib
#----Código adquirido no link:http://stackoverflow.com/questions/1131220/get-md5-hash-of-big-files-in-python



def md5_for_file(path, block_size=256*128, hr=False):
    '''
    Block size directly depends on the block size of your filesystem
    to avoid performances issues
    Here I have blocks of 4096 octets (Default NTFS)
    '''
    md5 = hashlib.md5()
    with open(path,'rb') as f:
        for chunk in iter(lambda: f.read(block_size), b''):
             md5.update(chunk)
    if hr:
        return md5.hexdigest()
    return md5.digest()
#----

def Analise(caminho, extensao):
    """Esta Funcao recebe como parametros um diretorio e uma extencao.
        Elaverifica todos os arquivos desntro deste diretorio com a extencao recebida e retorna um dicionario com as repitidas.
    """    
    arquivos={}
    print "horas: %i:%i:%i" %(datetime.now().hour, datetime.now().minute, datetime.now().second)
    for nomearq in os.listdir(caminho):
        if nomearq[len(nomearq)-3:] ==  extensao or nomearq[len(nomearq)-3:] ==  extensao.upper():
            arquivos[nomearq]=md5_for_file(caminho+"/"+nomearq, hr=True)
    
    retorno={}
    arquivo=arquivos.keys()
    for x in arquivo:
        for y in arquivo[:]:
            if x != y:                
                if arquivos[x] == arquivos[y]:
                    if retorno.has_key(x):
                        retorno[x].append(y)
                    else:
                        retorno[x]=[y]
                    arquivo.remove(y)
                

    print "horas: %i:%i:%i" %(datetime.now().hour, datetime.now().minute, datetime.now().second)   
    return retorno
    





