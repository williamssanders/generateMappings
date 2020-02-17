class Application:
    def __init__(self,key,name,rate,perturbedRate,computeName,mapping):
        self.key = key
        self.name = name
        self.rate = rate
        self.perturbedRate = perturbedRate
        self.computeName = computeName
        self.mapping = mapping

    def get_key(self):
        return self.key

    def set_key(self,key):
        self.key = key

    def get_name(self):
        return self.name
    
    def set_name(self,name):
        self.name = name

    def get_rate(self):
        return self.rate

    def set_rate(self,rate):
        self.rate = rate

    def get_perturbedRate(self):
        return self.perturbedRate

    def set_perturbedRate(self,perturbedRate):
        self.perturbedRate = perturbedRate

    def get_computeName(self):
        return self.computeName

    def set_computeName(self,computeName):
        self.computeName = computeName

    def get_mapping(self):
        return self.mapping
    
    def set_mapping(self,mapping):
        self.mapping = mapping
    
    def print_values(self):
        #print(str(self.key) + "," + self.name + "," + str(self.rate) + "," + str(self.perturbedRate) + "," + self.computeName + "," + self.mapping)
        return(str(self.key) + "," + self.name + "," + str(self.rate) + "," + str(self.perturbedRate) + "," + self.computeName + "," + self.mapping)

    def definition(self):
        #print(self.name + " = (" + self.computeName + ", infty)." + self.name + ";")
        return(self.name + " = (" + self.computeName + ", infty)." + self.name + ";")

    def string_rate(self):
        return("r" + str(self.key) + " = " + str(self.rate) + ";")
        
    def string_perturbedRate(self):
        return("p" + str(self.key) + " = " + str(self.perturbedRate) + ";")