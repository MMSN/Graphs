#!/usr/bin/env python
# -*- coding: latin1 -*-

import string
import numpy
import classGRAFO_definitiva
from classGRAFO_definitiva import *
#import kruskal
#from kruskal import *
import kruskal2
from kruskal2 import *
#import tentativa1
#from tentativa1 import *

class ler_arq(grafo):
    
    def __init__(self,grafo):
        f=raw_input()
        zodiac=f[0:9]
        #print zodiac
        
        if (zodiac!='*Vertices'):
            #print "ERRO!"
            return None
        wow=f.split()
        w = wow[1]
        #f.read(1)
        #print w
        for i in range(int(w)):
            talk=raw_input()
            X=talk.split()
            #print X
            Y=X[0]
            #print Y
            rest=X[1:]
            Z=" ".join(rest)
            #print Z
            #print rest
            apoc.new_vertex(Y,Z)
            
        #apoc.print_matriz_edge()
        #apoc.print_vertex_names()
        f=raw_input()
        zodiac=f[0:5]
        if zodiac=="*Edge":
            line=raw_input()
            zodiac=line[0:5]
            while zodiac!="*Quer":
                m=line.split()
                #print m
                #z=line[0]
                #x=line[2]
                #y=line[4]
                #if line!="*Queries":
                #vet.append(z)
                #vet.append(x)
                #vet.append(y)
                #print vet
                apoc.new_edge(m)
                #apoc.print_matriz_edge()
                #apoc.print_vertex_names()
                line=raw_input()
                zodiac=line[0:5]
        elif zodiac=="*Arcs":
            line=raw_input()
            zodiac=line[0:5]
            while zodiac!="*Quer":
                #line=raw_input()
                m=line.split()
                #z=line[0]
                #x=line[2]
                #y=line[4]
                #vet.append(z)
                #vet.append(x)
                #vet.append(y)
                #print m
                apoc.new_arc(m)
                line=raw_input()
                zodiac=line[0:5]
        else:
            #print "ERRO!"
            return None
            
        if line=="*Queries":
            line=raw_input()
            zodiac=line[0:3]
            #print zodiac
        while zodiac!='@':
            try:
                if zodiac=="get":
                    n=line.split()
                    #print n
                    ID_X=n[1]
                    apoc.locate(ID_X)
                    line=raw_input()
                    #print line
                    zodiac=line[0:3]
                elif zodiac=="del":
                    n=line.split()
                    ID_X=n[1]
                    apoc.kill_vertex(ID_X)
                    line=raw_input()
                    zodiac=line[0:3]
                elif zodiac=="viz":
                    n=line.split()
                    ID_X=n[1]
                    apoc.list_neighborhood(ID_X)
                    line=raw_input()
                    zodiac=line[0:3]
                elif zodiac=="con":
                    n=line.split()
                    ID_X=n[1]
                    ID_Y=n[2]
                    apoc.adjacency_test(ID_X,ID_Y)
                    line=raw_input()
                    zodiac=line[0:3]
                elif (zodiac=="kru") or (zodiac=="arv"):
                    n=line.split()
                    kruskal2(grafo)
                    line=raw_input()
                    zodiac=line[0:3]
                elif (zodiac=="top") or (zodiac=="ord"):
                    n=line.split()
                    apoc.topological_sort()
                    line=raw_input()
                    zodiac=line[0:3]
                elif (zodiac=="dij") or (zodiac=="men"):
                    n=line.split()
                    ID_X=n[1]
                    ID_Y=n[2]
                    apoc.dijkstra_path(ID_X,ID_Y)
                    line=raw_input()
                    zodiac=line[0:3]
                else:
                    #print "ERRO!"
                    return None
            except EOFError:
                #print "That's all folks"
                break
        

if __name__ == '__main__':
    apoc=grafo()
    ler_arq(apoc)
