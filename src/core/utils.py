from hashlib import sha256

def space_between(input:str, nbr:int) -> str:
    res = ""

    for i in range(len(input)):
        if i % (nbr) == 0:
            res += ' '

        res += input[i]

    return res

def crypt(text:str) -> str:
    h = sha256()
    h.update(text.encode())

    return h.hexdigest()