## Dada la siguiente secuencia: 
##          1                   sí 1<=k<=3
## Sk=  
##      2S(k-1)+3S(k-2)+4S(k-3) sí k>3
## Implemente una función en Python que calcule Sk usando la estrategia de programación dinámica

## versión recursiva
def calcularSk(k):
    ## caso base
    if 1<=k<=3:
        return 1
    ## casos recursivos
    else:
        return 2*calcularSk(k-1)+3*calcularSk(k-2)+4*calcularSk(k-3)

## versión programación dinámica con recursión
def calcularSkDP(k):
    d=dict()
    return calcularSkDpAux(k, d)

def calcularSkDpAux(k, d):
    if k in d:
        return d[k]
    if 1<=k<=3:
        d[k]=1
        return d[k] 
    else:   
        d[k]=2*calcularSkDpAux(k-1, d)+3*calcularSkDpAux(k-2, d)+4*calcularSkDpAux(k-3, d)
        return d[k]
    
## versión PD bottom-up
def calcularSk(k):
        
    if k<1:
        raise ValueError("k debe ser >= 1")
    if 1<=k<=3:
        return 1
        
    pd=dict()
    pd[1]=pd[2]=pd[3]= 1
    
    for i in range (4, k+1):
        pd[i] = 2*pd[i-1] + 3*pd[i-2] + 4*pd[i-3]
        
    return pd[k]
        
        

    
    
    
    
