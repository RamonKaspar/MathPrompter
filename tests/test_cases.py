test_cases_paper = [
    {
        'q': 'At a restaurant, each adult meal costs $5 and kids eat free. If a group of 15 people came in and 8 were kids, how much would it cost for the group to eat?', 
        'qt': 'At a restaurant, each adult meal costs A and kids eat free. If a group of B people came in and C were kids, how much would it cost for the group to eat?', 
        'Mapping': {'A': 5.0, 'B': 15.0, 'C': 8.0},
        'Correct': 35.0
    },
    {
        'q': 'At the fair Adam bought 13 tickets. After riding the ferris wheel he had 4 tickets left. If each ticket cost 9 dollars, how much money did Adam spend riding the ferris wheel?',
        'qt': 'At the fair Adam bought A tickets. After riding the ferris wheel he had B tickets left. If each ticket cost C dollars, how much money did Adam spend riding the ferris wheel?',   
        'Mapping': {'A': 13.0, 'B': 4.0, 'C': 9.0},
        'Correct': 81.0
    },
    {
        'q': ' Each chocolate bar in a box cost $3. If a box had 9 bars total and Wendy sold all but 3 bars, how much money would she have made?',
        'qt': ' Each chocolate bar in a box cost A. If a box had B bars total and Wendy sold all but C bars, how much money would she have made?',
        'Mapping': {'A': 3.0, 'B': 9.0, 'C': 3.0},
        'Correct': 18.0
    },
    {
        'q': 'Jerry was helping the cafeteria workers pick up lunch trays, but he could only carry 8 trays at a time. If he had to pick up 9 trays from one table and 7 trays from another, how many trips will he make?',
        'qt': 'Jerry was helping the cafeteria workers pick up lunch trays, but he could only carry A trays at a time. If he had to pick up B trays from one table and C trays from another, how many trips will he make?',
        'Mapping': {'A': 8.0, 'B': 9.0, 'C': 7.0},
        'Correct': 2.0
    },
    {
        'q': 'Kaleb bought 14 boxes of chocolate candy and gave 5 to his little brother. If each box has 6 pieces inside it, how many pieces did Kaleb still have?',
        'qt': 'Kaleb bought A boxes of chocolate candy and gave B to his little brother. If each box has C pieces inside it, how many pieces did Kaleb still have?',
        'Mapping': {'A': 14.0, 'B': 5.0, 'C': 6.0},
        'Correct': 54
    }
]


test_cases_own = [
    {
        'q': 'A train travels 320 kilometers south and then 150 kilometers north. What is the net distance traveled by the train?',
        'qt': 'A train travels A kilometers south and then B kilometers north. What is the net distance traveled by the train?',
        'Mapping': {'A': 320.0, 'B': 150.0},
        'Correct': 170.0
    },
    {
        'q': 'A concert hall has 425 seats. During a concert, 285 tickets were sold at full price and the remaining at half price. If the full-price ticket costs $30, what was the total revenue?',
        'qt': 'A concert hall has A seats. During a concert, B tickets were sold at full price and the remaining at half price. If the full-price ticket costs C, what was the total revenue?',
        'Mapping': {'A': 425.0, 'B': 285.0, 'C': 30.0},
        'Correct': 9975.0
    },
    {
        'q': 'The temperature was 5 degrees Celsius at noon, but it had dropped to -30 degrees Celsius by midnight. What was the total temperature change?',
        'qt': 'The temperature was A degrees Celsius at noon, but it had dropped to B degrees Celsius by midnight. What was the total temperature change?',
        'Mapping': {'A': 5.0, 'B': -30.0},
        'Correct': 35.0
    }
]

test_cases = test_cases_paper + test_cases_own