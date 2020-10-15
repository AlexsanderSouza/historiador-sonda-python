#converte o byte lido no PLC para seu respectivo tipo
from model.Measur import MS
import logging

def loadMeasur(tags):
    try:
        mss = {}
        mss['G01'] = MS("G01",5)
        mss['G02'] = MS("G02",5)
        mss['G03'] = MS("G03",10)
        mss['G04'] = MS("G04",10)

        for ms in mss.values():
            for tag in tags:
                if tag.measur == ms.name:                  
                    ms.insert_tag(tag)
        return mss
    except Exception as e:
        print e
        logging.error(str(e))
  
  
