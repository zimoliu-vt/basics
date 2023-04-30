"""
    Solve the problem from Khan Academy Math Grade 4
"""

"""
    Problem:
        One table can fit 6 people. but if we put 2 tables together, it can fit 10 people.
        Let x be the number of tables.
        Write an equation to represent the number of people that can fit at x tables.
        For example: How many people can fit at 3 tables?
        Answer: 14 people
"""

num_table = int(input("How many tables? "))
print(f"Number of table: {num_table}")
assert num_table>0, "Number of table must be greater than 0"
num_people = 2 + num_table * 4
print(f"Number of people: {num_people}")