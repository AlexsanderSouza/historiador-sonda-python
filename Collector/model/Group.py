import GravaDados
class Group(object):

    def __init__(self, time_interval_,time_max_):
        self.time_interval = time_interval_
        self.time_max = time_max_
        self.time_acc_max = 1
        self.time_cicle = 0
        self.time_acc = 1
        self.measur_list = []
    
    def set_time(self):

        if self.time_acc_max >= self.time_max:
            print 'Max: '+str(self.time_acc_max)
            GravaDados.grava_dados(self,True)
            self.time_acc_max = 1
        else:
            self.time_acc_max += 1

        if self.time_acc >= self.time_interval :
            #A ideia e disparar as threads aqui!
            gravou = GravaDados.grava_dados(self,False)
            if gravou:
                self.time_acc_max = 1
            self.time_acc = 1
        else:
            self.time_acc += 1
        
    def insert_measur(self, tag):
        self.measur_list.append(tag)
