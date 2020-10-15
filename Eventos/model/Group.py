import GravaDados
class Group(object):

    def __init__(self, time_interval_):
        self.time_interval = time_interval_
        self.time_cicle = 0
        self.time_acc = 1
        self.taglist = []
    
    def set_time(self):        
            if self.time_acc >= self.time_interval :
                #A ideia e disparar as threads aqui!
                #print "Gravou com "+ str(self.time_interval)+" segundos!"
                #for tag in self.taglist:
                #    print tag.get_valor()
                # print self.taglist
                GravaDados.grava_dados(self)
                self.time_acc = 1
            else:
                self.time_acc += 1
        # print " write:" + str(self.group_write)
        # print ""
        
    def insert_tag(self, tag):
        self.taglist.append(tag)
