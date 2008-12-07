def heighway_dragon(iterations):
   a = "aRbFR"
   b = "LFaLb"
   D = "Fa"

   #a possible optimization might be to store the indices
   #of the new a's and b's as we add them, to use for the
   #next pass.
   for i in xrange(iterations):
      for j in xrange(len(D)-1,-1,-1):
         if D[j] == "a":
            D = D[:j] + a + D[j+1:]
         elif D[j] == "b":
            D = D[:j] + b + D[j+1:]
   return D

if __name__ == "__main__":
   print "D(0) =", heighway_dragon(0)
   print "D(1) =", heighway_dragon(1)
   print "D(2) =", heighway_dragon(2)
