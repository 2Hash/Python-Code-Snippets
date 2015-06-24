#Author:  Eos
#Admin:   @StreamersHub.net
#Github:  https://github.com/Eos11

import uuid
import random
from random import randint

import random
def uniqueid():
    seed = random.getrandbits(30)
    while True:
       yield seed
       seed += randint(131,919391)
       
unique_sequence = uniqueid()

print("Eos's UniqueID Generator @Streamershub.net")

amount = int(input("Enter amount to generate: "))


for loopme in range( 0, amount ):
     id2 = next(unique_sequence)
     print( id2 )
print("Generated...", amount," UniqueID'S")
