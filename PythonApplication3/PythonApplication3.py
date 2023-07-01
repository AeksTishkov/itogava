import requests

def isDitto():
    res= requests.get("https://pokeapi.co/api/v2/pokemon/ditto")
    return "ditto".encode() in  res.content

def isPoison():
    res= requests.get("https://pokeapi.co/api/v2/pokemon/poison")
    return "poison".encode() in  res.content

def isGrass():
    res= requests.get("https://pokeapi.co/api/v2/pokemon/grass")
    return "grass".encode() in  res.content

def isFire():
    res= requests.get("https://pokeapi.co/api/v2/pokemon/dittohttps://pokeapi.co/api/v2/pokemon/fire")
    return "fire".encode() in  res.content

def isBug():
    res= requests.get("https://pokeapi.co/api/v2/pokemon/bug")
    return "bug".encode() in  res.content



print("Is Ditto?", isDitto())
print("Is Poison?", isPoison())
print("Is Grass?", isGrass())
print("Is Fire?", isFire())
print("Is Bug?", isBug())