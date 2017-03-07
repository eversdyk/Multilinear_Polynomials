def simplify(poly):
    import re
    #first lets separate the terms, keeping the numbers
    term_listnums=re.findall("[\w']+",poly)

    #now lets grab the coefficients from each term and store them for later
    #if there is not a coefficient, lets assume it is "1"
    #also lets go ahead and convert these to integers so that we can sum them later
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

    #now lets remove the coefficients, and sort each group of variables from a-z.
    term_list=[re.sub("[0-9]*","",i) for i in term_listnums]
    sorted_term_list=["".join(sorted(list(i))) for i in term_list]

    #here we will grab the signs (positive or negative) for each coefficient
    sign_list=re.findall("[/+-]",poly)
    polylist=list(poly)
    if polylist[0] is not "-" and polylist[0] is not "+":
        sign_list.insert(0,"+")

    #what we have now are three corresponding lists of identical length: sign(+/-), coefficients, and variables
    #lets go ahead and multiply our coefficients in "values" by -1 if they are negative
    for i in range(0,len(values)):
        if sign_list[i]=='-':
            values[i]*=-1

    #now we only have 2 lists of corresponding coefficients and variables.  Lets create a dictionary to store them as key-value pairs.
    #this is also where we eliminate duplicates and sum the coefficients.
    term_dict={}
    for i in range(0,len(values)):
        if sorted_term_list[i] in term_dict:
            term_dict[sorted_term_list[i]]+=values[i]
        else:
            term_dict[sorted_term_list[i]]=values[i]

    #if the resulting coefficient is 0, lets remove that key-value pair from our dictionary
    term_dict={k: v for k, v in term_dict.items() if v}

    #now lets convert each value (coefficient) in our dictionary to strings, adding the signs which will be used in our final result
    for i in term_dict:
        if term_dict[i]>1:
            term_dict[i]="+"+str(term_dict[i])
        elif term_dict[i]>0:
            term_dict[i]="+"
        elif term_dict[i]>-2:
            term_dict[i]="-"
        else:
            term_dict[i]=str(term_dict[i])

    #now that our dictionary is accurate for each term, lets convert it to a list of tuples,
    #and sort the list of tuples by key length and alphabetically by key
    newdict = term_dict.items()
    sortedlist = sorted(newdict, key=lambda s: (len(s[0]),s))

    #our sorted tuples are backwards, so lets flip them around so the coefficients are listed first
    sortedlist=[x[::-1] for x in sortedlist]

    #now we're ready to go!  just mash together each tuple, then mash everything into the simplified polynomial string!
    outputlist=list("".join(["".join(i) for i in sortedlist]))

    #don't forget, if our string starts with a plus(+) sign, we can remove it from the first term
    if outputlist[0]=="+":
        outputlist=outputlist[1:len(outputlist)]
    return "".join(outputlist)
