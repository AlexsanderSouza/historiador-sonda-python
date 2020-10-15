#converte o byte lido no PLC para seu respectivo tipo
from model.Tag import Tag
import logging

def loadTags():
    try:
        tags = [
            Tag(57,0, "RT_RPM", "RT velocidade do motor RPM", "R", "G01"),
            Tag(55,0, "Hookload", "Carga no gancho", "R", "G02"),
            Tag(55,4, "STANDPIPE", "Riser pressure", "R", "G03"),
            Tag(55,8, "LEFTCATHEADPRE", "Left cat head pressure", "R", "G03"),
            Tag(57,4, "RTMotorCurrent", "RT corrente do motor A", "R", "G04")
        ]

        return tags
    except Exception as e:
        print e
        logging.error(str(e))



