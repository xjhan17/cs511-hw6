from z3 import *

file = open('./input.txt', 'r')
lines = file.readlines()
ina = int(lines[0])
m = int(lines[1])
inb = int(lines[2])
n = int(lines[3])

def power(ina, m):
	outa = ina
	for i in range(m):
		outa = outa * ina
		# print('outa = ',outa) - for testing purposes

	return outa

def power_new(inb, n):
	outb = inb
	for i in range(n):
		outb = outb * outb
		# print('outb = ',outb) - for testing purposes
	return outb

def testEquiv(ina, m, inb, n):
	s = Solver()
	test = power(ina, m)
	test2 = power_new(inb, n)
	boolValue = Bool('equiv')
	if test != test2:
		boolValue = False
	s.add(boolValue)
	if s.check() == sat:
		print('true')
	else:
		print('false')

	

def main():
	testEquiv(ina, m, inb, n) 


if __name__== "__main__":
    main()