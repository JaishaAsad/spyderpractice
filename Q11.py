print ('EUCLIDEAN DISTANCE')
import math

x1 =int( input ('please provide value of x1 = '))
x2 =int( input ('please provide value of x2 = '))
y1 =int( input ('please provide value of x3 = '))
y2 =int( input ('please provide value of x4 = '))

distance_formula= math.sqrt(((x2-x1)**2) +((y2-y1)**2))

print ('THE DISTANCE BETWEEN TWO GIVEN POINTS'+ str(x1)+','+str(y1) + 'and' + str(x2)+','+str(y2) +'is'+str(distance_formula))