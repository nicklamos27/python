# Nick Lamos 11557486
# Worked with Puthypor Sengkeo
import re

opstack = []
def opPop():
    if len(opstack) > 0:
        return opstack.pop()
    else:
        print("error: opstack is empty")
def opPush(value):
    opstack.append(value)

dictstack = []
def dictPop():
    if len(dictstack) > 0:
        return dictstack.pop()
    else:
        print("error: dictstack is empty")
def dictPush(d):
    dictstack.append(d)

def define(name, value):
    if not (name, value):
        print("error: neither input can be empty")
    else:
        if dictstack.count == 0:
            dictPush((0,{name:value}))
        else:
            op1 = dictPop()
            op1[1][name] = value
            dictPush(op1)

def lookup(name, scope):
    if len(name) <= 0:
        print("error: name is empty")
    else:
        if (name[0] != "/"):
            name = "/" + name
        if scope == "static":
            dex = staticLink(name)
            if dex != None:
                return dictstack[dex][1][name]
        elif scope == "dynamic":
            for key, value in reversed(dictstack):
                if name in value:
                    return value[name]
        else:
            print("error - need scope")

def add():
    if len(opstack) > 0:
        op1 = opPop()
        op2 = opPop()
        opPush(op1 + op2)
    else:
        print("error: must have at least two numbers on stack")

def sub():
    if len(opstack) > 0:
        op1 = opPop()
        op2 = opPop()
        opPush(op2 - op1)
    else:
        print("error: must have at least two numbers on stack")

def mul():
    if len(opstack) > 0:
        op1 = opPop()
        op2 = opPop()
        opPush(op1 * op2)
    else:
        print("error: must have at least two numbers on stack")

def div():
    if len(opstack) > 0:
        op1 = opPop()
        op2 = opPop()
        if isinstance(op1, int) and isinstance(op2, int):
            opPush(op2 / op1)
    else:
        print("error: must have at least two numbers on stack")

def eq():
    if len(opstack) > 0:
        op1 = opPop()
        op2 = opPop()
        if op1 == op2:
            opPush(True)
        else:
            opPush(False)
    else:
        print("error: must have at least two numbers on stack")

def lt():
    if len(opstack) > 0:
        op1 = opPop()
        op2 = opPop()
        if isinstance(op1, int) and isinstance(op2, int):
            if op2 < op1:
                opPush(True)
            else:
                opPush(False)
        else:
            print("error: must compare two numbers")
    else:
        print("error: must have at least two numbers on stack")

def gt():
    if len(opstack) > 0:
        op1 = opPop()
        op2 = opPop()
        if isinstance(op1, int) and isinstance(op2, int):
            if op2 > op1:
                opPush(True)
            else:
                opPush(False)
        else:
            print("error: must compare two numbers")
    else:
        print("error: must have at least two numbers on stack")

def length():
    if len(opstack) > 0:
        op1 = opPop()
        opPush(len(op1[1]))
    else:
        print("error: must have at least one item on stack")

def get():
    if len(opstack) > 0:
        op1 = opPop()
        op2 = opPop()
        opPush(op2[1][op1])
    else:
        print("error: must have at least on item on stack")

def put():
    value = opPop()
    index = opPop()
    tup = opPop()
    tup[1][index] = value
    # opPush(tup)

def aload():
    tup = opPop()
    for item in tup[1]:
        if isinstance(item, str):
            var = lookup(item, "")
            opPush(var)
        else:
            opPush(item)
    opPush(tup)

def astore():
    tup = opPop()
    i = len(tup[1]) - 1
    while i >= 0:
        op1 = opPop()
        tup[1][i] = op1
        i = i - 1
    opPush(tup)

def dup():
    if len(opstack) > 0:
        op1 = opPop()
        opPush(op1)
        opPush(op1)
    else:
        print("error: must have at least one item on stack")

def copy():
    if len(opstack) > 0:
        op1 = opPop()
        op2 = opstack.copy()
        i = len(op2) - op1
        while op1 > 0:
            opPush(op2[i])
            op1 -= 1
            i += 1
    else:
        print("error: stack is empty")

def count():
    opPush(len(opstack))

def pop():
    if len(opstack) > 0:
        opPop()
    else:
        print("error: stack is empty")

def clear():
    if len(opstack) > 0:
        while len(opstack) != 0:
            opPop()
    else:
        print("error: stack is empty")

def exch():
    if len(opstack) > 0:
        op1 = opPop()
        op2 = opPop()
        opPush(op1)
        opPush(op2)
    else:
        print("error: must have at least one item on stack")

