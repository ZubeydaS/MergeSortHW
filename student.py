import csv

# class to hold each row of data
class Person: 
    def __init__(self, name, decile_score, priors_count, total_days_in_jail, total_days_in_custody): 
        self.name = name
        self.decile_score = int(decile_score)
        self.priors_count = int(priors_count)
        self.total_days_in_jail = int(total_days_in_jail)
        self.total_days_in_custody = int(total_days_in_custody)
        
        # creating new_decile score using the formula from readme instructions 
        # decile score = 0.6P + 0.5J + 0.1C
        P = self.priors_count
        J = self.total_days_in_jail
        C = self.total_days_in_custody
        self.new_decile = 0.6 * P + 0.5 * J + 0.1 * C
    

# comparison function: decide if "a" should come before "b"   
def comes_before(a, b, key):
    # gettig the attribute values for both objects
    a_value = getattr(a, key)
    b_value = getattr(b, key)
    
    # if values are equal, use alphabetical order of names as tiebreaker 
    if a_value == b_value:
        return a.name < b.name
    
    # lastly, return True if a should come before b (smaller values first)
    return a_value < b_value
   

# merge sort merge two sorted halves into one sorted list
def merge(left, right, key): 
    result = []
    i = 0  # index for left list
    j = 0  # index for right list
    
    # then I'm comparing values from both lists and add smaller one first
    while i < len(left) and j < len(right):
        if comes_before(left[i], right[j], key):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # adding any leftover elements from left list
    while i < len(left):
        result.append(left[i])
        i += 1
    
    # adding any leftover elements from right list
    while j < len(right):
        result.append(right[j])
        j += 1
    
    return result
  

# recursively merge sort 
def merge_sort(data, key):
    # base case: if the list length is <= 1, return it, me hopes
    if len(data) <= 1:
        return data
    
    # find the middle point
    mid = len(data) // 2
    
    # split into left and right halves
    left_half = data[:mid]   # from start to middle
    right_half = data[mid:]  # from middle to end
    
    # recursively sort both halves
    sorted_left = merge_sort(left_half, key)
    sorted_right = merge_sort(right_half, key)
    
    # merge the sorted halves and return result
    return merge(sorted_left, sorted_right, key)


# load in data from csv. a lot of re-used concepts from Software design
def load_data(filename): 
    records = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        row_count = 0
        for row in reader: 
            # only want to read the first 8 rows since I added the original data back + a counter because why not
            if row_count >= 8:
                break
                
            # create a Person object using values from the row
            person = Person(
                name=row['name'],
                decile_score=row['decile_score'],
                priors_count=row['priors_count'],
                total_days_in_jail=row['total_days_jail'],
                total_days_in_custody=row['total_days_custody']
            )
            records.append(person)
            row_count += 1
    return records

if __name__ == "__main__": 
    # set filename to the csv file
    filename = 'compas_data.csv'
    
    # load the data from the csv
    people = load_data(filename)
    
    print(f"Loaded {len(people)} people from the dataset")
    
    # sort the data twice:
    # 1. once by "decile_score" from the dataset
    # 2. once by computed "new_decile"
    sorted_by_data_decile = merge_sort(people, 'decile_score')
    sorted_by_student_decile = merge_sort(people, 'new_decile')
    
    # print both sorted lists (names and their scores)
    print("\nSorted by original decile_score (lowest to highest):")
    print("Name".ljust(25) + "Original Score".ljust(15) + "New Score")
    print("-" * 60)
    for person in sorted_by_data_decile:
        print(f"{person.name.ljust(25)}{str(person.decile_score).ljust(15)}{person.new_decile:.2f}")
    
    print("\n" + "="*70 + "\n")
    
    print("Sorted by new_decile (lowest to highest):")
    print("Name".ljust(25) + "Original Score".ljust(15) + "New Score")
    print("-" * 60)
    for person in sorted_by_student_decile:
        print(f"{person.name.ljust(25)}{str(person.decile_score).ljust(15)}{person.new_decile:.2f}")
    
    # show some comparison statistics
    print("\n" + "="*70)
    print("COMPARISON SUMMARY:")
    print("="*70)
    
    # check if ordering changed
    different_order_count = 0
    for i in range(min(10, len(people))):
        if sorted_by_data_decile[i].name != sorted_by_student_decile[i].name:
            different_order_count += 1
    
    print(f"Top 10 positions that changed: {different_order_count}/10")
    print(f"Original decile scores range: {min(p.decile_score for p in people)} to {max(p.decile_score for p in people)}")
    print(f"New decile scores range: {min(p.new_decile for p in people):.2f} to {max(p.new_decile for p in people):.2f}")
