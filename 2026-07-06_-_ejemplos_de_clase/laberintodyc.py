"""
dividir y conquistar laberinto

laberintodyc(f, c)
-- 1												f=maxf, c=maxc
-- laberintodyc(f+1, c) + laberintodyc(f, c+1) 		f<maxf, c<maxc
-- laberintodyc(f+1, c)								f<maxf, c>=maxc
-- laberintodyc(f, c+1)								f>=maxf, c<maxc
"""
maxf = 25
maxc = 25

def labdyc(f, c):
    if f==maxf and c==maxc:
        return 1
    else:
        derecha = 0
        abajo = 0
        if c<maxc:
            derecha = labdyc(f, c+1)
        if f<maxf:
            abajo = labdyc(f+1 , c)
        
        return derecha+abajo
    
def labpd2(f, c):
    d = dict()
    return labpd(f, c, d)

def labpd(f, c, d):
    if f==maxf and c==maxc:
        return 1
    else:
        derecha = 0
        abajo = 0
        if c<maxc:
            if (f,c+1) not in d:
                d[(f,c+1)] = labpd(f, c+1, d)
            derecha = d[(f, c+1)]
            
        if f<maxf:
            if (f+1,c) not in d:
                d[(f+1, c)]= labpd(f+1 , c, d)
            abajo = d[(f+1, c)]
        
        return derecha+abajo