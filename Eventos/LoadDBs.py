#converte o byte lido no PLC para seu respectivo tipo
from model.DB import DB
from restart import restart_program
import logging

def loadDBs():
    try:
        dbs = {}
        dbs['50'] = DB(50,0,42)
        dbs['51'] = DB(51,0,48)
        dbs['61'] = DB(61,0,72)
        dbs['90'] = DB(90,0,82)
        
        return dbs
    except Exception as e:
        print e
        logging.error(str(e))
        restart_program()
  
  
