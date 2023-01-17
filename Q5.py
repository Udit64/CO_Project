from math import log2

size=input('Memory size in MegaBytes or Megabits -')   #memory size
if size[-1]=='b':
    size=int(size[:-2])*(2**20)
else:
    size=int(size[:-2])*(2**23)
p=int(log2(size))

m=input('Memory is adressed as - ').lower()  # memory_adressed as
if m=='bit':
    m=1
elif m=='nibble':
    m=4
elif m=='byte':
    m=8
else:
    m=32
# first type
li=int (input('Length of one instruction in bits - '))
lr=int(input('Length of register in bits'))
print(f'Minimum bits needed to represent an address in this architecture - {p}')
o=li-lr-p
print(f'Number of bits needed by opcode - {o}')
f=li-o-lr-lr
print(f'Number of filler bits in Instruction type 2 - {f}')
print(f'Max instructions- {2**o}') # max instructions
print(f'Maximum number of registers- {2**lr}')


#second type Type-1
cpubits=int (input('Input how many bits the cpu is- '))
if (m==32):
    m=cpubits

newb=input('Input how you would want to change the current addressable memory- ').lower()
if newb=='bit':
    newb=1
elif newb=='nibble':
    newb=4
elif newb=='byte':
    newb=8
else:
    newb=cpubits
print(int(log2(m/newb)))

# Type-2
cpubits=int(input('How many bits the cpu is- '))
addresspins=int(input('How many address pins cpu has- '))
m=input('Type of addressable memory it has- ').lower()  # memory_adressed as
if m=='bit':
    m=1
elif m=='nibble':
    m=4
elif m=='byte':
    m=8
else:
    m=cpubits
print(int((2**addresspins*m)/8),'B or', int((2**addresspins*m)/(2**33)),'GB')