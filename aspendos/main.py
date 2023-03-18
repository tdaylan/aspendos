import numpy as np

def retr_mcut(gdat, defs, asca, acut, adishost, mdencrit):
    
    mscl = defs * np.pi * adishost**2 * mdencrit * asca
    fracacutasca = acut / asca
    mcut = mscl * retr_mcutfrommscl(fracacutasca)
    
    return mcut


def retr_mcutfrommscl(fracacutasca):
    
    mcut = fracacutasca**2 / (fracacutasca**2 + 1.)**2 * ((fracacutasca**2 - 1.) * np.log(fracacutasca) + fracacutasca * np.pi - (fracacutasca**2 + 1.))

    return mcut



