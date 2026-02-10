# CS252 Algorithms In-Class Handout Lab

### OVERVIEW
* OBJECTIVE
* INTRODUCTION TO THE PROBLEM
* REVIEW & UNDERSTANDING BINARY SEARCH
* STARTER CODE
* INDUCTIVE PROOF OF CORRECTNESS
* PROVIING EFFICIENCY
* IMPLEMENT & TEST
* CIVIC ENGAGEMENT UNDERSTANDING
* EXIT TICKET

### OBJECTIVE
This lab is designed to deepen your understanding of binary search by applying it to a real-world scenerio and reasoning formally about its correctness and efficieny.

You are expected to already be familiar with the basic mechanics of binary search. This lab emphasizes intuition-building, justification, and careful reeasoning rather than learning the algorithm for the first time as the only goal. 

You will:
* Complete a partially written binary search function
* Reason about correctness using induction
* Analyze efficiency using a recurrence relation
* Reflect on why these ideas matter in civic contexts
```
Does this task/explanation/question make sense?
[__] yes | [__] no | [__] partially
other comments: __________
```

### INTRODUCTION TO THE PROBLEM
In emergency situations, response systems must quickly locate nearby evacuation shelters. Suppose shelters are indexed by zip code and stored in a **sorted list**.

Your goal in this lab is to design and reason about an algorithm that efficiently locates a shelter by zip code, or determines that no such shelter exists.

Throughout the lab, assume:
* Zip codes are integers
* The list is already sorted
* Speed and correctness both matter

```
Does this task/explanation/question make sense?
[__] yes | [__] no | [__] partially
other comments: __________
```

### REVIEW & UNDERSTANDING BINARY SEARCH
You have previously overviewed binarcy search. Before beginning the lab activities, review the following ideas:
* Binary search operates on sorted data
* The search interval is reduced at every step
* Comparisons determine which half of the list can be safely discarded

**Think about (but do not answer yet)**
* Why is it safe to discard half the list?
* What condition tells us that the search should stop?

```
Does this task/explanation/question make sense?
[__] yes | [__] no | [__] partially
other comments: __________
```

### STARTER CODE
Complete the following function **on paper**. Do not change the function header.

```python
def find_shelter_by_zip(sorted_zips, target_zip)
	"""
	Returns the index of target_zip in sorted zips,
	or -1 if target_zip is not found.
	sorted_zips is sorted in ascending order
	"""
	low = 0
	high = len(sorted_zips) - 1

	while low <= high:
		# Determine the middle index
		mid = __________

		# Compare the middle element to the target
		if __________:
			return __________
		elif __________:
			high = __________
		else:
			low = __________

	# Target not found
	return __________
```
Guiding Prompts:
* What must be true for the loop to continue?
* How do *low* and *high* change in each case?
* Under what condition should the algorithm return -1?
```
Does this task/explanation/question make sense?
[__] yes | [__] no | [__] partially
other comments: __________
```
### INDUCTIVE PROOF OF CORRECTNESS
You will now justify the correctness of binary search using **induction**.

#### Task A: Base Cases
Identify the smallest possible input sizes and describe: 
* What binary search does
* Why the result is correct

Do not just assume correctness, explain it.

#### Task B: Inductive Hypothesis
State a clear inductive hypothesis for binary search on inputs of size *k*

#### Task C: Inductive Step
For an input of size *n > 1*:
* Describe what the algorithm does first
* Explain how the problem is reduced
* Justify why the inductive hypothesis applies

```
Does this task/explanation/question make sense?
[__] yes | [__] no | [__] partially
other comments: __________
```
### PROVIING EFFICIENCY
Binary search reduces the problem size at each step.

#### Task
You are given the recurrence relation:
##### *T(n) = T(n/2) + c*
By hand:
1. Draw a recursion tree
2. Determine how many level the tree has
3. Explain what this implies about the runtime

There is no code to run. This is a mathematical analysis exercise.
```
Does this task/explanation/question make sense?
[__] yes | [__] no | [__] partially
other comments: __________
```
### IMPLEMENT & TEST
#### Purpose
The goal of testing is to verify **correcctness**, not measure runtime. 

You are given a sorted list of zip codes in class.

#### Task
For each test case provided:
* Trace the algorithm step-by-step
* Record the values of low, high, and mid
* State the final return value

Include at least:
* One case where the target exists
* One case where the target does not exist
```
Does this task/explanation/question make sense?
[__] yes | [__] no | [__] partially
other comments: __________
```
### CIVIC ENGAGEMENT UNDERSTANDING
Binary search is often used in systems where speed and correctness are critical.

#### Activity
In groups, discuss:
* Why inefficient searching could be harmful in emergency systems
* How algorithmic gurantees affect public trust

Summarize your discussion in 2-3 bullet points. 

```
Does this task/explanation/question make sense?
[__] yes | [__] no | [__] partially
other comments: __________
```
### EXIT TICKET
Answer the following briefly:
1. Why does binary search never miss a target that exists?
2. How does the recurrence relation justify logarithmic time?
3. Why is binary search appropriate for emergency-response systems?
4. Name another scernioe where binary search would be a good choice and explain why.

```
Does this task/explanation/question make sense?
[__] yes | [__] no | [__] partially
other comments: __________
```
