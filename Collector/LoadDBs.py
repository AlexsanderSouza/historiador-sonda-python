#converte o byte lido no PLC para seu respectivo tipo
from model.DB import DB
import logging

def loadDBs():
    try:
        dbs = {}
        dbs['57'] = DB(57,0,72)
        dbs['55'] = DB(55,0,72)
        return dbs
    except Exception as e:
        print e
        logging.error(str(e))
  
  
