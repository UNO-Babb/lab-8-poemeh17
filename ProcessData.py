#ProcessData.py
#Name:
#Date:
#Assignment:

import random

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  yearABR = {"Freshman": "FR", "Sophomore" : "SO", "Junior": "JR", "Senior": "SR"}


  #Process each line of the input file and output to the CSV file
  #line = inFile.readline()
  for line in inFile:
    data = line.split()
    first = data[0]
    last = data[1]
    major = data [6]
    idNum = data [3]
    year = data [5]
  #print(data)
    year = yearABR.get(year.capitalize(), year [:2].upper())
    student_id = makeID(first, last, idNum)
    majorYear = major [:3].upper() + "-" + year
    output = last  + " "+ first + ", " + student_id +", " +  majorYear + "\n"
    outFile.write(output)
    #print(student_id)
    #print(output)

  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

def makeID(first, last, idNum):
  #print(first, last, idNum)
  idLen = len(idNum)

  while len(last) < 5 :
    last = last + "X"

  id = first[0] + last +idNum[idLen - 3: ]
  #print(id)
  return id
  

if __name__ == '__main__':
  main()
