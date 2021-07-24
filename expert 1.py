class notebook:
    def __init__(self):
        self.name=[]
        self.note=[]

    def set_name(self,name):
        self.name.append(name)
    def set_note(self,note):
        newnote=note
        self.note.append(newnote)
        return newnote
    def get_name(self):
        return self.name  
    def get_note(self):
        return self.note


op=notebook()
op.set_name("OPP")
op.set_note("PYTHON IS")
print("__________")
op.set_name("OPP")
op.set_note("JAVA IS")
print("__________")
op.set_name("OPP")
op.set_note("C++ IS")
print("SUBJECT 1: ",op.name[0],"\nNOTES 1 :  ",op.note[0])
print("\nSUBJECT 1: ",op.name[1],"\nNOTES 1 :  ",op.note[1])
print("\nSUBJECT 2: ",op.name[2],"\nNOTES 2 :  ",op.note[2])


  


  



