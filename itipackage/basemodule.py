

def validatestr(mystr):
    if isinstance(mystr, str):
        mystr = mystr.strip()
        return mystr

    return False