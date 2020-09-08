'''
Created on 09-Sep-2019
'''

def main():
    
    finallistU = processRitem([],'') # works
    finallistF = processRitem([],'') # works
    finallistD = processRitem([],'') # works
    finallistUsd = processUSD([]) # works
    finallistall = processAllR([]) # need to fix
    print(finallistU)
    print(finallistF)
    print(finallistD)
    print(finallistUsd)
    print(finallistall)


def processRitem(item, key):
    rlist = []
    for it in item:
        for el in it:
            if key in el:
                if el[key] in rlist:
                    continue
                else:
                    rlist.append(el[key])
    return rlist

def processUSD(item):
    uslist = processRitem(item,'')
    dlist = processRitem(item,'')
    outlist = uslist + dlist
    return  outlist       
                

def processAllR(item):
    uslist = processRitem(item,'')
    dlist = processRitem(item,'')
    flist = processRitem(item,'')
    outlist = uslist + dlist + flist
    return  outlist 

if __name__ == '__main__':
    main()