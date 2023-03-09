import numpy as np

def diskretizuj_interval(L, N):
    x = np.zeros(N)
    for i in range(1,N):
        x[i] += L/(N-1) * i
    return x

x = diskretizuj_interval(3, 9)

def sestav_matici(N):
    #A = np.random.rand(N, N)
    #FIN = np.zeros((N,N))
    #for i in range(-1,2):          algoš pro 3 diagy z random matice
    #    FIN += np.diag(np.diag(A,i),i)
    #return FIN
    A = np.ones((N, N))
    FIN = np.zeros((N,N))
    FIN += np.diag(np.diag(A,-1),-1) * -1
    FIN += np.diag(np.diag(A)) * 2
    FIN += np.diag(np.diag(A, 1), 1) * -1
    return FIN

A = sestav_matici(5)

# ÚKOL: Doplňte kód funkce sestav_f.
#Nyní sestavíme vektor pravé strany. Ten má v případě metody konečných diferencí a nulových okrajových podmínek tvar
#V našem případě si zvolíme pravou stranu ve tvaru




def sestav_f(x, h):
    FIN = np.zeros(np.size(x)*2)
    for i in range(np.size(x)):
        FIN[i] = h**2 * x[i]**2
    FIN[0] += 1
    FIN[np.size(x)-1] += 2
    print(FIN)
    return FIN

import matplotlib.pyplot as plt  
import math   

def mkd_1d(L, N):
    # Řešíme rovnici průhybu struny zatížené danou silou f na intervalu <0, L>:
    # -u''= f, u( 0 ) = 1, u( L ) = 2;   % rovnice struny + okrajové podmínky
    # x z <0,L>                            % interval
    # f = -1                               % zatížení
    
    ## Disretizace intervalu
    # Nejdříve rozdělíme interval <0, L> na N stejně dlouhých podintevalů, tim
    # vznikne n = N + 1 uzlů sítě { x0, x1, ..., xn }:
    n = N + 1                            # počet uzlů
    h = L / N                            # krok sítě
    x = diskretizuj_interval(L, n)
    
    ## Sestavení matice A

    # Matice soustavy ma rozměry (n-2)x(n-2), protože v krajních uzlech řešení 
    # známe:
    A = sestav_matici(n-2)
    
    
    ## Vektor pravé strany
    # Vyhodnotíme funkci f ve vnitřních bodech intervalu a sestavíme vektor 
    # pravé strany
    f = sestav_f(x[1:-1], h)    
    
    ## Numerické řešení
    # Soustavu vyřešíme pomocí funkce solve z knihovny NumPy
    u_inside = np.linalg.solve(A, f)

    # Řešili jsme ve vnitřních bodech intervalu. Před vykreslením doplníme předepsané
    # hodnoty v krajních bodech. Ke spojování vektorů slouží v NumPy funkce concatenate.
    u = np.concatenate(([0], u_inside, [0]))
    
    ## Analyticke reseni
    # Známé analytické řešení vyčíslíme na jemné síti
    x_analytic = diskretizuj_interval(L, 100)
    #u_analytic = 
    #-1 = (1-L**2)/2 * x + x**2/2
    # dát do kv. formula a jedeš a snad to pojede
    ## Vykresleni
    plt.figure(1)
    plt.plot(x, u, 'r-*', label='Numericke reseni')
    plt.plot(x_analytic, u_analytic, label='Analyticke reseni')
    plt.title('Vypoctene vs analyticke reseni')
    plt.legend()
    plt.show()

# Vyřešme na struně délky 5. 
mkd_1d(5, 10)

# Otestujte s různým počtem kroků, s různou délkou struny.




