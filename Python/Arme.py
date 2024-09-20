class Arme:
    def __init__(self,name,degats,protection,emplacement,niv=1):
        self.name=name
        self.lv=niv
        self.degats=degats*niv
        self.protection=protection*niv
        self.type="Arme"
        self.emplacement=emplacement


