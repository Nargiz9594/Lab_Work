class Computation:
    def __init__ (self):
        pass


#Factorial
    def factorial(self,n):
        b = 1
        for i in range (1, n + 1):
            b = b * i
        return b


#Sum of the first n numbers
     def sum(self, n):
         a=1
         for i in range (1, n+1):
             return a


 #Primality test of a number

         def testPrim(self, n):
             a=0
             for i in range(1,n+1):
                 if(n% i==0):
                     a=a+1
                     if(a==2):
                         return True
                     else:
                         return False


#Primality test of two integers
def testPrims(self, n,m):
    commonDiv = 0
    for i in range(1, n + 1):
        if (n % i == 0 and m % i == 0):
            commonDiv = commonDiv + 1
    if commonDiv == 1:
        print("The numbers", n, "and", m, "are co-primes")
    else:
        print("The numbers", n, "and", m, "are not co-primes")

#TableMult
 def tableMult (self, k):
        for i in range (1,10):
            print (i, "x", k, "=", i * k)

#AllTableMults
 def allTables (self):
        for k in range (1,10):
            print ("nthe multiplication table of:", k, "is:")
            for i in range (1,10):
                print (i, "x", k, "=", i * k)


#ListDiv

ef listDiv (self, n):
        # initialization of the list of divisors
        lDiv = []
        for i in range (1, n + 1):
            if (n% i == 0):
                lDiv.append (i)
        return lDiv

#ListDivPrim

def listDivPrim(self, n):
    # initialization of the list of divisors
    lDiv = []
    for i in range(1, n + 1):
        if (n % i == 0 and self.testPrim(i)):
            lDiv.append(i)
    return lDiv



