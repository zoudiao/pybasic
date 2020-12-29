#declared
f=0
#print(f)

#re-decalaring
#f="abc"
#print(f)

# error : variable of different types can't be combined
# print("this is a string" + 123)
print("this is a string"+str(123))


# global vs. local variables in functions
def somefunction():
    global f
    f="def"
    print(f)


somefunction()
print(f)