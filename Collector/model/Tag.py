from snap7 import util

class Tag(object):
    def __init__(self, db_, address_, tagname_, description_, type_var_, measur_, bit_ = None):
        self.tagname = tagname_
        self.description = description_
        self.measur = measur_
        self.write = True
        self.db = db_
        self.valor = 0
        self.valor_anterior = 0
        self.address = address_
        self.bit = bit_
        self.type_var = type_var_
    
    def __repr__(self):
        return str(self.tagname) +" "+ str(self.address)

    def set_value(self, byte):
        self.valor_anterior = self.valor
        if self.type_var == "R":
            self.valor = round(util.get_real(byte, self.address),2)
        elif self.type_var == "I" or self.type_var == "W":
            self.valor = round(util.get_int(byte, self.address),2)
        elif self.type_var == "DW" or self.type_var == "DI":
            self.valor = round(util.get_dword(byte, self.address),2)
        elif self.type_var == "B":
            self.valor = util.get_bool(byte, self.address, self.bit)
        if self.valor_anterior != self.valor:
            self.write = True
        else:
            self.write = False
            
    def get_valor(self):
        return self.valor
