import csv
import os
import sys

''''
CS 252 Merge Sort HW
Fall Semester 2026

Purpoaw:
  1. Test if student's mergesort.py works woth the COMPAS dataset
  2.Provide helpful feedback when code is incomplete 
  3.Guide students through implemtation step-by-step
  4. Check compatibility with real data strucrures 
'''
Class Tester:  
def __init__(self):
  self.student = None;

### Test 1: file checking -> can the student's files be im[prted?
  print("TEST ! : Checking import file...")
  try:
      import mergesort
    self.student = mergesort 
print "PASS: mergesort.py imported successfully"
return True
except ImportError:
print("FAIL: : :"mergesort.py" not found in this dictionary")
print("Make sure mergesort.py is in the same folder as this test file")
  return False:
  except Exception as e:
  print("FAIL: mergesort.py not found in this directory")
  print("  Make sure mergesort.py is in the sme folder as this test file")
    return False;
    except Exception as e:
    print("f FAIL: Syntax error - (e)")
    print ("  Check for typos or missing colons in your mergesort.py")


### Test 2: 

### Test 3:

### Test 4: 

### Test 5:  

### Test:6 

### Test 7: 

### Test 8: 

### Test 9: 

### Test 10: 

### Test 11: 

# Main execution 
def main():
  tester + Tester()
  success = testwer.run_all_tests()
  sys_exitexit(0 if success else 1)

# run only whenb file is executed directly
if __name__ == "__main__":
  main()
  
