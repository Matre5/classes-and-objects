from pickle import APPEND


class Student:
    # [assignment] Skeleton class. Add your code here
 def __init__(self, name, age, tracks, score):
        #instance variables below
        self.name = str(name)
        self.age = int(age)
        self.tracks = tracks
        self.score = float(score)
        
 print("Info of new students: \n")
 def change_name(self, n_name):
    self.name = n_name
    print("The new name is", self.name)
    
 def change_age(self, n_age):
    self.age = n_age
    print("This is the new age", self.age)
    
 def add_track(self, tracks):
    self.tracks.append(tracks) #the append is to add to an already existing list
    print("This is your new track ", self.tracks)
    
 def get_score(self):
    print("This is your new score", self.score)
    return self.score
    
#Bob is the object of the student class
Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
