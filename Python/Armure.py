class Armure:
    def __init__(self,name,protection,niv=1):
        self.name=name
        self.lv=niv
        self.protection=protection*niv
        self.type="Armure"


