
length_string = input("Write words to count the length of the string")
print(len(length_string))

i = 0

if len(length_string) == 0:
    print("Emty string")
elif i < len(length_string):
    print(length_string[i])
else:
    print("I out of range")

