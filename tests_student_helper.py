import unittest
import csv
import os
import sys
import student

"""
COMPAS Data Column Dictionary

This file provides:
  1. Complete COMPAS data dictionary for all 55 columns in the CSV
  2. Essential columns needed for the merge sort homework
  3. Standard unittest test cases with edge cases
  4. Simple helper functions for understanding the assignment

Students should:
  - Run individual test functions to check implementation
  - Use the column definitions to understand the COMPAS data
  - Refer to the test cases to understand expected behavior

Run with: python3 -m unittest tests_student_helper.py or python3 tests_student_helper.py
Tests merge sort homework functions with standard and edge cases.
"""

# COMPLETE COMPAS COLUMN DICTIONARY - 55 TERMS

COMPAS_COLUMNS = {
	# COLUMN 1-10: Identification and Demographics
	'id': 'unique identification for each person',
	'name': 'name of the subject',
	'first': 'first name of the person',
	'last': 'last name of the person',
	'compas_screening_date': 'COMPAS screening data of the suspect',
	'sex': 'sex of the subject',
	'dob': 'date of birth of the subject',
	'age': 'age category of the suspect at the time of the survey',
	'age_cat': 'age category of the subject',
	'race': 'race of the suspect',
	
	# COLUMN 11-15: Criminal History
	'juv_fel_count': 'the number of felony charges as a juvenile',
	'decile_score': 'recidivism score from 1 to 10',
	'juv_misd_count': 'the number of misdemeanor charges as a juvenile',
	'juv_other_count': 'the number of other charges for the suspect',
	'priors_count': 'the number of prior convictions for the suspect',
	
	# COLUMN 16-24: Current Case Information (c_ prefix)
	'days_b_screening_arrest': 'screeding date happened before arrest date',
	'c_jail_in': 'start timestamp of incarceration',
	'c_jail_out': 'end timestamp of incarceration',
	'c_case_number': 'charge case number of the suspect',
	'c_offense_date': 'charge offense date of the suspect',
	'c_arrest_date': 'charge arrest date of suspect',
	'c_days_from_compas': 'the count of days between screening date and (original) arrest date. If they are too far apart, that may i the number of days between committing an offense and going to jail',
	'c_charge_degree': 'charge degree of the suspect',
	'c_charge_desc': 'charge description of the suspect',
	
	# COLUMN 25-32: Recidivism Information (r_ prefix)
	'is_recid': 'whether the suspect recidivate',
	'r_case_number': 'recidivism case number of suspect',
	'r_charge_degree': 'recidivism charge degree of suspect',
	'r_days_from_arrest': 're-arrested from the re-offense date',
	'r_offense_date': 'recidivism offense date of the suspect',
	'r_charge_desc': 'recidivism charge description of the suspect',
	'r_jail_in': 'time and date when the suspect goes in the jail for recidivism',
	'r_jail_out': 'time and date when the suspect gets released from the jail for recidivism',
	
	# COLUMN 33-38: Violent Recidivism (vr_ prefix)
	'violent_recid': 'violent recidivism crime indicator of the suspect',
	'is_violent_recid': 'violent recidivism crime indicator of the suspect',
	'vr_case_number': 'violent_charge_number of the suspect',
	'vr_charge_degree': 'violent_charge_degree of the suspect',
	'vr_offense_date': 'violent_charge_date of the suspect',
	'vr_charge_desc': 'violent_charge_description of the suspect',
	
	# COLUMN 39-46: Assessment Information
	'type_of_assessment': 'onstant "Risk of Recidivism" for all rows, can be omitted',
	'decile_score.1': 'repetition of column 12',
	'score_text': 'decile score text -> low, medium, high',
	'screening_date': 'COMPAS screening date of the suspect',
	'v_type_of_assessment': 'constant "Risk of Violence" for all rows, can be omitted',
	'v_decile_score': 'violent recidivism score from 1 to 10',
	'v_score_text': 'violent recidivism score text -> low, medium, high',
	'v_screening_date': 'COMPAS screening data of the suspect for violent crimes',
	
	# COLUMN 47-52: Custody and Analysis
	'in_custody': 'custody start date',
	'out_custody': 'custody end date',
	'priors_count.1': 'the number of prior conviction for the suspect',
	'start': 'start point of the suspect entering the analysis',
	'end': 'end point of the suspect entering the survival analysis',
	'event': 'denotes whether the event of recidivism has occurred or not',
	
	# COLUMN 53-55: Outcome Variables
	'two_year_recid': 'target -> two year recidivism (binary 0/1)',
	'total_days_custody': 'how long the person stayed in custody',
	'total_days_jail': 'how long the person stayed in jail',
}

