import itertools


def order_is_good(p,V,E,Eprime):
    for e in Eprime:
        u = e[0]
        v = e[1]
        pos_u = p.index(u)
        pos_v = p.index(v)
        if pos_u < pos_v:
            linear = True
            wrap = True

            N1 = p[pos_u+1:pos_v]
            for n in N1:
                if [u,n] not in Eprime:
                    linear = False
                    break


            N2 = p[pos_v+1:]
            N3 = p[:pos_u]
            for n in N2:
                if [v,n] not in Eprime:
                    wrap = False
                    break
            for n in N3:
                if [v,n] not in Eprime:
                    wrap = False
                    break

            if not linear and not wrap:
                return False

    return True
    

def is_ca(V,E):
    found = False
    ca_order = None

    print("======")
    print("V = " + str(V))
    print("E = " + str(E))

    Eprime = E.copy()
    for e in E:
        Eprime.append([e[1],e[0]])

    P = itertools.permutations(V,len(V))

    for p in P:
        if order_is_good(p,V,E,Eprime):
            found = True
            ca_order = p
            break

    if found:
        print("The graph is circular-arc.")
        print("Tucker ordering: " + str(p))
    else:
        print("The graph is NOT circular-arc.")
    print("======")


V = [1,2,3,4,5]
E = [[1,2],[2,3],[3,4],[4,5],[5,1]]
is_ca(V,E)
