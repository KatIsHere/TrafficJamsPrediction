import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def getGraph():
    G = nx.Graph()
    G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])
    G.add_edge(1, 3,   highway = "Vasilkivska str.",  maxSpeed = 16.6, maxDensity = 0.2, L = 500, Speed = 15)
    G.add_edge(3, 4,  highway = "Vasilkivska str.",  maxSpeed = 16.6, maxDensity = 0.2, L = 400, Speed = 5)
    G.add_edge(4, 5,   highway = "Vasilkivska str.",  maxSpeed = 16.6, maxDensity = 0.2, L = 200, Speed = 15)     # jam
    G.add_edge(5, 6,   highway = "Vasilkivska str.",  maxSpeed = 16.6, maxDensity = 0.2, L = 210, Speed = 2)
    G.add_edge(6, 7,   highway = "Vasilkivska str.",  maxSpeed = 16.6, maxDensity = 0.2, L = 500, Speed = 6.6)
    G.add_edge(7, 8,   highway = "Vasilkivska str.",  maxSpeed = 16.6, maxDensity = 0.2, L = 90, Speed = 6.6)
    G.add_edge(20, 21,   highway = "Vasilkivska str.",  maxSpeed = 16.6, maxDensity = 0.2, L = 200, Speed = 7.8)
    G.add_edge(21, 2,   highway = "Vasilkivska str.",  maxSpeed = 16.6, maxDensity = 0.2, L = 850, Speed = 8)
    G.add_edge(2, 1,   highway = "Vasilkivska str.",  maxSpeed = 16.6, maxDensity = 0.2, L = 350, Speed = 3)

    G.add_edge(4, 13,  highway = "Burmustechka str.",  maxSpeed = 16.6, maxDensity = 0.2, L = 260, Speed = 10)
    G.add_edge(13, 15,  highway = "Burmustechka str.",  maxSpeed = 16.6, maxDensity = 0.2, L = 550, Speed = 4)

    G.add_edge(3, 14,  highway = "Kolomyskiy str.",  maxSpeed = 16.6, maxDensity = 0.2, L = 550, Speed = 24)

    G.add_edge(2, 14,   highway = "Lomonosov str.",  maxSpeed = 16.6, maxDensity = 0.2, L = 700, Speed = 2)
    G.add_edge(14, 13,   highway = "Lomonosov str.",  maxSpeed = 16.6, maxDensity = 0.2, L = 350, Speed = 15)
    G.add_edge(13, 11,   highway = "Lomonosov str.",  maxSpeed = 16.6, maxDensity = 0.2, L = 240, Speed = 7.8)
    G.add_edge(11, 10,   highway = "Lomonosov str.",  maxSpeed = 16.6, maxDensity = 0.2, L = 220, Speed = 10)

    G.add_edge(8, 9,   highway = "M01",  maxSpeed = 16.6, maxDensity = 0.2, L = 600, Speed = 2)
    G.add_edge(9, 12,   highway = "M01",  maxSpeed = 16.6, maxDensity = 0.2, L = 290, Speed = 15)
    G.add_edge(12, 15,   highway = "M01",  maxSpeed = 16.6, maxDensity = 0.2, L = 200, Speed = 7.8)
    G.add_edge(15, 16,   highway = "M01",  maxSpeed = 16.6, maxDensity = 0.2, L = 750, Speed = 5.5)
    G.add_edge(16, 18,   highway = "M01",  maxSpeed = 16.6, maxDensity = 0.2, L = 450, Speed = 4)
    G.add_edge(18, 19,   highway = "M01",  maxSpeed = 16.6, maxDensity = 0.2, L = 550, Speed = 4)
    G.add_edge(19, 20,   highway = "M01",  maxSpeed = 16.6, maxDensity = 0.2, L = 170, Speed = 3)

    G.add_edge(6, 10,   highway = "Stelmaxa str.",  maxSpeed = 16.6, maxDensity = 0.2, L = 240, Speed = 13)
    G.add_edge(10, 9,   highway = "Stelmaxa str.",  maxSpeed = 16.6, maxDensity = 0.2, L = 210, Speed = 3)
    G.add_edge(5, 11,   highway = "Merichanska str.",  maxSpeed = 16.6, maxDensity = 0.2, L = 280, Speed = 8)
    G.add_edge(11, 12,   highway = "Merichanska str.",  maxSpeed = 16.6, maxDensity = 0.2, L = 240, Speed = 8)

    G.add_edge(16, 17,   highway = "Potehina str.",  maxSpeed = 16.6, maxDensity = 0.2, L = 400, Speed = 15)
    G.add_edge(17, 18,   highway = "Oborony str.",  maxSpeed = 16.6, maxDensity = 0.2, L = 400, Speed = 16)
    return G

