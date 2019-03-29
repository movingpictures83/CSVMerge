import sys
import numpy
import random

# Scaling is done to make median=1
class CSVMergePlugin:
   def input(self, filename):
      self.myfile = filename

   def run(self):
      filestuff = open(self.myfile, 'r')

      firstline = filestuff.readline().strip()
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
      #print "M: ", self.m
      #print "N: ", self.n
      for i in range(self.m):
            self.ADJ.append([])
            contents = lines[i].split(',')
            self.samples.append(contents[0])
            for j in range(self.n):
               #print contents[j+1]
               value = float(contents[j+1].strip())
               #print self.ADJ[i][j]
               self.ADJ[i].append(value)#[j] = value
            i += 1

 
      for line in filestuff:
         #print "READING FILE ", line.strip()
         newfile = open(line.strip(), 'r')
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
            x = self.samples.index(bac2)
            for j in range(1, len(contents)):
               y = self.bacteria.index(bac[j-1])
               self.ADJ[x][y] = float(contents[j])


  
   def output(self, filename):
      filestuff2 = open(filename, 'w')
      filestuff2.write(self.firstline+"\n")
      
      for i in range(self.m):
         filestuff2.write(self.samples[i]+',')
         for j in range(self.n):
            filestuff2.write(str(self.ADJ[i][j]))
            if (j < self.n-1):
               filestuff2.write(",")
            else:
               filestuff2.write("\n")



