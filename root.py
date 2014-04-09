from __future__ import division
from decimal import Decimal, getcontext
 
def calculate(wexp, radi, acc=50):
    getcontext().prec = acc
    y = 2
    wexp = Decimal(str(wexp))
    radi = Decimal(str(radi))
    while True:
        old_y = y
        y = ((wexp - 1) * y**wexp + radi) / (wexp * y**(wexp-1))
        if old_y == y:
            break
    return y
 
def calculate_newton(radi, acc=50):
    getcontext().prec = acc
    y = 2
    einhalb = Decimal('0.5')
    radi = Decimal(str(radi))
    while True:
        old_y = y
        y = einhalb * (y + (radi/y))
        if old_y == y:
            break
    return y
 
if __name__ == '__main__':
    print calculate(2, 2, 10)
    print calculate_newton(2)