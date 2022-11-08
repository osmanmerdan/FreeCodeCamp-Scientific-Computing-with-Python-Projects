import copy
import random

class Hat:
    # kwargs allow us to pass a variable number of keyword argument
    def __init__(self, **kwargs):
      #Below code will fill self.contents of an hat object.
        self.contents=[]
        for k,v in kwargs.items():
            for i in range(v):
                self.contents.append(str(k))
    def draw(self, num_to_draw):
      #Below code will restrict the number of balls we can take out
        num_to_draw=min(num_to_draw, len(self.contents))
        returned_balls=[]
      #Drawing random balls 
        for n in range(num_to_draw):
          #Choosing a random integer from a sample which conteins all the indexes of self.contents
            p=random.randint(0,len(self.contents)-1)
          #Using that intefer value we can select a random ball.
            returned_balls.append(self.contents[p])
          #Removing that ball from self.contents
            self.contents.remove(self.contents[p])
        return(returned_balls)
            

#Experiment function 

def experiment(hat,expected_balls,num_balls_drawn,num_experiments):
  #M is the total number of success 
    M=0
    for n in range(num_experiments):
      #Population is where we draw our balls from
      #Deep.copy will ensure that hat object does not effected from the process of drawing because overall we will alter the hat.contents list every time we draw a ball. 
        population=copy.deepcopy(hat)
        #Sample is the balls we choose 
        sample=population.draw(num_balls_drawn)
        # We will ad 1 to x every time we obtain equal or more number of balls for each key value in expected balls dictionary.
        x=0
        for k in expected_balls:
            if expected_balls[k]<=sample.count(k):
                x+=1
              
        if x==len(expected_balls):
            M+=1
    
    return(M/num_experiments)

        


        