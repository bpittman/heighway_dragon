import sys
sys.path.append("./pygooglechart")
import pygooglechart as pgc
import matplotlib.pyplot as plt

def generate_string(iterations):
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

def generate_coords(string):
   facing = 90
   xcoords = [0]
   ycoords = [0]
   for c in string:
      if c == "a" or c == "b": continue
      elif c == "L":
         facing += 90
         facing = normalize(facing)
      elif c == "R":
         facing -= 90
         facing = normalize(facing)
      elif c == "F":
         if facing > 270: print facing
         if facing < 0: print facing
         if facing == 0:
            xcoords.append(xcoords[-1]+1)
            ycoords.append(ycoords[-1])
         elif facing == 90:
            xcoords.append(xcoords[-1])
            ycoords.append(ycoords[-1]+1)
         elif facing == 180:
            xcoords.append(xcoords[-1]-1)
            ycoords.append(ycoords[-1])
         elif facing == 270:
            xcoords.append(xcoords[-1])
            ycoords.append(ycoords[-1]-1)
   return xcoords, ycoords

def pgc_plot(coords):
   x = coords[0]
   y = coords[1]
   chart = pgc.XYLineChart(500, 500,
                       x_range=(min(x), max(x)),
                       y_range=(min(y), max(y)))
   chart.add_data(x)
   chart.add_data(y)
   #after about D(8) the url gets too long...
   #print len(chart.get_url())
   chart.download('output.png')

def plt_plot(coords):
   plt.plot(coords[0],coords[1])
   plt.show()

def normalize(x):
   while x >= 360: x -= 360
   while x < 0: x += 360
   return x

if __name__ == "__main__":
   #print "D(0) =", generate_string(0)
   #print "D(1) =", generate_string(1)
   #print "D(2) =", generate_string(2)
   plt_plot(generate_coords(generate_string(15)))
