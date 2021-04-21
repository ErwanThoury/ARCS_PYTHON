from collections import namedtuple
import os

DBInfos = namedtuple("infos", ['dbname', 'dbpath', 'dbfile'])
dbfiles =".index.db"

class NazeDB :
    
    
    def __init__(self, dbname=None):
        self.dbname = dbname 
        #if dbname is in listdb:
            #self.open(dbname)
        #else:
            #créer la bdd puis 
            #self.open(dbname)              
    def open(self, dbname: str):
        
        fichier = self.dbinfos.dbpath + "/" +dbfiles
        print(fichier)
        
        reader = 1
        
        return reader
    @property
    def dbinfos(self) -> DBInfos:
    	dbnom = self.dbname
    	a = self.listdb()
    	informations = DBInfos._make(["null", "null", ".index.db"])
    	#print(type(informations))
    	for i in a:
    	    if i.dbname == dbnom:
    	        informations = i
    	             
    	return informations
    
    @staticmethod
    def listdb() -> [DBInfos]:
        
        lstDB = []
        for root, directories, files in os.walk('./'):
            if dbfiles in files:
                fin = root.split("/")
                fin = fin[-1]
                d = DBInfos._make([fin, root, ".index.db"])
                lstDB.append(d)
        #print("IIIIIICCCCCCCIIIIIII") 
        return lstDB
        
""" 
dbname = "pouet"
dbfiles = ".index.db"
if dbname != None:   

    for root, directories, files in os.walk('./'):        
        if dbname in directories:         
            for directory in directories:
            
                if directory == dbname:
                    chemin = root+'/'+directory+"/"
                    #print(chemin)
                    #print("il y a les fichiers",files)
                    for rootB, dirsB, filesB in os.walk(chemin):                        
                        if (dbfiles in filesB) and (rootB == chemin):
                            print("C'est bien une bdd!")
                            rootdbfiles = chemin + dbfiles
                            
                            fw = open(rootdbfiles, "w")
                            with fw as f:
                                f.write("bip")
                             
                            fr = open(rootdbfiles, "r")
                            
                            with fr as frr:
                                reader = frr.read()
                                print(reader)
                            
                            return fr
"""                            



