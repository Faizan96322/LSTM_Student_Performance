# used randint to create the random values for input_data.csv

import random
def randoo():
    # Generate a random value between anynumber to  anynumber
    rand_value = random.randint(65, 100)
    #rand_value = random.randint(0, 1)
    print(rand_value)

for i in range(0,50):
   randoo()