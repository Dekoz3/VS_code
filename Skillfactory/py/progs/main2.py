
from sys import path
path.append('C:\\Users\\Denis.kozarenko\\VS_code\\VS_code\\Skillfactory\\py\\packages\\extrapack.zip')

# import extra.good.best.sigma as sig
# import extra.good.alpha as alp

# print(sig.FunS())
# print(alp.FunA())

from sys import path

# path.append('..\\packages\\extrapack.zip')

import extra.good.best.sigma as sig
import extra.good.alpha as alp
from extra.iota import FunI
from extra.good.beta import FunB

print(sig.FunS())
print(alp.FunA())
print(FunI())
print(FunB())