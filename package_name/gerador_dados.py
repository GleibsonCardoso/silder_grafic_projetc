import numpy as np

def graf2(indice):

    ang0 = 30
    ang1 = 90
    theta = []
    ang = []

    for i in np.arange(ang0,ang1,0.1):
            ang.append(i)

    for i in np.arange(ang0,ang1,0.1):
            valores = (np.pi/180)*i
            theta.append(valores)

    ref = []
        
    for i, th in enumerate(theta):
            
            n1re=1.5139
            n1im=0
            n1 = n1re + 1j*n1im
            e1 = (n1re**2-n1im**2) + 1j*(2*n1re*n1im)
            d1 = 1
        
            n2re=0.11112
            n2im=3.9995
            n2 = n2re + 1j*n2im
            e2 = (n2re**2-n2im**2) + 1j*(2*n2re*n2im)
            d2 = 50e-9
        
            n3re=indice
            n3im = 0
            n3 = n3re + 1j*n3im
            d3 = 8e-9
        
            n4re = 1.333
            n4im = 0
            n4 = n4re + 1j*n4im
            d4 = 500e-9
        
            onda = 670
            total = onda * 1e-9
        
            q1 = (np.sqrt(n1**2-(n1re*np.sin(float(th)))**2))/n1**2      
            q2 = (np.sqrt(n2**2-(n1re*np.sin(float(th)))**2))/n2**2
            q3 = (np.sqrt(n3**2-(n1re*np.sin(float(th)))**2))/n3**2
            q4 = (np.sqrt(n4**2-(n1re*np.sin(float(th)))**2))/n4**2
                
            beta2 = (2*np.pi*d2*np.sqrt(n2**2-(n1re*np.sin(float(th)))**2))/total
            beta3 = (2*np.pi*d3*np.sqrt(n3**2-(n1re*np.sin(float(th)))**2))/total
            
            M2 = np.array([[np.cos(beta2),-1j*np.sin(beta2)/q2],[-1j*q2*np.sin(beta2),np.cos(beta2)]])
            M3 = np.array([[np.cos(beta3),-1j*np.sin(beta3)/q3],[-1j*q3*np.sin(beta3),np.cos(beta3)]])
            M = np.dot(M2,M3)
            
            
            ET = ((M[0,0]+M[0,1]*q4)*q1-(M[1,0]+M[1,1]*q4))/((M[0,0]+M[0,1]*q4)*q1+(M[1,0]+M[1,1]*q4))
            ref.append(ET)
            
    y =np.real(np.array(ref*np.conjugate(ref)))
    
    return y
