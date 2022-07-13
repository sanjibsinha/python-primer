class Bear:
    age = 0
    _age = age
    height = 0
    
    def __init__(self, age, height):
        self.age = age
        self.height = height
    
bear_one = Bear(3, 9)
print(f'Age of bear_one : {bear_one.age} and height: {bear_one.height}')

# Age of bear_one : 3 and height: 9   

  
