import numpy as np
import matplotlib.pylab as plt
def dist(xb,x0,yb,y0):
    d=np.sqrt(((xb-x0)**2)+((yb-y0)**2))
    return d
def dv(v1,v2,v3,v4,v5,v6):
    m=np.var([v1,v2,v3,v4,v5,v6])
    return m

def MH(xg,yg,N):
    
    X=[xg]
    Y=[yg]
    
    
    px1=4
    px2=10
    px3=12
    px4=80
    px5=50
    px6=40
    
    py1=100
    py2=5
    py3=80
    py4=50
    py5=50
    py6=200
    
    d1=dist(px1,xg,py1,yg)
    d2=dist(px2,xg,py2,yg)
    d3=dist(px3,xg,py3,yg)
    d4=dist(px4,xg,py4,yg)
    d5=dist(px5,xg,py5,yg)
    d6=dist(px6,xg,py6,yg)
    
    t1=73
    t2=28
    t3=59
    t4=52
    t5=39
    t6=137
    
    v1=d1/t1
    v2=d2/t2
    v3=d3/t3
    v4=d4/t4
    v5=d5/t5
    v6=d6/t6
    
    V=[np.mean(v1,v2,v3,v4,v5,v6)]
    
    errv=exp(-1*dv(v1,v2,v3,v4,v5,v6))
    
    std=0.5
    
    for i in range(N):
        movex=np.random.normal(0,std)
        movey=np.random.normal(0,std)
        
        dn1=dist(px1,xg+movex,py1,yg+movey)
        dn2=dist(px2,xg+movex,py2,yg+movey)
        dn3=dist(px3,xg+movex,py3,yg+movey)
        dn4=dist(px4,xg+movex,py4,yg+movey)
        dn5=dist(px5,xg+movex,py5,yg+movey)
        dn6=dist(px6,xg+movex,py6,yg+movey)
        
        vn1=d1/t1
        vn2=d2/t2
        vn3=d3/t3
        vn4=d4/t4
        vn5=d5/t5
        vn6=d6/t6
    
        
        errn=exp(-1*dv(vn1,vn2,vn3,vn4,vn5,vn6))
        
        a=errn/errv
        
        if(a>=1):
            X.append[xg+move1x]
            Y.append[yg+move1y]
            V.append[vn1]
            v1=vn1
            xg=xg+movex
            yg=yg+movey
            
            
        else:
            b=np.random.uniform(0,1)
            if(a>b):
                X.append[xg+move1x]
                Y.append[yg+move1y]
                V.append[vn1]
                xg=xg+movex
                yg=yg+movey
                v1=vn1
            else:
                X.append[xg]
                Y.append[yg]
                V.append[v1]
                xg=xg+movex
                yg=yg+movey