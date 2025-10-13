import csv 

# A class to hold each row of data
class Person: 
  def __init__(self, name, decile_score, priors_count, total_days_in_jail, total_days_in_custody): 
    # TODO: store the name, decile_score, priors_count, total_days_in_jail, and total_days_in_custody as attributes
    # TODO: create a new attribute called new_decile that uses the formula
    # This score represents a simplified model of how likely someone is to reoffend.
    pass
    

# Comparison function: decide if "a" should come before "b"   
def comes_before(a, b, key):
  # TODO: use getattr() to access the attribute given by key
  # TODO: return True if a should come before b when sorting by 'key'
  # If values are equal, use alphabetical order of names as a tiebreaker
  pass
   

# Merge two sorted halves into one sorted list
def merge(left, right, key): 
  # TODO: implement the standard merge step from merge sort
  # Return the merged result
  pass
  

# Recursive merge sort 
def merge_sort(data, key):
  # TODO: implement recursive merge sort
  # Base case: if the list length is <= 1, return it
  # Recursive case: split the list in half, call merge_sort on each half
  # Merge the two halves using the merge() function and return the result
  pass


# Load in data from CSV  
def load_data(filename): 
  records = []
  with open(filename, newline='') as csvfile: 
    reader = csv.DictReader(csvfile)
    for row in reader: 
      # TODO: create a Person object using values from the row
      # Make sure to read:
      #   name, decile_score, priors_count, total_days_in_jail, total_days_in_custody
      # Append each new Person object to records
      pass
  # TODO: return the records list
  pass
  


if __name__ == "__main__": 
  # TODO: set filename to the CSV file you were provided
  filename = 

  # TODO: load the data from the CSV
  people = 

  # TODO: sort the data twice:
  #   (1) once by "decile_score" from the dataset
  #   (2) once by your computed "new_decile"
  sorted_by_data_decile = 
  sorted_by_student_decile = 

  # TODO: print both sorted lists (names and their scores)
  # Example output line:
  # print(person.name, person.decile_score, person.new_decile)
  
  # TODO: compare the two sorted outputs and briefly comment (IN GOOGLE DOC)
  # on any differences between rankings under the two scoring systems
  pass
