def simplify(poly):
    import re
    print(poly)
    term_listnums=re.findall("[\w']+",poly)
    term_list=[re.sub("[0-9]*","",i) for i in term_listnums]
    sorted_term_list=["".join(sorted(list(i))) for i in term_list]
    print (sorted_term_list)
    
    p=0
    values=[]
    for i in term_listnums:
        listterm=list(i)
        if listterm[0].isalpha() is True:
            values.append(1)
            p+=1
        else:
            values.append(int(re.findall("[0-9]*",i)[0]))
            p+=1
    print(values)
    
    sign_list=re.findall("[/+-]",poly)
    polylist=list(poly)
    if polylist[0] is not "-" and polylist[0] is not "+":
        sign_list.insert(0,"+")
    print(sign_list)
    
    for i in range(0,len(values)):
        if sign_list[i]=='-':
            values[i]*=-1
    print(values)
    
    term_dict={}
    for i in range(0,len(values)):
        if sorted_term_list[i] in term_dict:
            term_dict[sorted_term_list[i]]+=values[i]
        else:
            term_dict[sorted_term_list[i]]=values[i]
    print(term_dict)
    
    term_dict={k: v for k, v in term_dict.items() if v}
    
    for i in term_dict:
        if term_dict[i]>1:
            term_dict[i]="+"+str(term_dict[i])
        elif term_dict[i]>0:
            term_dict[i]="+"
        elif term_dict[i]>-2:
            term_dict[i]="-"
        else:
            term_dict[i]=str(term_dict[i])
    print(term_dict)
    
    newdict = term_dict.items()
    sortedlist = sorted(newdict, key=lambda s: (len(s[0]),s))
    print(sortedlist)
    sortedlist=[x[::-1] for x in sortedlist]
    print(sortedlist)
    output=[]
    for i in sortedlist:
        output.append("".join(i))
    output="".join(output)
    print(output)
    outputlist=list(output)
    print(outputlist)
    if outputlist[0]=="+":
        outputlist=outputlist[1:len(outputlist)]
    print(outputlist)
    y="".join(outputlist)
    print(y)
    return y
    
