class Bear:
    __age = 0 # it does not work inside the library
    
    height = 0
    
bear_one = Bear()
# bear_one.__age = 3 # it will work inside-outside class library
bear_one.height = 9
print(f'Age of bear_one : {bear_one.__age} and height: {bear_one.height}')

# Age of bear_one : 3 and height: 9

# AttributeError: 'Bear' object has no attribute '__age'