def CMax(c1, c2, c3):
    c_max = 0
    for d1 in d:
        for d2 in d:
            for d3 in d:
                for d4 in d:
                    new_c_max = abs(c1*d1+c2*d2+c3*d3+d4)
                    if new_c_max > c_max:
                        c_max = new_c_max
    return c_max

def KC(c_final):
    if c_final <= 0:
        return 0
    else:
        return len(str(bin(c_final)[2:]))

def BI(c_final):
    if i == KC(c_final) + 1:
        return 0
    elif i < 1 or i >= len(str(bin(c_final)[2:])) + 1:
        return "error i out of bounds"
    else:
        return str(bin(c_final)[2:])[::-1][i - 1]

def MMovesIfTrue(a1, a2, a3, carry_state, i_state, c_final):
    valid = False
    r = c1*a1 + c2*a2 + c3*a3 + int(BI(c_final)) + carry_state
    carry_prime = carry_state + 1
    i_prime = i_state + 1
    if r % 2 == 0 and carry_prime == r / 2:
        if 1 <= i_state <= KC(c_final):
            valid = i_prime == i + 1
        elif i_state > 1 or i_state >= KC(c_final):
            valid = i_prime == i_state
    return valid

def ConstuctFA(M, c1, c2, c3, c_final):
    state = [0, 1]
    M.append(state)
    for carry_state in range(-CMax(c1, c2, c3), CMax(c1, c2, c3) + 1):
        for i_state in range(1, int(KC(c_final)) + 2):
            for a1 in d:
                for a2 in d:
                    for a3 in d:
                        if MMovesIfTrue(a1, a2, a3, carry_state, i_state, c_final):
                            state = [carry_state, i_state]
                            M.append(state)

if __name__ == "__main__":
    c1 = int(input("Enter C1: "))
    c2 = int(input("Enter C2: "))
    c3 = int(input("Enter C3: "))
    c = int(input("Enter C: "))
    d1 = int(input("Enter D1: "))
    d2 = int(input("Enter D2: "))
    d3 = int(input("Enter D3: "))
    d_final = int(input("Enter D: "))
    i = int(input("Enter i for bi: "))
    d = [0, 1]
    M1 = []
    M2 = []
    ConstuctFA(M1, c1, c2, c3, c)
    ConstuctFA(M2, d1, d2, d3, d_final)
    M = [(a, b) for a in M1 for b in M2]
    print("Cmax =", CMax(c1, c2, c3))
    print("Kc =", KC(c))
    print("bi =", BI(c))
    print("M =", str(M))
