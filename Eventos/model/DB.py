from snap7 import util

class DB(object):

    def __init__(self, db_number_, db_start_, db_size_):
        self.db_number = db_number_
        self.db_size = db_size_
        self.db_start = db_start_
        self.data = None
    
    def get_values(self, plc):
        area = 0x84    # area for DB memory
        self.data = plc.read_area(area,self.db_number,self.db_start,self.db_size)        
