import sys
import os
import logging
# Funcao para reiniciar programa
def restart_program():
    print "Reiniciando"
    logging.info("Programa reiniciado")
    python = sys.executable
    os.execl(python, python, * sys.argv)