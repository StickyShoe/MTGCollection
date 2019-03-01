import sys
import os

# version one when the input used to be [card name] [number of cards]
# converts all input into states divided by $
# hence becomes [card name]$[number of cards]

class converter:

    def convert_v1(filename):

        try:
            data = []
            with open(filename, 'r') as fil: # opens file for reading
                data = fil.read().strip().split("\n")
            findat = []
            for line in data:                    # goes changing each line and appending to findat
                line = line.split(" ")
                findat.append(" ".join(line[:-1]) + "$" + line[-1])
            findat = "\n".join(findat)

        except:
            print("Error occurred")              # handles any exception (improvement needed)

        else:                                    # executes only if there is no error 
            with open(filename, 'w') as fil:     # open file to write findat, wiping all previous data
                fil.write(findat)

if __name__ == "__main__":
    converter.convert_v1("collection.txt")