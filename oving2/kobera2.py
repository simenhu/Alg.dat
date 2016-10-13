from sys import stdin, stderr
import traceback


class Node:
    def __init__(self):
        self.barn = {}
        self.posi = []


def bygg(ordliste):
    rootNode = Node()
    currentNode = rootNode
    posiCounter = 0
    for tup in ordliste:
        lastCounter = 0
        for letter in tup[0]:

            if currentNode.barn.__contains__(letter):
                currentNode = currentNode.barn.get(letter)

            else:
                currentNode.barn[letter] = Node()
                currentNode = currentNode.barn.get(letter)

            lastCounter +=1
            if (lastCounter == len(tup[0])):
                currentNode.posi.append(tup[1])
        currentNode = rootNode

    return rootNode





def posisjoner(ord, indeks, node):

    if(len(ord)==0):
        return node.posi
    elif (ord[0] == "?"):
        #returnList = []
        #for child in node.barn:
        #    returnList+=posisjoner(ord[1:], indeks +1, node.barn.get(child))
        return [posisjoner(ord[1:],indeks+1, x[1]) for x in node.barn.items()]

    for child in node.barn:
        if(ord[0]==child):
            return posisjoner(ord[1:], indeks, node.barn.get(child))
    return []





def main():
    try:
        #ord = stdin.readline().split()
        with open("textFile.txt", mode="r") as text:

            ord = text.readline().split()

        ordliste =[]
        pos = 0
        for o in ord:
            ordliste.append((o, pos))
            pos += len(o) + 1

        toppnode = bygg(ordliste)
        with open("textFile.txt", mode="r") as text:
            text.readline()
            for sokeord in text:
                sokeord = sokeord.strip()
                print("%s:" % sokeord, end='')
                posi = posisjoner(sokeord, 0, toppnode)

                posi.sort()
                for p in posi:
                    print(" %s" % p, end="")
                print()
    except:
        traceback.print_exc(file=stderr)


#def traverser(toppnode, count, word):
    #for key, value in toppnode.barn.items():
           # if(len(value.barn)==0 or len(value.posi)!=0):
                #print("level:%d letter:%s word:%s position:%a" % (count, key, word+key, value.posi))
           # else:
              #  print("level:%d letter:%s"%(count,key))
           # traverser(value,count+1, word+key)



if __name__ == "__main__":
    main()