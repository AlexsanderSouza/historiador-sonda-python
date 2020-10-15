from snap7 import util

class MS(object):

    def __init__(self, name_, grupo_time_):
        self.name = name_
        self.grupo_time = grupo_time_
        self.changed = True
        self.taglist = []


    def insert_tag(self, tag):
        self.taglist.append(tag)
