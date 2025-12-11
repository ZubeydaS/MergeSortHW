import unittest
import csv
import os
import sys
import student

'''
CS 252 Merge Sort Homework Tests
Fall Semester 2026

Run with: python3 -m unittest tests_grader.py or python3 tests_grader.py
Tests merge sort homework functions with standard and edge cases.
'''
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
          writer.writerow(['name', 'decile_score', 'priors_count', 'total_days_jail', 'total_days_custody'])
        
          writer.writerows([
            # Names are the expected sorting position
            ['1_FirstByDecile', 1, 0, 5, 8],      # Lowest decile (1)
            ['2_SecondByDecile', 3, 2, 15, 20],    # Second lowest (3)
            ['3_ThirdByDecile', 5, 3, 25, 30],    # Middle (5)
            ['4_FourthByDecile', 7, 4, 35, 40],   # Second highest (7)
            ['5_FifthByDecile', 9, 5, 45, 50]      # Highest decile (9)
      ])

            # TEST 2: EMPTY FILE (Edge Case)
            # Tests: load_data() doesn't crash on empty files
          with open('test_empty.csv', 'w', newline='') as f:
                  writer=csv.writer(f)
                  writer.writerow(['name', 'decile_score', 'priors_count', 'total_days_jail', 'total_days_custody'])

            # TEST 3: SINGLE RECORD (Edge Case)
            # Tests: merge_sort() base case (list length <= 1)
          with open('test_single.csv', 'w', newline='') as f:
                  writer = csv.writer(f)
                  writer.writerow(['name', 'decile_score', 'priors_count', 'total_days_jail', 'total_days_custody'])
                  writer.writerow(['Case_Single', 5, 2, 20, 25])

            # TEST 4: ALL SAME SCORES (Edge Case)
            # Tests: alphabetical tie-breaking in comes_before()
          with open('test_ties.csv', 'w', newline='') as f:
                  writer=csv.writer(f)
                  writer.writerow(['name', 'decile_score', 'priors_count', 'total_days_jail', 'total_days_custody'])
                  writer.writerows([
                    ['Layla_Tie', 5, 2, 30, 40],    # Should be LAST alphabetically
                    ['Amy_Tie', 5, 2, 30, 40],    # Should be FIRST alphabetically
                    ['Jean_Tie', 5, 2, 30, 40]     # Should be MIDDLE alphabetically
          ])

            # TEST 5: EXTREME VALUES (Edge Case)
            # Tests: Formula handles min/max values without errors
          with open('test_extremes.csv', 'w', newline='') as f:
                  writer = csv.writer(f)
                  writer.writerow(['name', 'decile_score', 'priors_count', 'total_days_jail', 'total_days_custody'])
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
        person=student.Person("Test", 5, 2, 30, 40)
    
        # Check all required attributes exist
        required=['name', 'decile_score', 'priors_count',
            'total_days_in_jail', 'total_days_in_custody', 'new_decile']
        for attr in required:
          self.assertTrue(hasattr(person, attr), f"Missing attribute: {attr}")

    ### comes_before() Function Tests ###
      # Test basic comparison with different values
      def test_comes_before_basic(self):
        p1=student.Person("Apple", 2, 0, 0, 0)    # Lower score
        p2=student.Person("Jack", 8, 0, 0, 0)			# Higher score

        # p1 should come before p2 when sorting by decile_score
        self.assertTrue(student.comes_before(p1, p2, 'decile_score'))
        # p2 should NOT come before p1
        # Test alphabetical tie-breaking when scores are equal
        self.assertFalse(student.comes_before(p2, p1, 'decile_score'))
      def test_comes_before_tiebreaker(self):
        p1=student.Person("Aaron", 5, 0, 0, 0)    # Alphabetically first
        p2=student.Person("Zarah", 5, 0, 0, 0)     # Alphabetically last

        # Aaron should come before Zarah when scores are equal
        self.assertTrue(student.comes_before(p1, p2, 'decile_score'))
        # Zarah should NOT come before Aaron
        # Test comparison works with different attribute keys
        self.assertFalse(student.comes_before(p2, p1, 'decile_score'))
            
      def test_comes_before_different_keys(self):
        p1=student.Person("A", 1, 0, 10, 20)      # Lower new_decile
        p2=student.Person("B", 1, 5, 30, 40)     # Higher new_decile

        # Should worsks with 'new_decile' as key
        result=student.comes_before(p1, p2, 'new_decile')
        self.assertTrue(result is not None)

    ### merge() Function Tests ###
      # Test merging two sorted lists
      def test_merge_basic(self):
        left=[
          student.Person("A", 1, 0, 0, 0),
          student.Person("C", 3, 0, 0, 0)
        ]
        right=[
          student.Person("B", 2, 0, 0, 0),
          student.Person("D", 4, 0, 0, 0)
        ]

        merged=student.merge(left, right, 'decile_score')

        # Check merged list has correct length
        self.assertEqual(len(merged), 4)
        # Check merged list is sorted
        scores=[p.decile_score for p in merged]
        self.assertEqual(scores, [1, 2, 3, 4])

      # Test merging with empty list
      def test_merge_empty_lists(self):
        # Empty left, non-empty right
        left=[]
        right=[student.Person("B", 2, 0, 0, 0)]

        merged1 = student.merge(left, right, 'decile_score')
        self.assertEqual(len(merged1), 1)
        self.assertEqual(merged1[0].decile_score, 2)

        # Non-empty left, empty right
        left=[student.Person("A", 1, 0, 0, 0)]
        right=[]

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
        people=student.load_data('test_ties.csv')
        if people:
            sorted_people = student.merge_sort(people, 'decile_score')
            # Should be sorted alphabetically
            names=[p.name for p in sorted_people]
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
