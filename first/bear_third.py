import bear_second as bear

bear_one = bear.Bear()
bear_one.__age = 4
bear_one.height = 9
print(f'Age of bear_one : {bear_one.__age} and height: {bear_one.height}')

# AttributeError: 'Bear' object has no attribute '__age'

# Age of bear_one : 4 and height: 9