# ESSENTIAL COLUMNS FOR MERGE SORT HOMEWORK
# These are the 5 columns you actually need for this assignment
ESSENTIAL_FOR_HOMEWORK = {
	'name': 'name of the subject',
	'decile_score': 'recidivism score from 1 to 10',
	'priors_count': 'the number of prior convictions for the suspect',
	'total_days_jail': 'how long the person stayed in jail',
	'total_days_custody': 'how long the person stayed in custody',
}

# SHORT HW NOTES
HOMEWORK_NOTES = """
___________________________________________________________________________________
MERGE SORT HOMEWORK - NOTES
___________________________________________________________________________________

THE FORMULA:
	new_decile = 0.6*P + 0.5*J + 0.1*C
	
	Where:
	P = priors_count (number of prior convictions)
	J = total_days_jail (how long the person stayed in jail)
	C = total_days_custody (how long the person stayed in custody)

COLUMN MAPPING:
	The CSV file has column names that don't exactly match what the 
	Person class expects. You must fix this in load_data() function:
	
	CSV has: 'total_days_jail' ->  Person expects: 'total_days_in_jail'
	CSV has: 'total_days_custody' ->  Person expects: 'total_days_in_custody'
	
MAN COLUMNS:
	You only need 5 columns for this assignment:
	1. name
	2. decile_score  
	3. priors_count
	4. total_days_jail
	5. total_days_custody
___________________________________________________________________________________
"""

# HELPER FUNCTONS

# python3 -c "from key import show_all_columns; show_all_columns()
def show_all_columns():
	"""Print all 55 COMPAS column definitions in a nice format"""
	print("="*100)
	print("COMPLETE COMPAS DATA DICTIONARY - 55 COLUMNS")
	print("="*100)
	
	# Group columns by category for easier readability
	categories = {
		"Identification (1-10)": ['id', 'name', 'first', 'last', 'compas_screening_date', 'sex', 'dob', 'age', 'age_cat', 'race'],
		"Criminal History (11-15)": ['juv_fel_count', 'decile_score', 'juv_misd_count', 'juv_other_count', 'priors_count'],
		"Current Case (16-24)": ['days_b_screening_arrest', 'c_jail_in', 'c_jail_out', 'c_case_number', 'c_offense_date', 'c_arrest_date', 'c_days_from_compas', 'c_charge_degree', 'c_charge_desc'],
		"Recidivism (25-32)": ['is_recid', 'r_case_number', 'r_charge_degree', 'r_days_from_arrest', 'r_offense_date', 'r_charge_desc', 'r_jail_in', 'r_jail_out'],
		"Violent Recidivism (33-38)": ['violent_recid', 'is_violent_recid', 'vr_case_number', 'vr_charge_degree', 'vr_offense_date', 'vr_charge_desc'],
		"Assessments (39-46)": ['type_of_assessment', 'decile_score.1', 'score_text', 'screening_date', 'v_type_of_assessment', 'v_decile_score', 'v_score_text', 'v_screening_date'],
		"Custody & Analysis (47-52)": ['in_custody', 'out_custody', 'priors_count.1', 'start', 'end', 'event'],
		"Outcomes (53-55)": ['two_year_recid', 'total_days_custody', 'total_days_jail']
	}
	
	column_number = 1
	for category, columns in categories.items():
		print(f"\n{category}:")
		print("-" * 50)
		for col in columns:
			print(f"{column_number:2}. {col:25} : {COMPAS_COLUMNS[col]}")
			column_number += 1
	
	print("="*100)
# python3 -c "from key import check_homework_requirements; check_homework_requirements()
def show_homework_columns():
	"""Print only the 5 columns needed for the merge sort homework"""
	print("="*100)
	print("ESSENTIAL COLUMNS FOR MERGE SORT HOMEWORK")
	print("="*100)
	print("You only need these 5 columns from the CSV file:\n")
	
	homework_cols = ['name', 'decile_score', 'priors_count', 'total_days_jail', 'total_days_custody']
	for i, col in enumerate(homework_cols, 1):
		print(f"{i}. {col:20} : {COMPAS_COLUMNS[col]}")
	
	print("\n" + "="*100)
	print(HOMEWORK_NOTES)

# EXAMPLE ->  python3 -c "from key import get_definition; print('priors_count means:', get_definition('priors_count'))
def get_definition(column_name):
	"""
	Get the definition of a specific COMPAS column.
	
	Usage:
		definition = get_definition('decile_score')
		print(definition)  # Output: 'recidivism score from 1 to 10'
	"""
	if column_name in COMPAS_COLUMNS:
		return COMPAS_COLUMNS[column_name]
	else:
		return f"ERROR: Column '{column_name}' not found in COMPAS data."

