import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())


txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())


#Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")
