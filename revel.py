# def backup()
# def calltodisk()
# def main()
# def increment()
# def decrement()

import sys
class Pack(object):
    def __init__(self):
        self.collection = {}

    def calltodisk(self, filename=""):
        with open(filename, 'r') as f: 
            for line in f:
                self.collection[line.strip().split("$")[0]] = line.strip().split("$")[1:]
        return self

    

    def __str__(self):
        print('Collection')
        print('_' * 30 + ' \n')
        for k, v in sorted(self.collection.items()):
            print('{:<30s}|  {:>10s}x'.format(k, v[0]))
        return "\n"

def menu():
    print("1 -Search for Card")
    print("2 -Edit Card Count")
    print("3 -Add a card")
    print("4 -Initialize an external collection")
    print("5 -Exit","\n\nEnter an option: ",end="")

def main():
    P = Pack().calltodisk('collection.txt')
    print(P)
    menu()
    resp = input()
     
    

if __name__ == "__main__":
    main()
