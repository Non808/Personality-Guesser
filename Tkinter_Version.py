from tkinter import *

def percentage(st):
    total = 0
    for i in st:
        total += i
    perc = []
    try:
        for i in range(7):
            perc.append(round(st[i]/total*100,1))
    except:
        for i in range(7):
            perc.append(round(100/7,1))
    return perc

def mbti(traitScore,l1,l2):
    if traitScore > 1:
        return l1
    elif traitScore < -1:
        return l2
    else:
        return "x"
        
class person():
    def __init__(self):
        self.r = [0,0,0,0,0,0,0]
        self.g = [0,0,0,0,0,0,0]
    def stats(self):
        rPerc = percentage(self.r)
        gPerc = percentage(self.g)
        print("\nReceiving")
        for i in range(7):
            print(str(i+1)+". "+str(rPerc[i])+"%")
        print("\nGiving")
        for i in range(7):
            print(str(i+1)+". "+str(gPerc[i])+"%")
        print()
    def personalysis(self,rgp,traits):
        if rgp > 50:
            points = 3
        elif rgp > 30:
            points = 2
        elif rgp > 20:
            points = 1
        elif rgp < 10:
            points = -1
        elif rgp < 7:
            points = -2
        elif rgp < 3:
            points = -3
        else:
            points = 0
        for i in range(5):
            self.ocean[i] += traits[i]*points
    def personality(self):
        self.ocean = [0,0,0,0,0]
        rp = percentage(self.r)
        gp = percentage(self.g)
        self.personalysis(rp[0],[0,0,1,0,-1])
        self.personalysis(gp[0],[0,0,0,1,0])
        self.personalysis(rp[1],[0,-1,0,0,0])
        self.personalysis(gp[1],[0,-1,1,0,0])
        self.personalysis(rp[2],[1,0,-1,0,0])
        self.personalysis(gp[2],[1,0,0,0,0])
        self.personalysis(rp[3],[0,0,-1,0,1])
        self.personalysis(gp[3],[0,0,0,1,1])
        self.personalysis(rp[4],[0,0,1,-1,0])
        self.personalysis(gp[4],[0,1,1,-1,1])
        self.personalysis(rp[5],[1,0,0,0,0])
        self.personalysis(gp[5],[0,0,0,1,0])
        self.personalysis(rp[6],[0,0,0,-1,0])
        self.personalysis(rp[6],[-1,0,0,-1,0])
        print("Openness:",self.ocean[0])
        print("Conscientiousness:",self.ocean[1])
        print("Extraversion:",self.ocean[2])
        print("Agreeableness:",self.ocean[3])
        print("Neuroticism:",self.ocean[4])
        mbtype = ""
        mbtype += mbti(self.ocean[2],"E","I")
        mbtype += mbti(self.ocean[0],"N","S")
        mbtype += mbti(self.ocean[3],"F","T")
        mbtype += mbti(self.ocean[1],"J","P")
        print("MBTI: "+mbtype)      
        
my = person()    
