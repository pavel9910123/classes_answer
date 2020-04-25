class Things:
    pass

#creating a derived class (from base class)
class Inanimate(Things):
    pass

class Animate(Things):
    # example of a class function
    def exist(self):
        print('Cogito ergo sum')

class Sidewalks(Inanimate):
    pass

class Animals(Animate):
    # TODO - create three functions for this class: move(), eat(), breathe()
    def duhanie(self):
        print('duschat')
    def dwigat(self):
        print('dwigat')
    def est(self):
        print('est')

    
class Mammals(Animals):
    # TODO - create one function for this class: feed_baby_with_milk()
    def kormit_molokom(self):
        print('kormit molokom')
    

class Giraffes(Mammals):
    # TODO - create one function for this class: eat_leaves_from_trees()
    def ediat_listia(self):
        print('est listia')
giraff=Giraffes()
giraff.ediat_listia()
swer=Animals()
swer.duhanie()
swer.dwigat()
swer.est()
korowa=Mammals()
korowa.kormit_molokom()
