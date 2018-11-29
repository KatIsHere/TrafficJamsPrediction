from math import ceil
import scipy.integrate as integrate

class LWR_Model:
    """Implements LWR traffic flow macro-model"""

    def __init__(self, segmentLenght, maxSpeed, startDensity = None, driverReact = 5, vehicleLen = 7.5, _segmNumb = 100):
        """cegmentLenght in m, avarageSpeed in m/s"""
        self._p0 = startDensity                 # function
        self._Len = segmentLenght
        self._maxSpeed = maxSpeed
        self.vehicleLen = vehicleLen
        self._pMax = 0.2 #1 / vehicleLen         
        self._segmNumb = _segmNumb
        self._deltaX = segmentLenght/_segmNumb  # meters

    
    def SpeedToDensity(self, v, vMax):
        return self._pMax*(1 - v/vMax)

    def start_dens(self, x, lMap, Gr, nodes):
        if x < 0:
            maxSpeed = Gr.edges[nodes[0], nodes[1]]['maxSpeed']
            sp = Gr.edges[nodes[0], nodes[1]]['Speed']
            dens = self.SpeedToDensity(sp, maxSpeed)
            return dens       
        else:
            for i in range(len(lMap) - 1):
                if x >= lMap[i] and x <= lMap[i + 1]:
                    maxSpeed = Gr.edges[nodes[i], nodes[i+1]]['maxSpeed']
                    sp = Gr.edges[nodes[i], nodes[i+1]]['Speed']
                    dens = self.SpeedToDensity(sp, maxSpeed)
                    return dens       

    # def Density(self, xmin, xmax, tmax, M, N, startDens = True, lMap = None, Gr = None, nodes = None):
    #     ht = tmax/N
    #     hx = (xmax - xmin)/M
    #     dens = [0 for i in range(N)]
    #     if not startDens:
    #         dens[0] = [self.start_dens(xmin + i*hx, lMap, Gr, nodes) for i in range(M)]
    #     else:
    #         dens[0] = [self._p0(xmin + i*hx) for i in range(M)]
    #     a = lambda p: self._maxSpeed*(1 - 2*p/self._pMax)  
    #     for i in range(N-1):
    #         dens[i+1] = [0 for j in range(M)]
    #         x = xmax - a(dens[i+1][0])*i*ht
    #         if not startDens:
    #             dens[i+1][0] = self.start_dens(x, lMap, Gr, nodes)
    #         else:
    #             dens[i+1][0] = self._p0(x)
    #         for j in range(1, M):
    #             dudx = (dens[i][j] - dens[i][j-1])/hx
    #             dens[i+1][j] = -a(dens[i][j])*dudx*ht + dens[i][j];
    #     return dens  


    def speed(self, p):
        return self._maxSpeed * (1 - p / self._pMax)


    def diagramFlow(self, p):
        return p*self.speed(p)


    # def nextDens(self, pThis, pPrev, deltaX, deltaT):
    #     return pThis + deltaT/deltaX * (self.diagramFlow(pThis) - self.diagramFlow(pPrev))


    # def DensityPrognose(self, xmin, xmax, tmax, M, N):
    #     dens = [0 for i in range(N)]
    #     hx = (xmax - xmin)/M
    #     ht = tmax/N
    #     dens[0] = [self._p0(xmin + i*hx) for i in range(M)]
    #     for i in range(1, N):
    #         dens[i] = [self.nextDens(dens[i-1][j], dens[i-1][j - 1], hx, ht) for j in range(1, M)]
    #         dens[i].insert(0, self.nextDens(dens[i-1][0], 0, ht, hx))
    #     return dens


    # def pEven(self, pPrev, pThis, pNext, f):
    #     return self._deltaT*(f(pThis) - (pNext - pPrev)/(2*self._deltaX)*(self._maxSpeed - 2*pThis/self._pMax)) + pThis


    # def pOdd(self, pPrevThis, pPrev, pThis, pNext, f):
    #     return (pPrevThis/self._deltaT - (pNext - pPrev)/(2*self._deltaX)*self._maxSpeed + f(pPrevThis))/(1/self._deltaT - 2/self._pMax*(pNext - pPrev)/(2*self._deltaX))
    

    # def netCounter(self, odd, pPrevn, pThisn, pNextn, pPrevn_1, pThisn_1, pNextn_1):
    #     if(odd):
    #         return self.pEven(pPrevn, pThisn, pNextn, lambda x: 0)
    #     else:
    #         return self.pOdd(pThisn, pPrevn_1, pThisn_1, pNextn_1, lambda x: 0)
        

    # def DensityFirst(self, xmin, xmax, tmax, M, N, pMax):
    #     dens = [0 for i in range(N)]
    #     dens[0] = [self._p0(xi) for xi in range(M)]
    #     for n in range(1, N):
    #         dens[n] = [0 for i in range(M)]
    #         #dens[n][0] = self.pEven(0, dens[n-1][0], dens[n-1][1], lambda x: 0)
    #         if n%2==0:
    #             if n ==150:
    #                 print("")
    #             dens[n][0] = 0      # self.netCounter(n%2==0, 0, dens[n-1][0], dens[n-1][1], 0,dens[n][0], dens[n-1][1])
    #         for i in range(n%2, M - 1, 2):
    #             dens[n][i] = self.netCounter((i+n)%2==0,dens[n-1][i-1], dens[n-1][i], dens[n-1][i+1], dens[n][i-1], dens[n][i], dens[n][i+1])
    #         if n%2==0:
    #             dens[n][M - 1] = 0 #self.netCounter((self._segmNumb - 1 + n)%2==0, dens[n-1][self._segmNumb - 2], dens[n-1][self._segmNumb - 1], 0, dens[n][self._segmNumb - 2], dens[n][self._segmNumb - 1], 0)
        
    #         for i in range(n%2 + 1, M - 1, 2):
    #             dens[n][i] = self.netCounter((i+n)%2==0,dens[n-1][i-1], dens[n-1][i], dens[n-1][i+1], dens[n][i-1], dens[n][i], dens[n][i+1])
    #         if n%2 != 0:
    #             dens[n][0] = 0   # self.netCounter(n%2==0, 0, dens[n-1][0], dens[n-1][1], 0,dens[n][0], dens[n-1][1])
    #         if n%2 != 0:
    #             dens[n][M - 1] = 0     # self.netCounter((self._segmNumb - 1 + n)%2==0, dens[n-1][self._segmNumb - 2], dens[n-1][self._segmNumb - 1], 0, dens[n][self._segmNumb - 2], dens[n][self._segmNumb - 1], 0)
    #     return dens


    # def u1(self, xmin, t, a):
    #     return self._p0(xmin - a*t)


    def q(self, p):
        return p*self.speed(p)


    def qG(self, pLeft, pRight):
        pc = self._maxSpeed*self._pMax / 2
        if pRight <= pLeft and pLeft <= pc:
            return self.q(pLeft)
        elif pRight <= pc and pc <= pLeft:
            return self.q(pc)
        elif pc <= pRight and pRight <= pLeft:
            return self.q(pRight)
        elif pLeft < pRight:
            return min(self.q(pLeft), self.q(pRight))


    def p0_n1(self, p0_n, p1_n, teta, h, integr):
        p_1 = 1/teta * integr
        return p0_n + teta/h*(self.qG(p_1, p0_n) - self.qG(p0_n, p1_n))


    def pM_n(self, pM_1_n, pM_n, teta, h, integr):
        p_1 = 1/teta * integr
        return pM_1_n + teta/h * (self.qG(pM_1_n, pM_n) - self.qG(pM_n, p_1))


    def Godunov(self, x0, L, teta, M, N, p0, dens0 = None):
        density = [0 for n in range(N)]
        h = (L - x0)/M
        if dens0 is None:
            density[0] = [p0(x0 + h*i) for i in range(M)]
        else:
            density[0] = dens0
        for n in range(1, N):
            density[n] = []
            for i in range(M):
                if (i == 0):
                    integr = teta * density[n-1][i]
                    pi_n = self.p0_n1(density[n-1][i], density[n-1][i+1], teta, h, integr)
                elif (i == M-1):
                    integr = teta * density[n-1][i]
                    pi_n = self.pM_n(density[n-1][i-1], density[n-1][i], teta, h, integr)
                else:
                    pi_n = density[n-1][i] + teta/h * \
                            (self.qG(density[n-1][i-1], density[n-1][i]) - \
                            self.qG(density[n-1][i], density[n-1][i+1]))
                
                density[n].append(pi_n)
        return density

