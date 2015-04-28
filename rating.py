#!/usr/bin/env python
rating = int(input('Please rate us\n'))
if rating == 0:
    print ('What!?  I give YOU a', rating, 'rating')
elif rating  == 1:
    print ('give some feedback about the shitty', rating, 'rating' )
elif rating == 2:
    print ('no likey? Why the low', rating, 'rating')
elif rating == 3:
    print('You kinda liked it huh?  How can we beat the', rating, 'rating?')
elif rating == 4:
    print('That good?  How can we get even better than a', rating, '?')
else:
    print('Thanks for the great', rating, 'rating!' )

print ('Thank\'s for rating us!')
x = input('press enter to exit')