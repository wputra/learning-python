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
thisdict3 = {}
emptylist = []
for i in range(len(thisstring)):
    eli = thisstring[i]
    if eli not in emptylist:
        emptylist.append(eli)
        thisdict3[eli] = thisstring.count(eli)
print(emptylist)
print(thisdict3)
# dict iterration
thisdict2 = {}
for key, value in thisdict.items():
    thisdict2[key] = list(str(value))
print(thisdict2)
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
