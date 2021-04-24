from hashlib import *



class Blockchain():
    def __init__(self):
        self.chain=[]
        self.nutzerListe=[]
        self.genesisBlock()
# type kann nur folgende Werte annehmen: genesis, transaktion
    def newBlock(self, inhalt, type):
        return([inhalt, type])
    def addBlock(self, block=None):
        if block!=None:
            self.chain.append(block)

    def blockAsStr(self, block):
        string = ""
        for a in self.chain[block]:
            if type(a)==list:
                for b in a:
                    string=string+", "+str(b)
            else:
                string=string+", "+str(a)
        string=string[2:]
        return string
# Verschiedene Arten von Blocks
    def genesisBlock(self):
        self.addBlock([0, "genesis", "genesis"])


    def transaktion(self, sender, receiver, betrag):
        inhalt=[sender, receiver, betrag]
        posSender=int(sender[-1])
        posSender-=1
        posReceiver=int(receiver[-1])
        posReceiver-=1
        if int(self.nutzerListe[posSender].balance) >= int(betrag):
            self.nutzerListe[posSender].changeBalance(betrag*-1)
            self.nutzerListe[posReceiver].changeBalance(betrag)
            self.addBlock(self.newBlock(inhalt, "transaktion"))
            self.callListeners()
        else:
            print("ERROR Sender hat zu wenig Geld, um die Transaktion auszuführen.")

# Nutzer hinzufügen
    def addNutzer(self, balance):
        name = "nutzer"+str((len(self.nutzerListe)+1))
        nutzer = Nutzer(name, balance)
        self.nutzerListe.append(nutzer)
        self.appendAllBlocks(self.nutzerListe[-1])

    def appendAllBlocks(self, nutzer):
        self.txt=open("%s.txt" %(nutzer.name), "a+")
        for x in range(0,len(self.chain[:])):
            self.txt.write(self.blockAsStr(x)+"\r\n")
        self.txt.close()

    def callListeners(self):
        for x in self.nutzerListe:
            x.addToTxt(self.blockAsStr(-1))

    def checkValid(self, block):
        liste = []
        for nutzer in self.nutzerListe:
            liste.append(nutzer.readTxt(block))
        valid = False

        for x in range(len(liste)):
            if x < len(liste)-1:
                if liste[x]==liste[x+1]:
                    valid = True
                else:
                    valid = False
                    return valid
        return valid
#hash berechnen
'''
    def hash(self, block):
        string=""
        liste=[]
        for x in block:
            if type(x)==type([]):
                newListe = x
                for x in newListe:
                    liste.append(x)
            else:
                liste.append(x)
        for element in liste:
            string=str(string)+str(element)
        return(sha256(string.encode("ascii")).hexdigest()   )
    def previousHash(self):
        return(self.hash(self.chain[-1]))
'''

class Nutzer():
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.nutzerStr = ""
        self.txt=open("%s.txt" %(self.name), "a+")
        self.txt.close()
    def changeBalance(self, betrag):
        self.balance = self.balance + betrag
    def nutzerToStr(self):
        self.nutzerStr = str(self.name)+";"+str(self.balance)
        return(self.nutzerStr)
    def addToTxt(self, string):
        self.txt=open("%s.txt" %(self.name), "a+")
        self.txt.write(string+"\r\n")
        self.txt.close()
    def readTxt(self, block):
        self.txt=open("H:\\Facherbeit Blockchain\\blockchain\\%s.txt" %(self.name), "r")
        string = self.txt.readlines(block)
        string=str(string)
        self.txt.close()
        return string[2:-4]




