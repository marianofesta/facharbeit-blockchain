from classBlockchain import *


blockchain=Blockchain()

blockchain.addNutzer(10)

blockchain.addNutzer(10)

blockchain.transaktion("nutzer1","nutzer2",5)

blockchain.addNutzer(1)

blockchain.transaktion("nutzer1","nutzer2",5)

blockchain.transaktion("nutzer2","nutzer1",5)

blockchain.addNutzer(100)

blockchain.transaktion("nutzer2", "nutzer4", 13)

