import sys
def reading(path,option):
    try:
        file = open(path,'r')
        if(file.readable()):
            if(option=="all"):
                for line in file:
                    print(line)
            elif(isinstance(option,(int))):
                print(file.read(option))
            elif(option=='line'):
                print(file.readline())
            elif(option=='lines'):
                print(file.readlines())
        file.close()
    except:
        print(sys.exc_info()[1])

def writing(path,content):
    newlist=[]
    try:
        file=open(path,'w')
        if(file.writable()):
            if(isinstance(content,(str))):
                file.write(content)
            elif(isinstance(content,(list))):
                for x in content:
                    x=x+"\n"
                    newlist.append(x)
                file.writelines(newlist)
    except:
        print(sys.exc_info()[1])

def appending(path,content):
    newlist=[]
    try:
        file=open(path,'a')
        if(file.writable()):
            if(isinstance(content,(str))):
                file.write(content)
            elif(isinstance(content,(list))):
                for x in content:
                    x=x+"\n"
                    newlist.append(x)
                file.writelines(newlist)
    except:
        print(sys.exc_info()[1])