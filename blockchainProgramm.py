from classBlockchain import *
import os

'''
#txt = open("testblockchain.txt", "w+")

#txt.close()

txt = open("testblockchain.txt", "r")
inhalt = txt.read()
txt.close()
print(inhalt)

txt = open("testblockchain.txt", "a")
txt.write("test2\r\n")
txt.close()
'''


blockchain=Blockchain()

blockchain.addNutzer(10)
blockchain.addNutzer(10)

blockchain.transaktion("nutzer1","nutzer2",5)

blockchain.addNutzer(1)

blockchain.transaktion("nutzer1","nutzer2",5)
blockchain.transaktion("nutzer2","nutzer1",5)


blockchain.addNutzer(100)

blockchain.nutzerListe[1].readTxt(2)
blockchain.checkValid(-1)
blockchain.transaktion("nutzer3","nutzer4",2)
blockchain.transaktion("nutzer3","nutzer4",1)


'''
cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))
'''





