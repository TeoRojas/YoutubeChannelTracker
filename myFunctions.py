#!/usr/bin/python
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

def nVidsInteger(nVidsAux):
    nVids = 0
    if (len(nVidsAux) == 7):
        nVids = int(nVidsAux[:-6])
    elif(len(nVidsAux) > 7):
            nVids = int(nVidsAux[:-7].replace('.',''))
    return nVids

def nSubsInteger(nSubsAux):
    nSubs = 0
    if (len(nSubsAux) == 12):
        nSubs = int(nSubsAux[:-11])
    elif(len(nSubsAux) >= 14):
        nSubs = int(nSubsAux[:-13].replace('.',''))
    return nSubs      

class Channel:
    def __init__ (self, name, link, subs, vids):
        self.name = name
        self.link = link
        self.nSubs = subs
        self.nVids = vids

def imprimeHola():
    print('Hola TU, que ase?')

def getNsubsAndNvids(element):
    nSubsAux = element.find_element(By.ID, 'metadata').find_element(By.ID, 'subscribers').text # need to delete the tail 'suscriptores' -13 characters.
    nVidsAux = element.find_element(By.ID, 'metadata').find_element(By.ID, 'video-count').text    
    
    nSubs = nSubsInteger(nSubsAux)
    nVids = nVidsInteger(nVidsAux)

    return nSubs, nVids

def getNsubs(element):
    nSubsAux = element.find_element(By.ID, 'metadata').find_element(By.ID, 'subscribers').text # need to delete the tail 'suscriptores' -13 characters.    
    nSubs = nSubsInteger(nSubsAux)
    return nSubs

def getNvids(element):
    nVidsAux = element.find_element(By.ID, 'metadata').find_element(By.ID, 'video-count').text       
    nVids = nVidsInteger(nVidsAux)
    return nVids

def returnChannel(element): #Return Channel if has subs > minSubs & vids > minVids
    channel = Channel(element.find_element(By.TAG_NAME , 'ytd-channel-name').text,
    '',
    getNsubs(element),
    getNvids(element))

    return channel

def printChannels(channels):
    for c in channels:
        print (c.name)
        print ("Subs: " + str(c.nSubs) + " | " + "Vids: " + str(c.nVids))    
        print ("------------")