
from math import *

digits = raw_input('Enter number of digits to round PI to: ')
print ('{0:.%df}' % min(1000, int(digits))).format(4 * (4 * atan(1.0/5.0) - atan(1.0/239.0)))
