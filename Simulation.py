# -*- coding: utf-8 -*-

import numpy as np
import math
import pickle

def sc(pi, gi, po, go, n):
    pi= float(pi)
    po= float(po)
    gi= float(gi)
    go= float(go)
    n= float(n)
    a = (go-po)/(gi-pi)
    return (n-pi)*a+po

def petit(n1, n2):
    if n1>n2:
        return n2
    else:
        return n1
def grand(n1, n2):
    if n1<n2:
        return n2
    else:
        return n1
    
def float_range(debut, fin, pas):
    ls= []
    
    while debut< fin:
        ls.append(debut)
        debut+=pas
    return ls

def intersection(d1, d2):
    sys = np.array([d1[0:2], d2[0:2]])
    val = np.array([[-d1[2]], [-d2[2]]])
    sol = []
    try:
        sol = np.linalg.solve(sys, val)
    except:
        return False
    x = sol[1][0]
    y = sol[0][0]
    return (x, y)

def dans_intervalle(d1, d2, x, y):
    if d1[3] <= x <= d1[4] and d2[3] <= x <= d2[4]:
        if d1[5] <= y <= d1[6] and d2[5] <= y <= d2[6]:
            return True
    return False

def convertir_fichier(nom_fichier, ls_p):
    print ls_p
    l = []
    for x in ls_p:
        for y in x:
            l.append(y)
    print "l:", l
    with open(nom_fichier, "wb") as fichier:
        mon_pickler = pickle.Pickler(fichier)
        mon_pickler.dump(l)