def stack():
    lengthOS = len(opstack)
    lengthDS = len(dictstack)
    print("==============")
    for dex in range(lengthOS):
        print(opstack[lengthOS - dex - 1])
    print("==============")
    for item1 in reversed(dictstack):
        print("----" + str(lengthDS - 1) + "----" + str(item1[0]) + "----")
        for item2 in item1[1]:
            print(str(item2) + "\t" + str(item1[1][item2]))
        lengthDS -= 1
    print("==============")

def psDef():
    value = opPop()
    name = opPop()
    define(name, value)

def psIf(scope):
    if len(opstack) > 0:
        op1 = opPop()
        op2 = opPop()
        if op2 == True:
            interpretSPS(op1, scope)
        else:
            print("error: must compare two things")
    else:
        print("error: must have at least two numbers on stack")

def psIfelse(scope):
    if len(opstack) > 2:
        op1 = opPop()
        op2 = opPop()
        op3 = opPop()
        if op3 == True:
            interpretSPS(op2, scope)
        elif op3 == False:
            interpretSPS(op1, scope)
        else:
            print("error: must compare two things")
    else:
        print("error: must have at least two numbers on stack")

def psFor(scope):
    op1 = opPop()
    if isinstance(op1, tuple):
        op1 = op1[1]
    op2 = opPop()
    op3 = int(opPop())
    op4 = opPop()
    if op3 > 0:
        while op4 <= op2:
            opPush(op4)
            interpretSPS(op1, scope)
            op4 += op3
    else:
        while op4 >= op2:
            opPush(op4)
            interpretSPS(op1, scope)
            op4 += op3

def tokenize(s):
    return re.findall("/?[a-zA-Z][a-zA-Z0-9_]*|[\[][a-zA-Z-?0-9_\s!][a-zA-Z-?0-9_\s!]*[\]]|[-]?[0-9]+|[}{]+|%.*|[^ \t\n]", s)

def groupMatch(it):
    res = []
    for c in it:
        if c == '}':
            return res
        elif c.lower() == 'true':
            res.append(True)
        elif c.lower() == 'false':
            res.append(False)
        elif c == ']':
            return (len(res), res)
        elif c =='{':
            res.append(groupMatch(it))
        elif c.isnumeric() or c[0] == '-':
            res.append(int(c))
        elif c[0] == '[':
            temp = c[1:-1].split()
            temp.append(']')
            res.append(groupMatch(temp))
        else:
            res.append(c)
    return False

def parse(L):
    res = []
    it = iter(L)
    for c in it:
        if c =='}':
            return False
        elif c.lower() == 'true':
            res.append(True)
        elif c.lower() == 'false':
            res.append(False)
        elif c =='{':
            res.append(groupMatch(it))
        elif c.isnumeric() or c[0] == '-':
            res.append(int(c))
        elif c[0] == '[':
            temp = c[1:-1].split()
            temp.append(']')
            res.append(groupMatch(temp))
        else:
            res.append(c)
    return res

def staticLink(name):
    length = len(dictstack)
    if (name[0] != "/"):
        name = "/" + name
    if length == 0:
        return None
    else:
        dex = length - 1
    while(True):
        for item in dictstack[dex][1]:
            if name in item:
                return dex
        if dex != 0:
            dex = dictstack[dex][0]

def interpretSPS(tokenList, scope):
    d = {
        'dictPop':dictPop,
        'add':add,
        'sub':sub,
        'mul':mul,
        'div':div,
        'eq':eq,
        'lt':lt,
        'gt':gt,
        'length':length,
        'get':get,
        'put':put,
        'aload':aload,
        'astore':astore,
        'dup':dup,
        'copy':copy,
        'count':count,
        'pop':pop,
        'clear':clear,
        'exch':exch,
        'stack':stack,
        'def':psDef,
    }
    dS = {
        'if':psIf,
        'ifelse':psIfelse,
        'for':psFor
    }
    for word in tokenList:
        if isinstance(word, (int, list, tuple, bool)):
            opPush(word)
        elif isinstance(word, str):
            if word in d.keys():
                value = d[word]
                value()
            elif word in dS.keys():
                value = dS[word]
                value(scope)
            elif word[0] == '/':
                opPush(word)
            else:
                retVal = lookup(word, scope)
                if retVal == None:
                    opPush(word)
                elif isinstance(retVal, list):
                    if scope == "static":
                        var = staticLink(word)
                        if var == None:
                            return None
                        else:
                            dictPush((var, {}))
                            interpretSPS(retVal, scope)
                            dictPop() 
                    elif scope == "dynamic":
                        dictPush((0, {}))
                        interpretSPS(retVal, scope)
                        dictPop()
                    else:
                        print("error - need scope")
                else:
                    opPush(retVal)

def interpreter(s, scope):
    interpretSPS(parse(tokenize(s)),scope)

def clear():
    opstack[:] = []

def clearBoth():
    opstack[:] = []
    dictstack[:] = []