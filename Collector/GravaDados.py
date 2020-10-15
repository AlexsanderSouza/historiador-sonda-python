#monte tudo relativo ao influx a partir daqui, pegue outros atributos do grupo
#como a measurement por exemplo
from influxdb import InfluxDBClient
import datetime
import threading
import logging
from restart import restart_program 

# Configuracao Influx
ip_influxdb ="192.168.0.200"
port_influxdb = 8086
user_influx ="XXXX"
password_influx = "YYYY"
bd_influx ="rosneft"


try:
    clientInflux = InfluxDBClient(ip_influxdb, port_influxdb, user_influx, password_influx, bd_influx)
except :
    print "Erro ao canectar-se com o influxdb"

def grava_dados(group,force):
    datetime_aux = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    gravou = False
    for ms in group.measur_list:
        obj = {}
        if ms.changed or force:
            for tag in ms.taglist:
                obj[tag.tagname] = tag.get_valor()

            json_data = [
                    {
                        "measurement": ms.name,
                        "time": datetime_aux,
                        "fields": obj
                    }
                ]
            try:
                clientInflux.write_points(json_data)
                ms.changed = False
                print "Gravou: "+str(ms.name)
                gravou = True
            except Exception as e:
                print "Erro ao gravar grupo: " + str(ms.name) + " " + str(e)
                restart_program()
                logging.error(str(e))
    return gravou

# def grava_dados_th(taglist,meas):
#     """
#     db          objeto com dados
#     db_name     nome do banco
#     start       primeira variavel do obj db
#     """
#     t = threading.Thread(target=grava_dados,args=([taglist],meas))
#     # t.setName = db_name
#     t.start()

# def grava_dados_th(taglist,meas):
#     """
#     db          objeto com dados
#     db_name     nome do banco
#     start       primeira variavel do obj db
#     """
#     t = threading.Thread(target=grava_dados,args=([taglist],meas))
#     # t.setName = db_name
#     t.start()