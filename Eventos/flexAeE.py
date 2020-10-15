import time
from snap7 import util
from snap7 import client
from LoadTags import loadTags
from LoadDBs import loadDBs
from restart import restart_program
import GravaDados
import logging
 
# initialize the log settings
logging.basicConfig(format='%(asctime)s - %(levelname)s:%(message)s', datefmt='%d/%m/%Y %H:%M:%S',filename = 'historian.log', level = logging.INFO)

# Configuracao do PLC
ipSiemens = '192.168.1.1'
clock = 1

def conection(ipSiemens):
    if not plc.get_connected() :
        try:
            print "Conectando ao PLC Siemens..."
            plc.connect(ipSiemens, 0, 2) # connect to PLC            
            msg1 = "Conectado ao PLC Siemens, IP:" + ipSiemens
            print msg1
            return True
        except Exception as e:
            print(e)
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

        GravaDados.grava_tag(tags)
        
        return True
    except Exception as e:
        print(e)
        restart_program()

if __name__ == "__main__":
    tags = loadTags()
    dbs = loadDBs()
    plc = client.Client()
    mincount = 0
    heartbit = 0

    while True:
        if conection(ipSiemens) :
            try:
                read_tags()                
                time.sleep(clock)
                heartbit += 1
                if heartbit > 60:
                    mincount += 1
                    print "checkpoint de funcionamento minuto " + str(mincount)
                    heartbit = 0
                erro = 0
            except:
                restart_program()
        else:
            print "Erro em alguma lib"
            restart_program()
