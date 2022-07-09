# solutuon 1

def cakes(recipe, available):
    try:
        return min([available[a]/recipe[a] for a in recipe])
    except:
        return 0


# solutuon 2

def cakes(recipe, available):

    return min([available[i]//recipe[i] if i in available else 0 for i in recipe])
