import psycopg2
from config import config
import logging
from restart import restart_program

conn = None

def grava_tag(tags):

    """ Connect to the PostgreSQL database server """
    global conn
    global cur
    if conn is None:
        try:
            # read connection parameters
            params = config()
     
            # connect to the PostgreSQL server
            print('Connecting to the PostgreSQL database...')
            conn = psycopg2.connect(**params)

            # create a cursor
            cur = conn.cursor()

            # execute a statement
            print('PostgreSQL database version:')
            for tag in tags:
                if tag.valor_anterior != tag.valor:
                    cur.execute("INSERT INTO " + str(tag.table) + " VALUES (NOW(), " + str(tag.tag_id) + ", '" + str(tag.valor) + "');")
                        
            conn.commit()
            # close the communication with the PostgreSQL
            # cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            logging.error(str(error))
            restart_program()
    else:
        try:
            for tag in tags:
                if tag.valor_anterior != tag.valor:
                    cur.execute("INSERT INTO " + str(tag.table) + " VALUES (NOW(), " + str(tag.tag_id) + ", '" + str(tag.valor) + "');")
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            logging.error(str(error))
            restart_program()
