from snap7 import util

class Tag(object):
    def __init__(self, tag_id_, db_, address_, type_var_, table_, bit_ = None):
        self.db = db_
        self.valor = None
        self.valor_anterior = None
        self.address = address_
        self.type_var = type_var_
        self.table = table_
        self.tag_id = tag_id_
        self.bit = bit_
    
    def __repr__(self):
        return str(self.tag_id) +" "+ str(self.address)

    def set_value(self, byte):
        self.valor_anterior = self.valor
        if self.type_var == "R":
            self.valor = util.get_real(byte, self.address)
        if self.type_var == "I" or self.type_var == "W":
            self.valor = util.get_int(byte, self.address)
        if self.type_var == "DW" or self.type_var == "DI":
            self.valor = int(util.get_dword(byte, self.address))
            # print str(self.db )+"."+str(self.address )+" DI: "+ str(self.valor)
        if self.type_var == "B":
            #print self.address
            value_t = util.get_bool(byte, int(self.address), int(self.bit))
            if value_t:
                self.valor = 1
            else:
                self.valor = 0
            
    def get_valor(self):
        return self.valor
