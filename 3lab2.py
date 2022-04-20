class CTECH:
    pass
class CINTEL:
    pass
class NWC:
    pass
class DSBS:
    pass

instance1 = CTECH()
instance2 = CINTEL()
instance3 = NWC()
instance4 = DSBS()
print(isinstance(instance1, CTECH))
print(isinstance(instance2, CINTEL))
print(isinstance(instance3, NWC))
print(isinstance(instance4, DSBS))
print(isinstance(instance1, object))
print(isinstance(instance2, object))
print(isinstance(instance3, object))
print(isinstance(instance4, object))