class main:
    def __init__(self):
        self.condition = 'A'

    def rig(self):
        if self.condition == 'A':
            self.condition = 'B'
            return 0
        elif self.condition == 'C':
            self.condition = 'D'
            return 3
        elif self.condition == 'E':
            self.condition = 'G'
            return 6
        else:
            raise KeyError

    def stand(self):
        if self.condition == 'B':
            self.condition = 'C'
            return 1
        elif self.condition == 'E':
            self.condition = 'F'
            return 5
        elif self.condition == 'F':
            self.condition = 'G'
            return 7
        else:
            raise KeyError

    def clone(self):
        if self.condition == 'B':
            self.condition = 'E'
            return 2
        elif self.condition == 'D':
            self.condition = 'E'
            return 4
        elif self.condition == 'F':
            self.condition = 'D'
            return 8
        elif self.condition == 'G':
            self.condition = 'B'
            return 9
        else:
            raise KeyError


o = main()
o.rig() # 0
o.clone() # 2
o.stand() # 5
o.clone() # 8
o.stand() # KeyError
o.clone() # 4
o.stand() # 5
o.rig() # KeyError
o.stand() # 7
o.clone() # 9
o.rig() # KeyError
o.stand() # 1
o.rig() # 3
o.clone() # 4
o.rig() # 6
o.clone() # 9