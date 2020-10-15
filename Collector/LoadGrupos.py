from model.Group import Group
import logging

def loadGrupos(measurs):
    try:
        grupos = {}
        grupos['5'] = Group(5,30)
        grupos['10'] = Group(10,50)

        for grupo in grupos.values():
            for measur in measurs.values():
                if measur.grupo_time == grupo.time_interval:                  
                    grupo.insert_measur(measur)
        return grupos
    except Exception as e:
        print e
        logging.error(str(e))

def check_group_time(grupos):
    #For nao funciona mas deveria, depois verificar
    #for grupo in grupos:
    #    grupo.set_time()
    grupos['5'].set_time()
    grupos['10'].set_time()
    
