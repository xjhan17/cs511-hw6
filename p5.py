from z3 import *

ina0, inb0, outa0, outb0

phia = And((outa0=ina0),(outa1=outa0*ina0), (outa2=outa1*ina0))
phib = (outb0 = (inb0*inb0)*inb0)

# p -> q equiv \neg q \or q
phi = Or(Or(Not(ina0=inb0), Not(phia), Not(phib)), (outa2=outb0))



s = Solver()
s.add(Not(phi))

print(s.check())