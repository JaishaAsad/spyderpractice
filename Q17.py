print (' PRINT BINARY TO DECIMAL CONVERSION')
print("Enter 'x' for exit")
binary = input("Enter number in Binary Format: ")
if binary == 'x':
    exit()
else:
    decimal = int(binary, 2)
    print(binary,"in Decimal =",decimal)