#Holosievo
# G.add_edge(1, 3,   highway = "Vasilkivska str.",  maxSpeed = 16.6, maxDensity = 0.2, L = 500, Speed = 15)
# G.add_edge(3, 4,  highway = "Vasilkivska str.",  maxSpeed = 16.6, maxDensity = 0.2, L = 400, Speed = 5)
# G.add_edge(4, 5,   highway = "Vasilkivska str.",  maxSpeed = 16.6, maxDensity = 0.2, L = 200, Speed = 15)     # jam
# G.add_edge(5, 6,   highway = "Vasilkivska str.",  maxSpeed = 16.6, maxDensity = 0.2, L = 210, Speed = 2)
# G.add_edge(6, 7,   highway = "Vasilkivska str.",  maxSpeed = 16.6, maxDensity = 0.2, L = 500, Speed = 6.6)
# G.add_edge(7, 8,   highway = "Vasilkivska str.",  maxSpeed = 16.6, maxDensity = 0.2, L = 900, Speed = 6.6)
# G.add_edge(20, 21,   highway = "Vasilkivska str.",  maxSpeed = 16.6, maxDensity = 0.2, L = 200, Speed = 7.8)
# G.add_edge(21, 2,   highway = "Vasilkivska str.",  maxSpeed = 16.6, maxDensity = 0.2, L = 850, Speed = 3)
# G.add_edge(2, 1,   highway = "Vasilkivska str.",  maxSpeed = 16.6, maxDensity = 0.2, L = 350, Speed = 3)

# G.add_edge(4, 13,  highway = "Burmustechka str.",  maxSpeed = 16.6, maxDensity = 0.2, L = 260, Speed = 25)
# G.add_edge(13, 15,  highway = "Burmustechka str.",  maxSpeed = 16.6, maxDensity = 0.2, L = 550, Speed = 25)

# G.add_edge(2, 14,   highway = "Lomonosov str.",  maxSpeed = 16.6, maxDensity = 0.2, L = 700, Speed = 2)
# G.add_edge(14, 13,   highway = "Lomonosov str.",  maxSpeed = 16.6, maxDensity = 0.2, L = 350, Speed = 15)
# G.add_edge(13, 11,   highway = "Lomonosov str.",  maxSpeed = 16.6, maxDensity = 0.2, L = 240, Speed = 7.8)
# G.add_edge(11, 10,   highway = "Lomonosov str.",  maxSpeed = 16.6, maxDensity = 0.2, L = 220, Speed = 10)

# G.add_edge(8, 9,   highway = "M01",  maxSpeed = 16.6, maxDensity = 0.2, L = 600, Speed = 2)
# G.add_edge(9, 12,   highway = "M01",  maxSpeed = 16.6, maxDensity = 0.2, L = 290, Speed = 15)
# G.add_edge(12, 15,   highway = "M01",  maxSpeed = 16.6, maxDensity = 0.2, L = 20, Speed = 7.8)
# G.add_edge(15, 16,   highway = "M01",  maxSpeed = 16.6, maxDensity = 0.2, L = 750, Speed = 10)
# G.add_edge(16, 18,   highway = "M01",  maxSpeed = 16.6, maxDensity = 0.2, L = 450, Speed = 10)
# G.add_edge(18, 19,   highway = "M01",  maxSpeed = 16.6, maxDensity = 0.2, L = 550, Speed = 10)
# G.add_edge(19, 20,   highway = "M01",  maxSpeed = 16.6, maxDensity = 0.2, L = 170, Speed = 10)

