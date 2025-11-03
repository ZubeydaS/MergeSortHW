import csv
import os
import sys

''''
CS 252 Merge Sort HW
Fall Semester 2026

Purpose:
  1. Test if student's mergesort.py works woth the COMPAS dataset
  2.Provide helpful feedback when code is incomplete 
  3.Guide students through implemtation step-by-step
  4. Check compatibility with real data strucrures 
'''
Class Tester:  
def __init__(self):
  self.student = None;

### Test 1: file checking -> can the student's files be imported?
  def test_file_import(self):
  print("TEST ! : Checking import file...")
  try:
      import mergesort
      self.student = mergesort 

    print "PASS: mergesort.py imported successfully"
    return True

  except ImportError:
    print("FAIL: mergesort.py not found in this directory")
    print("  Make sure mergesort.py is in the sme folder as this test file")
    return False
  except Exception as e:
    print(f" FAIL: Syntax error - (e)")
    print ("  Check for typos or missing colons in your mergesort.py")
    return False

### Test 2: Person class -> dpes the class structure exist?
def test_person_structure(self):
print(n\ TEST 2: Checking person class...")
try: 
  person = self.student.Person("Test", 1, 2, 3, 4)
  print("PASS: Person class structure exists")
  return True
except Exception as e:
print(f" FAIL: Cannot create Person - (e)")
print("  Check your Person class definition")
return False

### Test 3: Function choices -> are all required functions defined
def test_functions(self):
print("\n TEST 3: Checking functions...")
required_functions = ['come_before', 'merge', 'merge_sort', 'load_data']
missing_functions = []

for func in required_functions:
  if hasattr(self.student, func):
    print (f" {func}() is defined")
else:
    print(f"   {func}() is missing")
    missing_function.append(func)
  if not missing_function:
    print("PASS: All basic functions exist ")
    return True
  else:
    print(f"  FAIL: Missing functions: {missing_functions}")
    returns FALS

### Test 4: Main block -> does the main code structure esxist in the student's submission
 def test_main_block(self):
   
  print("\n  TEST 4: Checking code block")
try:
  with open('merge.py', 'r') as f:
    content = f.read()

if 'if __name__ == "__main__":'
    print("  PASS: Main block exists :)")
    return True
else:
  print("  FAIL: Main block missing")
  print("  Add: of __name__ == \"__main__\": to your file")
  return False
except:
  print"  Could not read file to check main block"
  return True

### Test 5: Data compatability -> creating test file
def test_data_compatibility(self):

print("\n TEST 5: Creating compatible test files")
with open('COMPAS Data - Sample Data.csv)
  print("n\  TEST 5: Creating compatible test files)
  writer.writerow(['name', 'decile_score', 'priors_count', 'total_days_jail', 'total_days_custody'])
  writer.writerow('[Michael Jackson', 8, 3, 45, 60])
  writer.writerow(['Bob Dylan', 2, 1, 10 ,15])
  writer.writerow(['Whitney Houston, 5, 2, 30, 40])
  writer.writerow(['Star Dust, 9, 4, 80, 100])
  writer.writerow(['Minnie Riperton',1, 0, 5, 8])

  print("  PASS: Created compatible_test.csv")
  print("  This file has the eact columns the homework needs :)")
  return True


          
### Test 6: Column mapping check -> critical compatibility check 
def test_column_mapping(self):
                   
print("  \n  TEST 6: Column Mapping Check (CRITICAL)")

print("  YOUR CSV HAS: 'total_days_jail', 'total_days_custody'")
print("  PERSON CLASS EXPECTS: ''")
print("  YOU MUST  MAP IN load_data():")
print("  total_days_in_jail = int(row['total_days_jail'])")
print("  total_days_in_custody = int(row['total_days_custody'])")

return True

### Test 7: Implementation progress -> what's actually working?
def test_implementation_progress(self):
                   
print("\n  Test 7: Implementation progress check")
progress = [] 
try:
  person = self.student.Person("Test", 1, 2, 3, 4)
if hasattr(person, 'name'):
  progress.append("  Person stores attributes")
else:
  progress.append("  Person needs attribute storage")

  if hasattr(person, 'new_decile'):
    progress_append("  Person has new_decile")
  else:
    progress.append("  Person needs new_decile calculation")

    except:
      progress.append("  Person class incomplete")

      try:
        Person = self.student.Person
        test_person = Person("Test", 1, 0, 0 ,0)
        result = self.student.comes_before(test_peerson, test_person, 'decile_score')
          if result is not None:
            progress.append("  comes_before implemented")
          else:
            progress.append("  comes_before needs implementation")
        except:
        progress.append(  Person class incomplete)
    try:
        Person = self.student.Person
        test_person = Person("Test", 1, 0, 0, 0)
    
        result = self.student.comes_bef0re(test_person, test_person, 'decile_score')
        progress.append("  comes_before implemented")
    else:
        progress.append("  comes_before needs implementation")
    except:
        progress.append("  comes_before not working")
    print("  Current Status:")
    for item in progress:
      print(f"  (item)")
Return true
      
### Test 8: Code and style organization
def test_code_style(self):
              
print(\n TEST8: Checking code style and organization...)
try:
  with open('mergesort.py', 'r') as f:
  content = f.read()

  style_notes = []

  if len(content) > 100:
    style_notes_apppend("Good code length")
  else:
    styles_notes.append("Minimal implementation")

  if content.count('#') > 5:
  style_notes.append("has comments: good documentation"):
  else:
    style_notes.append("Could use more comments to explain your logic :/")

  if 'getattr' in content:
    style_notes_append("Uses getattr: follows starter code suggestions")
  else:
    style_notes_append("Consider using getattr for flexible attribute access")
  print("  Style notes:")
  for note in style_notes:
      print(f"  {notes}")
    return True
  except:
    print("  Could not alalyze code style")
    return True

### Test 9: Homework guidance -> step-by-step help for the kiddos 
    def test_homework_guidance(self):
    print("  TEST 9: Step-by-Step Instructions if you're overwhelmed :)")
    # Step 1: Person class (most important and foundation for everything)         
    print("  1. PERSON CLASS (First Priority:)")
    print("  - Store all parameters as attributes")
    print("    self.name = name")
    print("    self.decile_score = decile_score")
    print("    etc...")
    print("  - Calculate new_decile using the formula:")
    print("    self.new_decile = 0.6*priots_count + 0.5*total_days_in_jail + 0.1*total_days_in_custody")
             
    # Step 2: load the data - critical for connecting the data to the code!
    print("\n  2. LOAD_DATA (Critical!)")
    print("  - Read CSV with csv.DictReader")
    print("  - Map the column names (also critical!")
    print("   row['total_days_jail'] -> total_days_in_jail")
    print("row['total_days_custody'] -> total_days_in_custody")
    print("  - Create Person objects and return list")
    # Step 3: comes_before - think about the logic of your algorithm
    print("\n  3. COMES_BEFORE (Comparison logic!)")
    print("    - Use getattr(a, key) to compare specified attributes")
    print("    - Handle ties with alphabetical name comparison")
    print("    - Return True if 'a' should come before 'b' for example")
    # Step 4: Merge :)
    print("\n  4. MERGE (combine sorted lists")
    print("    - Standard merge algorithm from class")
    print("    - Use comes_before for comparisons")
    print("    - Return merge sorted list")
    # Step 5: 
    print("\n   5. MERGE_SORT (Recursive Sorting!")
    print("     - Base case: if len(data) <=1, return data")
    print("     - Split list in half")
    print("     - Recursively sort each half")
    print("     - Merge the sorted halves. Ta-da! Mergesort :)")
    # STEP 6: Main (just putting all of this stuff together... whew)
    print("\n  6. MAIN (Complete Your File! - Finishing touches")
    print("    - Set filename to COMPAS data file")
    print("    - Load data using load_data()")
    print("    - Sort by decile_score and new_decile")
    print("    - Print both sorted lists for comparison!")
    
    return True

### Run all tests 
    def run_all_tests(self):
          
    print("=" * 60)
    print("CS 252: Algorithms - test_mergesort - Merge Sort Homework Tester - 9 Tests Total")
    print("=" * 60)
    print("Running compatibility check...")
    print()

  tests = [
    self.test_file_import,               # Test 1
    self.test_person_structure,          # Test 2
    self.test_functions,                 # Test 3            
    self.test_main_block,                # Test 4
    self.test_data_compatibility,        # Test 5
    self.test_column_mapping,            # Test 6
    self.test_implementation_progress,   # Test 7
    self.test_code_style,                # Test 8
    self.test_homework_guidance          # Test 9
    
  ]
  
  results = []
  for test in tests: 
    try:
         result = test()
         results.append(result)
        except Exception as e:
         print(f"  Test error: {e}")
         results.append(False)

  print("\n" + "=" * 60)
  print(COMPATIBILITY CHECK/TESTS COMPLETE :D)
  print("=" * 60)

  passed = sum(results)
  total = len(results)

  print(f"Compatibility Score: {parsed}/{total}");

  if passed == total:
         print("Fully compatible :) You're good")
  else:
         print("Partially compatible :/ check the warning above!")
  print("\n  NEXT STEPS BROSKI")
  print("1. Implement Person class with new_decile calculation")
  print("2. Implement load_data")
  print("3. Test with: python mergesort.py COMPAS Data - Sample Data.csv")
  print("4. Complete other functions step by step")
  print("5. Run the tests again to check your progress")
  print("6. Complete README.md (including Reflection) for Full Credit")
           
# Main execution 
def main():
  tester + Tester()
  success = tester.run_all_tests()
  sys_exit(0 if success else 1)

# run only whenb file is executed directly
if __name__ == "__main__":
  main()
  


