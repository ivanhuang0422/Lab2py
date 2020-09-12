# Author: Yu-Hsiang, Huang ykh5222@psu.edu
# Collabrator: Wenjun Ju wkj5070@psu.ed
# Collabrator: Aracind Hariprased azh5899@psu.edu
# Collabrator: Abishek Venkataraman apv5314@psu.edu
# Section: 4
# Breakout: 11

def getLetterGrade(grade):
  if grade>=93.0:
    return "A"
  elif grade>=90.0:
    return "A-"
  elif grade>=87.0:
    return "B+"
  elif grade>=83.0:
    return "B"
  elif grade>=80.0:
    return "B-"
  elif grade>=77.0:
    return "C+"
  elif grade>=70.0:
    return "C"
  elif grade>=60.0:
    return "D"
  else:
    return "F"

def run():
  grade=float(input("Enter your CMPSC 131 grade: "))
  print(f"Your letter grade for CMPSC 131 is {getLetterGrade(grade)}.")

if __name__=="__main__":
  run()