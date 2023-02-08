class Phone:
    color = ""
    camera = 0
    sim_Slot = 0
    name=""
    price=0

    def __init__(self):
        pass

    def __init__(self, color,camera,sim_slot,name,price):
        self.color=color
        self.camera=camera
        self.sim_Slot=sim_slot
        self.name=name
        self.price=price

    def __str__(self):
        return 'phone name : '+self.name+' phone camera : '+str(self.camera)

    def calls(self):
        print("Speaking with friend")
        pass

    def message(self):
        print("messaging a friend")
        pass

    def photography(self):
        print(self.camera)
        print("photo can be taken through camera")
        pass

