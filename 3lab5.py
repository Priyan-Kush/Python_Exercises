class PrintDT:
    def python_data(self, input:tuple):
        print(input,type(input).__name__)
    def python_data(self, input:list):
        print(input,type(input).__name__)
    def python_data(self, input:str):
        print(input,type(input).__name__)


printDT = PrintDT()
printDT.python_data((1,2,3))
printDT.python_data([1,2,3])
printDT.python_data("Hello")