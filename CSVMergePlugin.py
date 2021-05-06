import sys
import numpy
import random
import PyPluMA

# Scaling is done to make median=1
class CSVMergePlugin:
   def input(self, filename):
      self.myfile = filename

   def run(self):
      filestuff = open(self.myfile, 'r')

      firstline = filestuff.readline().strip()
      if (len(PyPluMA.prefix()) != 0):
         firstline = PyPluMA.prefix() + "/" + firstline
      firstfile = open(firstline, 'r')

      # Use first file to get indices
      self.firstline = firstfile.readline().strip()
      lines = []
      for line in firstfile:
         lines.append(line.strip())

      self.m = len(lines)
      self.samples = []
      self.bacteria = self.firstline.split(',')
      if (self.bacteria.count('\"\"') != 0):
         self.bacteria.remove('\"\"')

      self.n = len(self.bacteria)
      self.ADJ = []#numpy.zeros([self.m, self.n])
      i = 0
      for i in range(self.m):
            self.ADJ.append([])
            contents = lines[i].split(',')
            self.samples.append(contents[0])
            for j in range(self.n):
               #print contents[j+1]
               value = contents[j+1].strip()#float(contents[j+1].strip())
               #print self.ADJ[i][j]
               self.ADJ[i].append(value)#[j] = value
            i += 1

 
      for line in filestuff:
         myline = line.strip()
         if (len(PyPluMA.prefix()) != 0):
            myline = PyPluMA.prefix() + "/" + myline
         newfile = open(myline, 'r')
         firstline = newfile.readline().strip()
         bac = firstline.split(',')
         if (bac.count('\"\"') != 0):
            bac.remove('\"\"')
         lines = []
         for line2 in newfile:
            lines.append(line2.strip())
         for line2 in lines:
            contents = line2.split(',')
            bac2 = contents[0]
            if (bac2 in self.samples):
               x = self.samples.index(bac2)
            else:
               self.ADJ.append([])
               for i in range(0, self.n):
                  self.ADJ[len(self.ADJ)-1].append(0)
               x = len(self.ADJ)-1
               self.m += 1
               self.samples.append(bac2)
            for j in range(1, len(contents)):
               if (bac[j-1] in self.bacteria):
                  #print("FOUND "+bac[j-1]+", NOT APPENDING")
                  #xxx = input()
                  y = self.bacteria.index(bac[j-1])
                  #print(x)
                  #print(len(self.ADJ))
                  #print(y)
                  #print("ROW LENGTH "+str(x))
                  #print(len(self.ADJ[x]))
                  #print(j)
                  #print(len(contents))
                  #print(len(self.bacteria))
                  #print(self.n)
                  self.ADJ[x][y] = contents[j].strip()
               else:
                  self.bacteria.append(bac[j-1])
                  #print("APPENDING: "+str(len(self.bacteria)))
                  #xxx = input()
                  self.n += 1
                  #print(self.n)
                  for row in range(len(self.ADJ)):
                     self.ADJ[row].append(0.0)
                  self.ADJ[x][len(self.ADJ[x])-1] = contents[j].strip()

  
   def output(self, filename):
      filestuff2 = open(filename, 'w')
      #filestuff2.write(self.firstline+"\n")
      filestuff2.write("\"\",")
      for i in range(len(self.bacteria)):
         filestuff2.write(self.bacteria[i].strip())
         if (i != len(self.bacteria)-1):
            filestuff2.write(',')
         else:
            filestuff2.write('\n') 
      for i in range(len(self.samples)):
         filestuff2.write(self.samples[i]+',')
         for j in range(len(self.ADJ[i])):
            #if (j != 0 and (float(self.ADJ[i][j]) != 0) and (float(self.ADJ[i][j]) <= 1e-4)):
            #   print(float(self.ADJ[i][j]))
            filestuff2.write(str(self.ADJ[i][j]))
            if (j < len(self.ADJ[i])-1):
               filestuff2.write(",")
            else:
               filestuff2.write("\n")


