# strings and outputs
msg = "Hello World"
print(msg)

#Lists
pets = ["dog","cat","fish"]
thepet = pets[1]
print(thepet)

#Lenght and types
size = len(pets)
msg = "there are "+ str(size) + " pets"
print(msg)

#loops
for anml in pets:
    print("I wish I had a",anml)

#User input
ans = input("What kind of Animals do you have?")
print("you have a " + ans)

#Booleans
known = ans in pets
print("It is "+str(known)+" that I have seen a "+ans)

#Branching
if known:
    msg = "My friend has a "+ans
else:
    msg = "I don't know anyone with a "+ans
print(msg)

#dictionarys
feels = {"cat":"selfish","dog":"Loyal","fish":"wet"}

if known:
    pre = "e" if ans == "fish" else ""
    msg = ans + pre+"s are very "+ feels.get(ans)
else:
    msg = "I don't know anyone with a "+ans
    
print(msg)