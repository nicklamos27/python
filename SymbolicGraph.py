from pyeda.inter import *

def CreateG():
    nodes = range(0, 32)
    return [(i, j) for i in nodes for j in nodes if (i + 3) % 32 == j % 32 or (i + 8) % 32 == j % 32]

def ToBinary():
    iBinary = []
    jBinary = []
    for i,j in G:
        x = '{0:08b}'.format(i)
        iBinary = list(map(int,x))
        y = '{0:08b}'.format(j)
        jBinary = list(map(int,y))

        ijBinary = (iBinary,jBinary)
        binary.append(ijBinary)

def ToExpression():
    for pair in binary:
        exp = ''
        count = 0
        for i in pair[0]:
            if(i == 1):
                exp += 'x' + str(count) + ' & '
            elif (i == 0):
                exp += '~x' + str(count) + ' & '
            count += 1
        count = 0            
        for i in pair[1]:
            if(i == 1):
                exp += 'y' + str(count) + ' & '
            elif (i == 0):
                exp += '~y' + str(count) + ' & '
            count += 1
        exp = exp[:-3]
        expressions.append(exp)

def ToBDD(BDDvar):
    for exp in expressions[1:]:
        obj = expr2bdd(expr(exp))
        BDDvar = BDDvar | obj

if __name__ == "__main__":
    G = CreateG()
    binary = []
    ToBinary()
    expressions = []
    ToExpression()

    x,y,z = map(expr, "xyz")
    xx,yy,zz = map(bddvar, "xyz")

    BDDvar = expr2bdd(expr(expressions[0]))
    ToBDD(BDDvar)

    r1 = BDDvar.compose({xx:zz})
    r2 = BDDvar.compose({zz:yy})
    BDDvar = (r1 & r2).smoothing(zz).equivalent(True)
    print(BDDvar)