def k(a,b):
    if a<=1 or b<=1:
        return 1
    else:
        return k(a//2, b) + k(a, b//2) + k(a//2,b//2)


#cáscara
def k2(a,b):
    d=dict()
    return k_aux(a,b,d)

#versión de axel
def k_aux(a,b,d):
    if a<=1 or b<=1:
        return 1
    else:
        if (a,b) in d:
            return d[(a,b)]
            
        else:
            d[(a,b)] = k_aux(a//2,b,d) + k_aux(a, b//2,d) + k_aux(a//2, b//2,d)
            return d[(a,b)]
    

    
