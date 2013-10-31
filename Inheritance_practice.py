class Triangle(object):
    number_of_sides = 3
    
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
        
    def check_angles(self):
        if self.angle1 + self.angle2 + self.angle3 == 180:
            print "The sum of the angles %d, %d, and %d is equal to 180 degrees." % (self.angle1, self.angle2, self.angle3)
            return True
        else:
            print "Your angles do not form a triangle."
            return False
            
class Equilateral(Triangle):
    angle = 60
    def __init__(self):
        self.angle1 = self.angle
        self.angle2 = self.angle
        self.angle3 = self.angle
            
my_triangle = Equilateral()
print "The number of sides is", my_triangle.number_of_sides
print my_triangle.check_angles()