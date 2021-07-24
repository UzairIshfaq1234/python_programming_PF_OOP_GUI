d2={"harry":"burger",
    "rohan":"fish",
    "skillf":"roti",
    "uzair":{"breakfast": 3,"lunch":"chicken"}, }
print(d2)
print("______")
print(d2["harry"])
print("______")
print(d2["rohan"])
print("______")
print(d2["uzair"])
print("______")
print(d2["uzair"]["lunch"])
print("______")
print(d2["uzair"]["breakfast"])
print("______")
d2["awais"]="fish","egg"
print(d2)
print("______")
del d2["awais"]
print(d2)
print("______")
d3=d2.copy
del d2["harry"]
print(d3)
print(d2)
print("______")
d2.update({"sudais":"'burger' "+"'rice' "+" 'piza'"})
print(d2)
print("______")
print(d2.keys())
print("______")

print(d2.items())