# G.add_edge(6, 10,   highway = "Stelmaxa str.",  maxSpeed = 16.6, maxDensity = 0.2, L = 240, Speed = 13)
# G.add_edge(10, 9,   highway = "Stelmaxa str.",  maxSpeed = 16.6, maxDensity = 0.2, L = 210, Speed = 3)
# G.add_edge(5, 11,   highway = "Merichanska str.",  maxSpeed = 16.6, maxDensity = 0.2, L = 280, Speed = 8)
# G.add_edge(11, 12,   highway = "Merichanska str.",  maxSpeed = 16.6, maxDensity = 0.2, L = 240, Speed = 8)

# G.add_edge(16, 17,   highway = "Potehina str.",  maxSpeed = 16.6, maxDensity = 0.2, L = 400, Speed = 15)
# G.add_edge(17, 18,   highway = "Oborony str.",  maxSpeed = 16.6, maxDensity = 0.2, L = 400, Speed = 16)


# Kiev central


# San Diego
# G.add_edge(1, 2,   highway = "S/O 56",  maxSpeed = 16.6, maxDensity = 0.2, L = 15450, Speed = 29.95168)
# G.add_edge(1, 3,  highway = "Carmel Valley Rd to 5",  maxSpeed = 16.6, maxDensity = 0.2, L = 370, Speed = 5)
# G.add_edge(3, 4,   highway = "Carmel Valley Rd to 5",  maxSpeed = 16.6, maxDensity = 0.2, L = 7242, Speed = 15)     # jam
# G.add_edge(4, 10,   highway = "Carmel Valley Rd to 5",  maxSpeed = 16.6, maxDensity = 0.2, L = 9495, Speed = 2)
# G.add_edge(3, 5,   highway = "S/O 5/805",  maxSpeed = 16.6, maxDensity = 0.2, L = 7725, Speed = 6.6)
# G.add_edge(5, 9,   highway = "S/O 5/805",  maxSpeed = 16.6, maxDensity = 0.2, L = 4830, Speed = 6.6)
# G.add_edge(9, 12,   highway = "S/O 5/805",  maxSpeed = 16.6, maxDensity = 0.2, L = 4830, Speed = 6.6)
# G.add_edge(10, 11,   highway = "S/O 8",  maxSpeed = 16.6, maxDensity = 0.2, L = 3860, Speed = 5)       # jam
# G.add_edge(11, 12,  highway = "S/O 8",  maxSpeed = 16.6, maxDensity = 0.2, L = 3060, Speed = 25)
# G.add_edge(11, 9,  highway = "N/O 163",  maxSpeed = 16.6, maxDensity = 0.2, L = 5310, Speed = 2)
# G.add_edge(9, 7,   highway = "N/O 163",  maxSpeed = 16.6, maxDensity = 0.2, L = 4185, Speed = 2)
# G.add_edge(7, 6,   highway = "N/O 163",  maxSpeed = 16.6, maxDensity = 0.2, L = 2415, Speed = 15)
# G.add_edge(4, 5,   highway = "S/O 52",  maxSpeed = 16.6, maxDensity = 0.2, L = 5310, Speed = 7.8)
# G.add_edge(5, 7,   highway = "S/O 52",  maxSpeed = 16.6, maxDensity = 0.2, L = 4510, Speed = 10)
# G.add_edge(7, 8,   highway = "S/O 52",  maxSpeed = 16.6, maxDensity = 0.2, L = 120, Speed = 7.8)
# G.add_edge(6, 8,   highway = "S/O 15",  maxSpeed = 16.6, maxDensity = 0.2, L = 7080, Speed = 3)
# G.add_edge(2, 6,   highway = "S/O 15",  maxSpeed = 16.6, maxDensity = 0.2, L = 14325, Speed = 27.71648)