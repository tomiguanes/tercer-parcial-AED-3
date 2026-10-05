def dyc(L, f):
    if len(L)==1
        return L[0]
    else:
        ld=L[:len(L)//2]
        li=L[len(L)//:]
        fi=dyc(li,f)
        fd=dyc(ld,f)
        return f(fi,fd)