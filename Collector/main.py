import time
from snap7 import util
from snap7 import client
from LoadTags import loadTags
from LoadDBs import loadDBs
from LoadMeasur import loadMeasur
from LoadGrupos import loadGrupos
from LoadGrupos import check_group_time
import logging
from restart import restart_program 
 
# initialize the log settings
logging.basicConfig(format='%(asctime)s - %(levelname)s:%(message)s', datefmt='%d/%m/%Y %H:%M:%S',filename = 'historian.log', level = logging.INFO)

# Configuracao do PLC
ipSiemens = '192.168.0.266'

def conection(ipSiemens):
    if not plc.get_connected() :
        try:
            print "Conectando ao PLC Siemens..."
            plc.connect(ipSiemens, 0, 2) # connect to PLC            
            msg1 = "Conectado ao PLC Siemens, IP:" + ipSiemens
            print msg1
            return True
        except Exception as e:
            print("Erro: "+str(e))
            return False
    else:
        return True

#converte o byte lido no PLC para seu respectivo tipo 
def read_tags():
    """
    length:          Proxima posicao pos a variavel desejada
    start:           location we are going to start the read
    """
    try:
        # Leitura das DBs pode ser ate em outra funcao
        for db in dbs.values():
            db.get_values(plc)
        
        for tag in tags:
            tag.set_value(dbs[str(tag.db)].data)
            if tag.write:
                mss[tag.measur].changed = True
            #print tag.get_valor()
        
        check_group_time(grupos)
        
        return True
    except Exception as e:
        print e
        return False #log_error("PLC Siemens falha de leitura na db:",db,cur)

if __name__ == "__main__":
    tags = loadTags()
    dbs = loadDBs()
    mss = loadMeasur(tags)
    grupos = loadGrupos(mss)
    plc = client.Client()
    erro = 0

    while True:
        if conection(ipSiemens) :
            try:
                read_tags()
                time.sleep(1)
                erro = 0
            except:
                erro += 1
        else:
            erro += 1
            if erro >=1:
                restart_program()
                erro = 0

