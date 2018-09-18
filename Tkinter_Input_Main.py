from tkinter import *
from tkinter.ttk import Style
from tkinter.font import Font,nametofont
from threading import Thread
from time import sleep


global root,canvas,my,done,name
done = False
name = str()

def drawUI():
    global root,canvas,my,nameBox
    canvas = Canvas(root)
    canvas.grid()
    
    title = Label(canvas,text="Personality Guesser",font=("Futura",18,"bold"))
    title.grid(row=0,column=4)

    nameLab = Label(canvas,text="Name:")
    nameBox = Text(canvas,height=1,width=10)
    nameLab.grid(row=1,column=1)
    nameBox.grid(row=1,column=2)
    
    sub1 = Label(canvas,text="Reactions Given",font=("Futura",16,"bold"))
    sub1.grid(row=2,column=4)
    givLov = Button(canvas,text="Love",command=lambda: my.addLov(True))
    givLau = Button(canvas,text="Laughter",command=lambda: my.addLau(True))
    givWow = Button(canvas,text="Wow",command=lambda: my.addWow(True))
    givSad = Button(canvas,text="Sad",command=lambda: my.addSad(True))
    givAng = Button(canvas,text="Angry",command=lambda: my.addAng(True))
    givUpv = Button(canvas,text="Upvote",command=lambda: my.addUpv(True))
    givDow = Button(canvas,text="Downvote",command=lambda: my.addDow(True))
    givLov.grid(row=3,column=1)
    givLau.grid(row=3,column=2)
    givWow.grid(row=3,column=3)
    givSad.grid(row=3,column=4)
    givAng.grid(row=3,column=5)
    givUpv.grid(row=3,column=6)
    givDow.grid(row=3,column=7)
    
    sub1 = Label(canvas,text="Reactions Gotten",font=("Futura",16,"bold"))
    sub1.grid(row=4,column=4)
    getLov = Button(canvas,text="Love",command=lambda: my.addLov(False))
    getLau = Button(canvas,text="Laughter",command=lambda: my.addLau(False))
    getWow = Button(canvas,text="Wow",command=lambda: my.addWow(False))
    getSad = Button(canvas,text="Sad",command=lambda: my.addSad(False))
    getAng = Button(canvas,text="Angry",command=lambda: my.addAng(False))
    getUpv = Button(canvas,text="Upvote",command=lambda: my.addUpv(False))
    getDow = Button(canvas,text="Downvote",command=lambda: my.addDow(False))
    getLov.grid(row=5,column=1)
    getLau.grid(row=5,column=2)
    getWow.grid(row=5,column=3)
    getSad.grid(row=5,column=4)
    getAng.grid(row=5,column=5)
    getUpv.grid(row=5,column=6)
    getDow.grid(row=5,column=7)

    submit = Button(canvas,text="Submit",command=lambda: guess())
    submit.grid(row=7,column=4)
    
    

def guess():
    global my,nameBox,name,done
    name = nameBox.get("1.0",END)[:-1]
    file = open(str("Personality_"+str(name)+".txt"),"w+")
    file.close()
    print(str("Personality of "+str(name)+":"))
    my.stats()
    print("")
    my.personality()
    done = True


def main():
    global root,canvas,my,done

    drawUI()

    while not done:
        sleep(1)

    root.destroy()

    return None
    

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

def print(text="",end="\n"):
    global name
    file = open(str("Personality_"+str(name)+".txt"),"a")
    file.write(str(str(text)+str(end)))
    file.close()

       
class person():
    def __init__(self):
        self.r = [0,0,0,0,0,0,0]
        self.g = [0,0,0,0,0,0,0]
        
    def addLov(self,given=False):
        if given:
            self.g[0] += 1
        else:
            self.r[0] += 1
    def addLau(self,given=False):
        if given:
            self.g[1] += 1
        else:
            self.r[1] += 1
    def addWow(self,given=False):
        if given:
            self.g[2] += 1
        else:
            self.r[2] += 1
    def addSad(self,given=False):
        if given:
            self.g[3] += 1
        else:
            self.r[3] += 1
    def addAng(self,given=False):
        if given:
            self.g[4] += 1
        else:
            self.r[4] += 1
    def addUpv(self,given=False):
        if given:
            self.g[5] += 1
        else:
            self.r[5] += 1
    def addDow(self,given=False):
        if given:
            self.g[6] += 1
        else:
            self.r[6] += 1
    
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
        print(str("Openness: "+str(self.ocean[0])))
        print(str("Conscientiousness: "+str(self.ocean[1])))
        print(str("Extraversion: "+str(self.ocean[2])))
        print(str("Agreeableness: "+str(self.ocean[3])))
        print(str("Neuroticism: "+str(self.ocean[4])))
        mbtype = ""
        mbtype += mbti(self.ocean[2],"E","I")
        mbtype += mbti(self.ocean[0],"N","S")
        mbtype += mbti(self.ocean[3],"F","T")
        mbtype += mbti(self.ocean[1],"J","P")
        print(str("MBTI: "+mbtype))      
        
my = person()    



root = Tk()
root.title("Personality Guesser")
root.geometry("690x200")
style = Style()
style.theme_use("default")
defaultfont = nametofont("TkDefaultFont")
defaultfont.configure(size=16,family="Futura")
t = Thread(target=main)
t.start()
root.mainloop()