def check_homework_requirements():
	"""
	Verify that you understand what's needed for the assignment.
	Returns a checklist of requirements.
	"""
	print("="*100)
	print("MERGE SORT HOMEWORK - REQUIREMENTS CHECKLIST")
	print("="*100)
	
	checklist = [
		("Person class stores all 5 attributes", False),
		("Person calculates new_decile correctly", False),
		("load_data() reads CSV and creates Person objects", False),
		("load_data() maps 'total_days_jail' to 'total_days_in_jail'", False),
		("load_data() maps 'total_days_custody' to 'total_days_in_custody'", False),
		("comes_before() compares values and handles ties", False),
		("merge() correctly combines sorted lists", False),
		("merge_sort() recursively sorts lists", False),
		("main() sorts by both decile_score and new_decile", False),
		("main() prints both sorted lists for comparison", False),
	]
	
	for i, (requirement, _) in enumerate(checklist, 1):
		print(f"[ ] {i:2}. {requirement}")
	
	print("\n" + "="*100)
	print("After implementing each item, check it off in the Google Doc!")
	print("="*100)

# SUMMARY
if __name__ == "__main__":
	print("\n" + "="*100)
	print("COMPAS DATA COLUMN REFERENCE KEY")
	print("="*100)
	print("\nThis file contains definitions for all 55 COMPAS data columns.")
	print("Use it as a reference when working with the COMPAS dataset.")
	
	print("\nAvailable functions:")
	print("  1. show_all_columns()     - View all 55 column definitions")
	print("  2. show_homework_columns()- View only the 5 columns you need")
	print("  3. get_definition(col)    - Get definition for specific column")
	print("  4. check_homework_requirements() - See assignment checklist")
	
	print("\n" + "="*100)
	print("Run show_homework_columns() to see what you need!")
	print("="*100)

# STANDARD AND EDGE CASES

# Import student code
try:
    import student
except ImportError:
    print("ERROR: Could not import student.py")
    sys.exit(1)

# Test suite for merge sort implementation


