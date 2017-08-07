import aria


class ai(aria.AI):
    def __init__(self):
        super().__init__()
        self.right = False
        self.left = False
        
    # override
    def routine(self):
        # print(self.sm.p2)
        if (self.sm.p2.x < -50 and not self.right):
            self.do(self.walkRight)
            self.right = True
            self.left = False
        elif (self.sm.p2.x > 50 and not self.left):
            self.do(self.walkLeft)
            self.right = False
            self.left = True
            

if __name__ == "__main__":
    x = ai()
    x.run()
    
