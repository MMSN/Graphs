#!/usr/bin/env python
# -*- coding: latin1 -*-
import time
caminho=[]

class grafo:
    
    def __init__(self):
        global caminho
        self.matriz_edge={};
        self.name=['X']*300;
        self.count=0;
        self.max_count=300;
        self.dim=[300,300]
        self.ID=[None]*300
        self.direcionado = 0
        #for i in range(self.dim[0]):
        #    self.name[i]="X"
        
        #for lin in range(self.dim[0]):                #a intenção
         #   for col in range(self.dim[1]):            #era zerar
          #      self.matriz_edge.get((lin, col), 0),  #a matriz

    def new_vertex(self,pos_X,name_vertex):
        if (self.count == (self.max_count-1)):
            self.increasing_space()
        pos=self.search_pos()
        if (self.count > self.max_count) or (pos==-1):
            return 1
        else:
            if pos!=-1:
                if self.name[pos] == 'X':
                    self.name[pos]=name_vertex
                    self.ID[pos]=pos_X
                    #print self.ID[pos]
                    if(self.count<self.max_count):
                        self.count=self.count+1
                        #print self.count
                        #print "NOVO VERTICE"
                    return 0
            else:
                #print "SEM NOVO VERTICE"
                print self.count
                return 1
    
    def search_pos(self):
        for i in range(self.max_count):
            if self.name[i]=='X':
                return i
        #print "No espace for new vertex"
        return -1
    
    def search_name_pos(self,x):
        for i in range(self.max_count):
            if self.name[i]==x:
                return i
        #print "No espace for new vertex"
        return -1
    
    def find_for_id(self,num_x):
        for i in range(self.count):
            if self.ID[i]==num_x:
                return i
        return -1
        
    def find_for_path(self,x):
        #print x
        for i in range(self.count):
            if int(self.ID[i])==int(x):
                return i
        return -9999
    
    def kill_vertex(self,ID_X):
        for i in range(self.count):
            if self.ID[i]==ID_X:
                self.ID[i]=None
                self.name[i]='X'
                for j in range(self.count):
                    self.matriz_edge[i,j]=0
                    self.matriz_edge[j,i]=0
                #self.count=self.count-1
                print ("{\"delete\":{\"ID\":%d, \"resposta\":\"sucesso\"}}")%(int(ID_X))
                return 0
        print ("{\"delete\":{\"ID\":%d, \"resposta\":\"falha\"}}")%(int(ID_X))
        return 0
    
    def new_edge(self,vet):
        a=self.find_for_id(vet[0])
        b=self.find_for_id(vet[1])
        if (a!= -1) and (b!= -1):
            self.matriz_edge[a,b]=int(vet[2])
            self.matriz_edge[b,a]=int(vet[2])
            #print "NOVO EDGE"
            return 0
        else:
            #print "SEM NOVO EDGE"
            return 1
            
    def new_arc(self,vet):
        self.direcionado = 1
        a=self.find_for_id(vet[0])
        b=self.find_for_id(vet[1])
        if (a!= -1) and (b!= -1):  
            self.matriz_edge[a,b]=int(vet[2])
            #print "Successful New Arc"
            return 0
        else:
            #print "Unsuccessful"
            return 1

    def kill_edge(self):
        a=(raw_input("Type the name of the vertex: "))
        posA=self.search_name_pos(a)
        b=(raw_input("Type the name of the vertex: "))
        posB=self.search_name_pos(b)
        if (posA!= -1) and (posB!= -1):  
            self.matriz_edge[posA,posB]=0
            self.matriz_edge[posB,posA]=0
            print "Successful"
            return 0
        else:
            print "Unsuccessful"
            return 1

    def adjacency_test(self,ID_X,ID_Y):
        posA=self.find_for_id(ID_X)
        posB=self.find_for_id(ID_Y)
        if (posA!= -1) and (posB!= -1): 
            if(self.matriz_edge.get((posA,posB))!=0):
                print ("{\"conexao\":{\"ID1\":%d, \"ID2\":%d, \"resposta\":\"sucesso\", \"conexao\":\"sim\"}}")%(int(ID_X),int(ID_Y))
                return 0
            else:
                print ("{\"conexao\":{\"ID1\":%d, \"ID2\":%d, \"resposta\":\"sucesso\", \"conexao\":\"nao\"}}")%(int(ID_X),int(ID_Y))
                return 1
        else:
            print ("{\"conexao\":{\"ID1\":%d, \"ID2\":%d, \"resposta\":\"falha\", \"conexao\":\"\"}}")%(int(ID_X),int(ID_Y))
            return 1

    def list_neighborhood(self,ID_X):
        list=[]
        posA=self.find_for_id(ID_X)
        if posA!= -1:
            for i in range(self.count):
                #print i
                if (self.matriz_edge.get((posA,i))>0):
                    list.append(int(self.ID[i]))
                    #print self.matriz_edge.get((posA,i),1)
            print ("{\"vizinhos\":{\"ID\":%d, \"resposta\":\"sucesso\", \"vizinhos\":%s}}")%(int(ID_X),list)
            return list
        else:
            print ("{\"vizinhos\":{\"ID\":%d, \"resposta\":\"falha\", \"vizinhos\":[]}}")%(int(ID_X))
            return 1

    def print_matriz_edge(self):
        for lin in range(self.count):
            for col in range(self.count):
                print self.matriz_edge.get((lin, col), 0),
            print "\n"

    def print_vertex_names(self):
        for i in range(self.count):
            print self.name[i]
            print " "
            
    def locate(self,ID_X):
        for i in range(self.count):
            if self.ID[i]==ID_X:
                #print"{vertice:{ID:%d, dado:%s, resposta:sucesso}}"%(int(self.ID[i]), self.name[i])
                print ("{\"vertice\":{\"ID\":%d, \"dado\":%s, \"resposta\":\"sucesso\"}}")%(int(self.ID[i]), self.name[i])
                return 1
        print ("{\"vertice\":{\"ID\":%d, \"dado\":\"\", \"resposta\":\"falha\"}}")%(int(self.ID[i]))
        return -1
    
    def increasing_space(self):
        new_space=self.max_count*2
        self.max_count=new_space;
        self.dim=[new_space,new_space]
        i = self.count
        for i in range(self.max_count):
            self.name.append('X')
            self.ID.append(0)
    
    def topological_sort(self):
        if self.direcionado == 1:
            
            #print("TOPO")
            solution=[]
            dic=self.matriz_edge.copy()
            no_arcs=[]
            for i in range(self.count):
                count = 0
                for j in range(self.count):
                    if(dic.get((j,i))>0):
                        count=count+1
                if count == 0:
                    no_arcs.append(int(self.ID[i]))
            #self.print_matriz_dic(dic)
            no_arcs.sort()
            #print no_arcs
            aux=[]
            while len(no_arcs) > 0:
                #print ":" 
                #print no_arcs
                aux=[]
                #self.print_matriz_dic(dic)
                vertex=self.find_for_path(no_arcs.pop(0))
                #print vertex
                solution.append(int(self.ID[vertex]))
                #print solution
                for i in range(self.count):
                    if(dic.get((vertex,i))>0):
                        dic[vertex,i]=0
                        omg=i
                        count2=0
                        for j in range(self.count):
                            if dic.get((j,omg))>0:
                                count2=count2+1
                        if count2 == 0:
                            #no_arcs.append(int(self.ID[i]))
                            aux.append(int(self.ID[i]))
                            #print "!"
                            #print aux
                aux.sort()
                no_arcs = no_arcs + aux
                    
            if (dic.has_key("1"))== True:
                print ("{\"ordemtop\":[]}")
                return None
            else:
                #print "Nao ha arestas"
                #print solution
                print ("{\"ordemtop\":%s}")%(solution)
                return solution
        else:
            print ("{\"ordemtop\":[]}")
            return None
            
    def print_matriz_dic(self,dic):
        for lin in range(self.count):
            for col in range(self.count):
                print dic.get((lin, col), 0),
            print "\n"
            
    def dijkstra(self,id_x):
        list_dist=[]
        INFINITY=1000000
        for i in range(self.count):
            list_dist.append(INFINITY)
        source=self.find_for_id(id_x)
        list_dist[source]=0
        Q=[]
        print list_dist
        for i in range(self.count):
            if(self.ID[i]!=None):
                Q.append(self.ID[i])
        #print Q
        while(len(Q)>0):
            #print list_dist
            adj=[]
            x=Q[0]
            #print x
            y=self.find_for_id(x)
            if(list_dist[y]==INFINITY):
                break;
                print "M"
            Q.pop(0)
            for i in range(self.count):
                if (self.matriz_edge.get((y,i))>0):
                    #adj.append(self.ID[i])
            #for i in range(len(adj)):
                #w=self.find_for_id(adj[i])
                    total_dist = list_dist[y]+self.matriz_edge[y,i]
                    #print total_dist
                    if total_dist < list_dist[i]:
                        list_dist[i]=total_dist
        print list_dist
        return list_dist

    def dijkstra_path(self,id_x,id_y):
        list_dist=[]
        previous_list=[]
        INFINITY=1000000
        for i in range(self.count):
            list_dist.append(INFINITY)
            previous_list.append(-INFINITY)
        source=id_x
        target=id_y
        
        list_dist[self.find_for_id(source)]=0
        Q=[source]
        check=[]
        while(len(Q)>0):
            x=Q[0]
            y=self.find_for_id(x)
            temp = list_dist[y]
            for i in range(1,len(Q)):
                if list_dist[self.find_for_id(Q[i])] < temp:
                    temp= list_dist[self.find_for_id(Q[i])]
                    x=Q[i]
                    y=self.find_for_id(x)
            check.append(x)
            Q.remove(x)
            for i in range(self.count):
                if ((self.matriz_edge.get((y,i))>0) and not (self.ID[i] in check)):
                    if(not (self.ID[i] in Q)):
                        Q.append(self.ID[i])
                    total_dist = list_dist[y]+self.matriz_edge[y,i]
                    if total_dist < list_dist[i]:
                        list_dist[i]=total_dist
                        previous_list[i]=int(self.ID[y])
        
        target=self.find_for_id(id_y)
        #print previous_list
        if(list_dist[target]==INFINITY):
            print ("{\"menorcaminho\":{\"ID1\":%d, \"ID2\":%d, \"caminho\":[],\"custo\":0}}")%(int(id_x),int(id_y))
            return None
        
        
        self.teste_caminho(id_x,id_y,previous_list)
        
        #print caminho
        #print caminho[::-1]
        #print list_dist
        #print previous_list
        print ("{\"menorcaminho\":{\"ID1\":%d, \"ID2\":%d, \"caminho\":%s,\"custo\":%d}}")%(int(id_x),int(id_y),caminho[::-1],int(list_dist[self.find_for_id(id_y)]))
        return list_dist
        
    def teste_caminho(self,inicio,fim,distancias):
        try:
            global caminho
            #print inicio, fim, distancias
            if int(inicio)==int(fim):
                caminho.append(int(inicio))
                #print current_path
                #print current_path.reverse()
                return True
            else:
                caminho.append(int(fim))
                final=self.find_for_path(fim)
                #print final
                meio=distancias[int(final)]
                teste=self.teste_caminho(inicio,meio,distancias)
        except IndexError:
            return None
