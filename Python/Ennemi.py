from random import randint

class Ennemi :
    def __init__(self,type,pv,degats,loot,exp,gold_min=0,gold_max=0,niv=1):
        self.type=type
        self.pv=pv
        self.pv_base=pv/niv
        self.pv_a_restituer=self.pv
        self.degats=degats
        self.degats_base=degats/niv
        self.lv=niv
        self.loot=loot
        self.gold_lachées=randint(gold_min,gold_max)
        self.exp=exp
        self.exp_base=exp
