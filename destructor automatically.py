class demo:
    count=0 #here count is a static /class variable 
    def __init__(self):
        self.value=1 #object/instatnce/nonstatic variable

demo.count=1
print(demo.count)   #class variable can be accesed using class name and can be cahngd by class variable 
d=demo()
d.value=0
print(d.value)       #non-static variable or instance can be accessed by object name and can be cahnged by object name



