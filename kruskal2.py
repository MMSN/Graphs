#!/usr/bin/env python
# -*- coding: latin1 -*-

import classGRAFO_definitiva
from classGRAFO_definitiva import *

class kruskal2(grafo):
    
    def __init__(self,grafo):
        self.parents=[None]*grafo.count
        #print self.parents
        self.kruskal_algoritmo(grafo)
    
    def kruskal_algoritmo(self,grafo):
        if grafo.direcionado == 1:
            print ("{\"arvoreminima\":{\"arestas\":[], \"custo\":0}}")
            return None
        a=self.crescent_edge(grafo)
        a.sort()
        for i in range(grafo.count):
            #print i
            self.make_set(i,grafo)
        T=[]
        custo = 0
        #print grafo.count
        while len(T) < (grafo.count-1):
            #print a
            e=a.pop(0)
            ajudante = e
            #print e
            #for i in range(grafo.count):
             #   for j in range(grafo.count):
              #      if grafo.matriz_edge.get((i,j))==e:
               #         u=i
                #        v=j
                 #       break
            coordenadas = ajudante[1]
            valor = ajudante[0]
            u = coordenadas[0]
            v = coordenadas[1]
            u_set=self.find(u,grafo)
            v_set=self.find(v,grafo)
            if u_set != v_set:
                custo += valor
                aux=[]
                self.merge(u_set,v_set,grafo)
                aux.append(int(grafo.ID[u]))
                aux.append(int(grafo.ID[v]))
                T.append(aux)
        if len(T) < grafo.count-1:
            print ("{\"arvoreminima\":{\"arestas\":[], \"custo\":0}}")
            return None
        print ("{\"arvoreminima\":{\"arestas\":%s, \"custo\":%d}}")%(T,custo)
        return None
        #print "Mateus"
        #print T
        #return None
                    
    def find_value(self,grafo,val):
        coordenates=[]
        for lin in range(grafo.count):
                for col in range(grafo.count):
                    if (grafo.matriz_edge.get((lin, col)) == val):
                        coordenates.append(lin)
                        coordenates.append(col)
                        #print "MT"
                        #print coordenates
                        return coordenates
    
    def list_vertex(self,grafo):
        list_vertex=[]
        list_aux=[]
        for i in range(grafo.count):
            list_aux.append(i)
            list_aux.append(i)
            list_vertex.append(list_aux)
            list_aux=[]
        #print list_vertex
        return list_vertex
        
    
    def crescent_edge(self,grafo):
        edge_list=[]
        for lin in range(grafo.count):
            for col in range(grafo.count):
                aux=[]
                if (grafo.matriz_edge.get((lin, col), 0)>0) and (col>lin):
                    aux.append(grafo.matriz_edge.get((lin, col), 0))
                    aux.append([lin,col])
                    edge_list.append(aux)
        edge_list.sort
        #print edge_list
        return edge_list
    
    def make_set(self,x,grafo):
        #print x
        self.parents[x]=x
        
    def find(self,x,grafo):
        if self.parents[x]==x:
            return x
        else:
            return self.find(self.parents[x],grafo)
    
    def merge(self,u,v,grafo):
        uRoot=self.find(u,grafo)
        vRoot=self.find(v,grafo)
        self.parents[uRoot]=vRoot
