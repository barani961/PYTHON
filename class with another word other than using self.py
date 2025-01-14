class barani:
    def __init__(niga,name,sec):
        niga.name=name
        niga.sec=sec
    def print_info(niga):
        print(niga.name)
        print(niga.sec)
        
obj=barani('barani','B')
obj2=barani('sanjay','C')
print(obj2.name)
