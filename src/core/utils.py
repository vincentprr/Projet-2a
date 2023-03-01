from hashlib import sha256
from wtforms import widgets, SelectMultipleField

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

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()