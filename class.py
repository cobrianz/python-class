class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        def move(self):
            print('moving')
        
        
        def draw(self):
            print('drawing')
        
        
point = Point(20, 30)
point.x = 40
print(point.x, point.y)