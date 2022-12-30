ex = "dabAcCaCBAcCcaDA"

for i in range(len(ex)-1):
    if ex[i].isupper and ex[i].lower() == ex[i+1]:
        string = ex.replace(ex[i:i+3], "")
        print(string)
    elif ex[i].islower and ex[i].upper() == ex[i+1]:
        string = ex.replace(ex[i:i+3], "")
        print(string)