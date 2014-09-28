inp = raw_input('enter RSPLS')
if inp == 'rock':
    print 'Player chooses' , inp
    inp = 0
elif inp == 'spack':
    print 'Player chooses' , inp
    inp = 1    
elif inp=='paper':
    print 'Player chooses' , inp
    inp = 2
elif inp == 'lizard':
    print 'Player chooses' , inp
    inp = 3
elif inp == 'scissors':
    print 'Player chooses' , inp
    inp = 4
else:
    print 'invalid input' 
    

import random

comp = random.randrange(0,5)
if comp == 0:
    comp = 'rock'
    print 'computer chooses' , comp
elif comp == 1:
    comp='spack'    
    print 'computer chooses' , comp	
elif comp == 2:
    comp = 'paper'
    print 'computer chooses' , comp
elif comp == 3:
    comp='lizard'
    print 'computer chooses' , comp
elif comp == 4:
    comp = 'scissors'
    print 'computer chooses' , comp
else:
    print 'invalid computer chooses' 
    
comp=random.randrange(0,5)
    

if (inp - comp) % 5 >= 3 :
    print 'computer wins'
elif (inp - comp) % 5 == 0 :
    print 'tied'
else : 
    print 'player wins' 
    



