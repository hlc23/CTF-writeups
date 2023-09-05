import math

def base256(M):
    base = 256
    message256 = []
    sisa = M
    z = int(M)
    p = int(math.floor(math.log(z, base)))
    r = p
    for j in range(r + 1):
        k = sisa % base
        sisa = sisa // base
        message256.append(k)
    return message256

def Encode256(ascii):
    ascii256 = ""
    for i in range(len(ascii)):
        g = int(ascii[i])
        ascii256 += chr(g)
    return ascii256

def main():
    N = 1280678415822214057864524798453297819181910621573945477544758171055968245116423923
    e = 65537
    c = 62324783949134119159408816513334912534343517300880137691662780895409992760262021
    phiN = 1280678415822214057864524798453297819181234364596418349127352680639289550089776560

    d = pow(e, -1, phiN)
    m = pow(c, d, N)

    print("d =", d)
    print("m =", m)

    print("m in base 256 =", base256(m))
    print("Convert with ASCII:")
    flag = Encode256(base256(m))
    flag = reversed(flag)
    print("flag =", ''.join(flag))

if __name__ == "__main__":
    main()
