#!/usr/bin/python3
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thislist = ["a", "1", "2", "b"]
thisstring = "bfjskbflsdanf123728"
thisstring2 = "1F 2B 3D"


# list iterration
for i in thislist:
    print(i)
# list iterration from string
for i in range(len(thisstring)):
    print(thisstring[i])
# dict iterration
for key, value in thisdict.items():
    print(key)
    print(value)
# split space separated string to list
splittolist = thisstring2.split()
print(splittolist)
# put space separated string to dict
splittodict = {}
for i in range(len(thisstring2)-1):
    j = i +1
    if thisstring2[i].isspace() or  thisstring2[j].isspace():
        pass
    else:
        splittodict[thisstring2[i]] = thisstring2[j]
print(splittodict)
