class Banks_SRMIST:
    def getBalance(self):
        return 0

class CUB(Banks_SRMIST):
    def getBalance(self):
        return 15000
class HDFC(Banks_SRMIST):
    def getBalance(self):
        return 30000
class Indian_Bank(Banks_SRMIST):
    def getBalance(self):
        return 40000

cub_bank = CUB()
hdfc_bank = HDFC()
indian_bank = Indian_Bank()
print(cub_bank.getBalance())
print(hdfc_bank.getBalance())
print(indian_bank.getBalance())
