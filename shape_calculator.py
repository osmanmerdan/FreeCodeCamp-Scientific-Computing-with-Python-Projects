class Rectangle:
    #Defining attributes
    def __init__(self,width,height):
        self.width=width
        self.height=height
    
    #Creating methods
    #Using them we can easily change width and height of the object
    def set_width(self,width):
        self.width=width
    def set_height(self,height):
        self.height=height
    
    #Area calculator method  
    def get_area(self):
        return(self.width*self.height)
    
    #Calculating perimeter   
    def get_perimeter(self):
        return(self.width*2+self.height*2)
    
    #Getting high-on-potenuse:)
    #It is a joke from Key and peele 
    #Watch it from https://www.youtube.com/watch?v=k1tsGGz-Qw0
    def get_diagonal(self):
        return((self.width ** 2 + self.height ** 2) ** .5)
    
    #method for getting the picture
    def get_picture(self):
        if self.width>50 or self.height>50:
            return('Too big for picture.')
        else:
            pic=(('*' * self.width) + '\n')*self.height
            return(pic)
    #method for amount inside problem 
    def get_amount_inside(self,shape):
        return(int(self.get_area()/shape.get_area()))
    #Definene the __repr__ representation
    #Using  __repr__ will enable us to create beautiful summary
    #When we call print(object)
    def __repr__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

# Inheriting
#Define square instence class Square (Rectangle):
class Square (Rectangle):
 
    def __init__(self,side):
        self.width=side
        self.height=side
    def set_side(self,side):
        self.width=side
        self.height=side
    #Representations
    def __repr__(self):
            return f'Square(side={self.width})'