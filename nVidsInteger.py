def nVidsInteger(nVidsAux):
    nVids = 0
    if (len(nVidsAux) == 7):
        nVids = int(nVidsAux[:-6])
    elif(len(nVidsAux) > 7):
            nVids = int(nVidsAux[:-7])
    return nVids

def nSubsInteger(nSubsAux):
    nSubs = 0
    if (len(nSubsAux) == 12):
        nSubs = int(nSubsAux[:-11])
    elif(len(nSubsAux) >= 14):
            nSubs = int(nSubsAux[:-12])
    return nSubs    

print(nSubsInteger(''))
print(nSubsInteger('1 suscriptor'))
print(nSubsInteger('2 suscriptores'))
print(nSubsInteger('25869 suscriptores'))