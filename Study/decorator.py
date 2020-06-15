# decorater
def decorate_country(f):
    def wrap(*args,**kwargs):
        x = f(*args,**kwargs)
        return '*{}*'.format(x)

    return wrap

@decorate_country
def india():
    return "Delhi"

@decorate_country
def Australia():
    return "Sydney"

print(india())