import re 

result =re.search(r"aza", "plaza")
print(result)

result = re.search(r"aza", "bazaar")
print(result)

result = re.search(r"aza", "xenom")
print(result)

print(re.search(r"p.ng", "penguin"))
print(re.search(r"p.ng", "Penguin", re.IGNORECASE))