class robot:
    def __init__(self, carte):
        self.posx = 0.0
        self.posy = 0.0
        self.angle = 0.0# angle en radians
        self.carte = carte
        self.ls_droites = []
        self.ls_points = []
        self.dist_max_point = 2.5
        self.division = 10
        self.ls_pos = []

    def avancer(self, distance):
        self.posx = math.cos(self.angle)*distance
        self.posy = math.sin(self.angle)*distance

    def tourner(self, angle):
        self.angle += angle

    def creer_droites(self):
        self.ls_droites = []

        for alpha in float_range(0.0,2.0*math.pi, (2.0*math.pi)/48):
            droite_robot = []
            if math.cos(self.angle+alpha)!=0:
                pente = (1.0/math.cos(self.angle+alpha))*math.sin(self.angle+alpha)
                y_origine = self.posy-pente*self.posx
                if math.cos(self.angle+alpha)<0:
                    if math.sin(self.angle+alpha)<0:
                        droite_robot = [-1, pente, y_origine, -float("inf"), self.posx, -float("inf"), self.posy]
                    else:
                        droite_robot = [-1, pente, y_origine, -float("inf"), self.posx, self.posy, float("inf")]
                else:
                    if math.sin(self.angle+alpha)<0:
                        droite_robot = [-1, pente, y_origine, self.posx, float("inf"), -float("inf"), self.posy]
                    else:
                        droite_robot = [-1, pente, y_origine, self.posx, float("inf"), self.posy, float("inf")]
            else:
                droite_robot = [0, -1, self.posx, self.posx, self.posx, -float("inf"), float("inf")]
            self.ls_droites.append(droite_robot)
        return self.ls_droites

    def tour_points(self):
        self.creer_droites()
        self.trouver_points()
        self.ls_pos.append((self.posx, self.posy))
    def trouver_points(self):

        ls_p = []
        #ls_p.append((self.posx, self.posy))
        for droite_robot in self.ls_droites:
            inter = False
            dist_inter = False
            for droite_map in self.carte.ls_droites:
                coupe = intersection(droite_robot, droite_map)
                if coupe != False:
                    if dans_intervalle(droite_robot, droite_map, coupe[0], coupe[1]):
                        if inter == False:
                            inter = coupe
                            dist_inter = math.sqrt((self.posx-inter[0])**2 + (self.posy-inter[1])**2)
                        else:
                            d = math.sqrt((self.posx-coupe[0])**2 + (self.posy-coupe[1])**2)
                            if d<dist_inter:
                                inter = coupe
                                dist_inter = d
                else:
                    print("pas d'intersection")
            if inter != False:
                ls_p.append(inter)
        self.ls_points.append(ls_p)


    def trouver_chemin(self, x, y):
        if self.test_droite((self.posx, self.posy), (x, y)):
            self.posx = x
            self.posy = y
            print("CHEMIN BON")
        else:
            print("CHEMIN BLOQUE")

    def test_point(self, point):
        point_bon = True
        for pointc in self.ls_points[-1]:
            dist = math.sqrt((point[0]-pointc[0])**2 +(point[1]-pointc[1])**2)
            print "dist", dist
            if dist < self.dist_max_point:
                point_bon  = False

        return point_bon
    def test_droite(self, point1, point2):
        droite_ok = True
        ls_points = []
        for i in range(self.division):
            x = (((point2[0]-point1[0])/self.division)*i)+point1[0]
            y = (((point2[1]-point1[1])/self.division)*i)+point1[1]

            ls_points.append((x, y))
        #self.ls_points.append(ls_points)
        for point in ls_points:
            if not self.test_point(point):
                droite_ok = False
            print droite_ok
        return droite_ok

    def deplacement_auto(self):
        ls_p = self.ls_points[-1]
        ls_dist = []
        for point in range(1, len(ls_p)-1):
            dist = math.sqrt((ls_p[point][0]-ls_p[point+1][0])**2+ (ls_p[point][1]-ls_p[point+1][1])**2)
            #print "p1", ls_p[point]
            #print "p1", ls_p[point+1]
            ls_dist.append(dist)
            #print "dist = ", dist
            #print ""

        b = (0, 0)
        for i in enumerate(ls_dist):
            if i[1]>b[1]:
                b = i
        p1 = ls_p[b[0]+1]
        p2 = ls_p[b[0]+2]

        #print(((p1[0]+p2[0])/2), ((p1[1]+p2[1])/2))
        #self.trouver_chemin(((p1[0]+p2[0])/2), ((p1[1]+p2[1])/2))
        self.trouver_chemin(0, 10)
        #self.ls_points.append([(((p1[0]+p2[0])/2), ((p1[1]+p2[1])/2))])
    def afficher_droites(self):
        for droite in self.ls_droites:
            print(str(droite[0])+"y+"+str(droite[1])+"x+"+str(droite[2])+"=0 xe["+ str(droite[3])+", "+str(droite[4])+ "] ye["+str(droite[5])+", "+str(droite[6])+"]")


class Carte:
    def __init__(self, points):
        self.points = points
        self.ls_droites = []
        self.droites()

    def droites(self):
        for i in self.points:
            for j in range(len(i)):
                a = i[j]
                if j != len(i)-1:
                    b = i[j+1]
                else:
                    b = i[0]

                if a[0] == b[0]:
                    self.ls_droites.append((0, 1, -a[0],  petit(a[0], b[0]), grand(a[0], b[0]), petit(a[1], b[1]), grand(a[1], b[1])))
                else:
                    B = float(b[1]-a[1])/float(b[0]-a[0])
                    C = float(a[1])-(B*float(a[0]))
                    self.ls_droites.append((-1, B, C, petit(a[0], b[0]), grand(a[0], b[0]), petit(a[1], b[1]), grand(a[1], b[1])))

    def afficher_droite(self):
        for droite in self.ls_droites:
            print(str(droite[0])+"y+"+str(droite[1])+"x+"+str(droite[2])+"=0 xe["+ str(droite[3])+", "+str(droite[4])+ "] ye["+str(droite[5])+", "+str(droite[6])+"]")

if __name__ == "__main__":

    C = Carte([[(-10, -10), (-10, 15), (20, 15), (20, 5), (5, 5), (5, -10)]])


    r = robot(C)
    r.posy = 0
    r.tour_points()
    r.deplacement_auto()
    r.tour_points()
    r.ls_points.append(r.ls_pos)
    convertir_fichier("map.sce",r.ls_points)