class TestMergeSortFunctions(unittest.TestCase):

     # Set up test data before each test
      def setUp(self):
        self.create_test_files()

      # Clean up test files after each test
      def tearDown(self):
        for f in ['test_normal.csv', 'test_empty.csv', 'test_single.csv', 'test_ties.csv', 'test_extremes.csv']:
          if os.path.exists(f):
            os.remove(f)

      # Create test CSV files for various test cases
      def create_test_files(self):

	      # TEST 1: BASIC FUNCTIONALITY (Standard Case)
	      # Tests: mixed data
        with open('test_normal.csv', 'w', newline='') as f:
          writer = csv.writer(f)
          writer.writerow(['name', 'decile_score', 'priors_count',
                          'total_days_jail', 'total_days_custody'])

          writer.writerows([
              # Names are the expected sorting position
            ['1_FirstByDecile', 1, 0, 5, 8],     	 # Lowest decile (1)
            ['2_SecondByDecile', 3, 2, 15, 20],   	 # Second lowest (3)
            ['3_ThirdByDecile', 5, 3, 25, 30],	     # Middle (5)
            ['4_FourthByDecile', 7, 4, 35, 40],  	 # Second highest (7)
            ['5_FifthByDecile', 9, 5, 45, 50]        # Highest decile (9)
              ])

           # TEST 2: EMPTY FILE (Edge Case)
           # Tests: load_data() doesn't crash on empty files
          with open('test_empty.csv', 'w', newline='') as f:
                  writer = csv.writer(f)
                  writer.writerow(
                  	['name', 'decile_score', 'priors_count', 'total_days_jail', 'total_days_custody'])

            # TEST 3: SINGLE RECORD (Edge Case)
            # Tests: merge_sort() base case (list length <= 1)
          with open('test_single.csv', 'w', newline='') as f:
                  writer = csv.writer(f)
                  writer.writerow(
                  	['name', 'decile_score', 'priors_count', 'total_days_jail', 'total_days_custody'])
                  writer.writerow(['Case_Single', 5, 2, 20, 25])

            # TEST 4: ALL SAME SCORES (Edge Case)
            # Tests: alphabetical tie-breaking in comes_before()
          with open('test_ties.csv', 'w', newline='') as f:
                  writer = csv.writer(f)
                  writer.writerow(
                  	['name', 'decile_score', 'priors_count', 'total_days_jail', 'total_days_custody'])
                  writer.writerows([
                      ['Layla_Tie', 5, 2, 30, 40],    # Should be LAST alphabetically
                    # Should be FIRST alphabetically
                    ['Amy_Tie', 5, 2, 30, 40],
                    # Should be MIDDLE alphabetically
                    ['Jean_Tie', 5, 2, 30, 40]
                      ])

            # TEST 5: EXTREME VALUES (Edge Case)
            # Tests: Formula handles min/max values without errors
          with open('test_extremes.csv', 'w', newline='') as f:
                  writer = csv.writer(f)
                  writer.writerow(
                  	['name', 'decile_score', 'priors_count', 'total_days_jail', 'total_days_custody'])
                  writer.writerows([
                      ['Min', 1, 0, 0, 0],		# Minimum everything
                      ['Max', 100, 100, 500, 500]  # Input maximum values
                      ])

    ### Person Class Tests ###
      def test_person_creation(self):
        person = student.Person("Test", 5, 2, 30, 40)
        self.assertIsNotNone(person)

      # Test Person stores all required attributes
      def test_person_attributes(self):
        person = student.Person("Test", 5, 2, 30, 40)

        # Check all required attributes exist
        required =['name', 'decile_score', 'priors_count',
                  'total_days_in_jail', 'total_days_in_custody', 'new_decile']
        for attr in required:
          self.assertTrue(hasattr(person, attr), f"Missing attribute: {attr}")

    ### comes_before() Function Tests ###
      # Test basic comparison with different values
      def test_comes_before_basic(self):
        p1 = student.Person("Apple", 2, 0, 0, 0)    # Lower score
        p2 = student.Person("Jack", 8, 0, 0, 0)			# Higher score

        # p1 should come before p2 when sorting by decile_score
        self.assertTrue(student.comes_before(p1, p2, 'decile_score'))
        # p2 should NOT come before p1
        # Test alphabetical tie-breaking when scores are equal
        self.assertFalse(student.comes_before(p2, p1, 'decile_score'))

      def test_comes_before_tiebreaker(self):
        p1 = student.Person("Aaron", 5, 0, 0, 0)    # Alphabetically first
        p2 = student.Person("Zarah", 5, 0, 0, 0)     # Alphabetically last

        # Aaron should come before Zarah when scores are equal
        self.assertTrue(student.comes_before(p1, p2, 'decile_score'))
        # Zarah should NOT come before Aaron
        # Test comparison works with different attribute keys
        self.assertFalse(student.comes_before(p2, p1, 'decile_score'))

      def test_comes_before_different_keys(self):
        p1 = student.Person("A", 1, 0, 10, 20)      # Lower new_decile
        p2 = student.Person("B", 1, 5, 30, 40)     # Higher new_decile

        # worsks with 'new_decile' as key
        result = student.comes_before(p1, p2, 'new_decile')
        self.assertTrue(result is not None)

    ### merge() Function Tests ###
      # Test merging two sorted lists
      def test_merge_basic(self):
        left =[
            student.Person("A", 1, 0, 0, 0),
          student.Person("C", 3, 0, 0, 0)
        ]
        right =[
            student.Person("B", 2, 0, 0, 0),
          student.Person("D", 4, 0, 0, 0)
        ]

        merged = student.merge(left, right, 'decile_score')

        # Check merged list has correct length
        self.assertEqual(len(merged), 4)
        # Check merged list is sorted
        scores = [p.decile_score for p in merged]
        self.assertEqual(scores, [1, 2, 3, 4])

      # Test merging with empty list
      def test_merge_empty_lists(self):
        # Empty left, non-empty right
        left = []
        right = [student.Person("B", 2, 0, 0, 0)]

        merged1 = student.merge(left, right, 'decile_score')
        self.assertEqual(len(merged1), 1)
        self.assertEqual(merged1[0].decile_score, 2)

        # Non-empty left, empty right
        left = [student.Person("A", 1, 0, 0, 0)]
        right = []

        merged2 = student.merge(left, right, 'decile_score')
        self.assertEqual(len(merged2), 1)
        self.assertEqual(merged2[0].decile_score, 1)

        # Both empty
        merged3 = student.merge([], [], 'decile_score')
        self.assertEqual(len(merged3), 0)

    ### merge_sort() Function Tests ###
      # Test basic merge sort functionality
      def test_merge_sort_basic(self):
        people = [
            student.Person("C", 3, 0, 0, 0),
          student.Person("A", 1, 0, 0, 0),
          student.Person("B", 2, 0, 0, 0),
          student.Person("E", 5, 0, 0, 0),
          student.Person("D", 4, 0, 0, 0)
        ]

        sorted_people = student.merge_sort(people, 'decile_score')

        # Check length unchanged
        self.assertEqual(len(sorted_people), 5)
        # Check sorted order
        scores = [p.decile_score for p in sorted_people]
        self.assertEqual(scores, [1, 2, 3, 4, 5])

        # Test merge sort with empty list
      def test_merge_sort_empty(self):
        sorted_list = student.merge_sort([], 'decile_score')
        self.assertEqual(len(sorted_list), 0)

      # Test merge sort with single element
      def test_merge_sort_single(self):
        people = [student.Person("Single", 5, 0, 0, 0)]
        sorted_people = student.merge_sort(people, 'decile_score')
        self.assertEqual(len(sorted_people), 1)
        self.assertEqual(sorted_people[0].name, "Single")

      # Test merge sort with already sorted list
      def test_merge_sort_already_sorted(self):
        people = [
            student.Person("A", 1, 0, 0, 0),
          student.Person("B", 2, 0, 0, 0),
          student.Person("C", 3, 0, 0, 0)
        ]

        sorted_people = student.merge_sort(people, 'decile_score')

        # Should return same order
        names = [p.name for p in sorted_people]
        self.assertEqual(names, ['A', 'B', 'C'])

      # Test merge sort with reverse sorted list
      def test_merge_sort_reverse_sorted(self):
        people = [
          student.Person("C", 3, 0, 0, 0),
          student.Person("B", 2, 0, 0, 0),
          student.Person("A", 1, 0, 0, 0)
        ]

        sorted_people = student.merge_sort(people, 'decile_score')
        scores = [p.decile_score for p in sorted_people]
        self.assertEqual(scores, [1, 2, 3])

    ### load_data() Function Tests ###

      # Test loading data from normal CSV file
      def test_load_data_normal(self):
        people = student.load_data('test_normal.csv')
        self.assertIsNotNone(people)
        self.assertEqual(len(people), 5)

        # Check first person has correct attributes
        if people:
          first_person = people[0]
          self.assertTrue(hasattr(first_person, 'name'))
          self.assertTrue(hasattr(first_person, 'new_decile'))

      # Test loading data from empty CSV file
      def test_load_data_empty(self):
        people = student.load_data('test_empty.csv')

        # Should return empty list
        self.assertIsNotNone(people)
        self.assertEqual(len(people), 0)

      # Test loading data from CSV with single record
      def test_load_data_single(self):
        people = student.load_data('test_single.csv')

        self.assertEqual(len(people), 1)
        if people:
          self.assertEqual(people[0].name, "Case_Single")

      # Test that CSV columns are correctly mapped to Person attributes"

      def test_load_data_column_mapping(self):
        people = student.load_data('test_normal.csv')

        # Person should have total_days_in_jail, not total_days_jail
        if people:
          person = people[0]
          self.assertTrue(hasattr(person, 'total_days_in_jail'))
          self.assertTrue(hasattr(person, 'total_days_in_custody'))

    ### Integration Tests ###

      # Test complete homework workflow
      def test_complete_workflow(self):
        # Load data
        people = student.load_data('test_normal.csv')
        self.assertIsNotNone(people)
        self.assertTrue(len(people) > 0)

        # Sort by original decile_score
        sorted_by_original = student.merge_sort(people, 'decile_score')

        # Sort by new_decile
        sorted_by_new = student.merge_sort(people, 'new_decile')

        # Both should have same number of elements
        self.assertEqual(len(sorted_by_original), len(sorted_by_new))
        self.assertEqual(len(sorted_by_original), len(people))

        # Both should be sorted
        original_scores = [p.decile_score for p in sorted_by_original]
        new_scores = [p.new_decile for p in sorted_by_new]

        self.assertEqual(original_scores, sorted(original_scores))
        self.assertEqual(new_scores, sorted(new_scores))

      # Test sorting with all equal scores (alphabetical order)
      def test_edge_case_ties(self):
        people = student.load_data('test_ties.csv')
        if people:
            sorted_people = student.merge_sort(people, 'decile_score')
            # Should be sorted alphabetically
            names = [p.name for p in sorted_people]
            self.assertEqual(names, ['Amy_Tie', 'Jean_Tie', 'Layla_Tie'])

      # Test sorting with extreme values
      def test_edge_case_extremes(self):
        people = student.load_data('test_extremes.csv')
        if people:
          sorted_people = student.merge_sort(people, 'decile_score')
          # Min should come before Max
          names = [p.name for p in sorted_people]
          self.assertEqual(names, ['Min', 'Max'])


# Runs
if __name__ == '__main__':
  unittest.main(verbosity=2)
