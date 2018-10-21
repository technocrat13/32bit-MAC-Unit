a = int(input("Enter the first binary number: "))
b = int(input("Enter the second binary number: "))
e = '00000000000000000000000000000000'
A = str(bin(a))[2:]
B = str(bin(b))[2:]
print("A in binary: " + e[:-len(A)] + A)
print("B in binary: " + e[:-len(B)] + B)

c = a*b
print("Decimal multiplication will result in: " + str(c))

cbin = input("What is the binary output: ")
cdec = int(cbin, 2)
print("Output from the MAC unit is: " + str(cdec))