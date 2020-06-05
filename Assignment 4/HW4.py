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
    for key, value in d:
        if not (key or value):
            print("error: dictionary is empty")
        else:
            dictstack.append(d)

def define(name, value):
    if not (name, value):
        print("error: neither input can be empty")
    else:
        dictstack.append({name:value})

def lookup(name):
    if len(name) <= 0:
        print("error: name is empty")
    else:
        for i in reversed(dictstack):
            for key, value in i.items():
                key = key[1:]
                if (key == name):
                    return value

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

def aload():
    tup = opPop()
    for item in tup[1]:
        if isinstance(item, str):
            var = lookup(item)
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
    for item in reversed(opstack):
        if isinstance(item, tuple):
            print(item[1])
        else:
            print(item)

def psDict():
    if len(opstack) > 0:
        opPop()
        opPush({})
    else:
        print("error: stack is empty")

def begin():
    if len(opstack) > 0:
        dictPush({})
        opPop()
    else:
        print("error: stack is empty")

def end():
    if len(opstack) > 0:
        dictPop()
    else:
        print("error: stack is empty")

def psDef():
    value = opPop()
    name = opPop()
    define(name, value)

def psIf():
    if len(opstack) > 0:
        op1 = opPop()
        op2 = opPop()
        if op2 == True:
            interpretSPS(op1)
        else:
            print("error: must compare two things")
    else:
        print("error: must have at least two numbers on stack")

def psIfelse():
    if len(opstack) > 2:
        op1 = opPop()
        op2 = opPop()
        op3 = opPop()
        if op3 == True:
            interpretSPS(op2)
        elif (op3 == False):
            interpretSPS(op1)
        else:
            print("error: must compare two things")
    else:
        print("error: must have at least two numbers on stack")

def psFor():
    op1 = opPop()
    if isinstance(op1, tuple):
        op1 = op1[1]
    op2 = opPop()
    op3 = int(opPop())
    op4 = opPop()
    if op3 > 0:
        while op4 <= op2:
            opPush(op4)
            interpretSPS(op1)
            op4 += op3
    else:
        while op4 >= op2:
            opPush(op4)
            interpretSPS(op1)
            op4 += op3

def tokenize(s):
    return re.findall("/?[a-zA-Z][a-zA-Z0-9_]*|[\[][a-zA-Z-?0-9_\s!][a-zA-Z-?0-9_\s!]*[\]]|[-]?[0-9]+|[}{]+|%.*|[^ \t\n]", s)

def groupMatch(it):
    res = []
    for c in it:
        if c == '}':
            return res
        elif c == ']':
            return (len(res), res)
        elif c =='{':
            res.append(groupMatch(it))
        elif c.isnumeric() or c[0] == '-':
            res.append(int(c))
        else:
            res.append(c)
    return False

def parse(L):
    res = []
    it = iter(L)
    for c in it:
        if c =='}':
            return False
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

def interpretSPS(code):
    d = {
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
        'dict':psDict,
        'begin':begin,
        'end':end,
        'def':psDef,
        'if':psIf,
        'ifelse':psIfelse,
        'for':psFor
    }
    for word in code:
        if isinstance(word, (int, list, tuple, bool)):
            opPush(word)
        elif isinstance(word, str):
            if word in d.keys():
                value = d[word]
                value()
            elif word[0] == '/':
                opPush(word)
            else:
                retVal = lookup(word)
                if retVal == None:
                    opPush(word)
                elif isinstance(retVal, list):
                    interpretSPS(retVal)
                else:
                    opPush(retVal)

def interpreter(s):
    interpretSPS(parse(tokenize(s)))

def clearStacks():
    opstack[:] = []
    dictstack[:] = []

input1 ="""
            /fact{
                0 dict
                begin
                    /n exch def
                    1
                    n -1 1 {mul} for
                end 
            } def
            6 fact stack 
        """
input2 ="""
            /x 4 def x x add stack
        """
interpreter(input2)
clearStacks()