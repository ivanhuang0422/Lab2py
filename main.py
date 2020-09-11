# Author: Yu-Hsiang, Huang ykh5222@psu.edu
# Collabrator: Wenjun Ju wkj5070@psu.ed
# Collabrator: Aracind Hariprased azh5899@psu.edu
# Collabrator: Abishek Venkataraman apv5314@psu.edu
# Section: 4
# Breakout: 11
def getLetterGrade(grade):
    return "A","B","B-","C+", "C", "D", "F"
def run():
  grade=float(input("Enter your CMPSC 131 grade: "))
  if grade>=93.0:
    print(f"Your letter grade for CMPSC 131 is A.")
  elif grade>=90.0:
    print(f"Your letter grade for CMPSC 131 is A-.")
  elif grade>=87.0:
    print(f"Your letter grade for CMPSC 131 is B+.")
  elif grade>=83.0:
    print(f"Your letter grade for CMPSC 131 is B.")
  elif grade>=80.0:
    print(f"Your letter grade for CMPSC 131 is B-.")
  elif grade>=77.0:
    print(f"Your letter grade for CMPSC 131 is C+.")
  elif grade>=70.0:
    print(f"Your letter grade for CMPSC 131 is C.")
  elif grade>=60.0:
    print(f"Your letter grade for CMPSC 131 is D.")
  else:
    print(f"Your letter grade for CMPSC 131 is F.")
if __name__=="__main__":
  run()