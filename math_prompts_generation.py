from llm_inference.llm_factory import get_llm_service

# DISCLAIMER: The following examples inside the prompts are partly generated with Claude Opus 3
# NOTE: You may adapt the prompt based on the model you use
ALGEBRAIC_FEW_SHOT_PROMPT = [
    {
        "question": "John has A apples. He gives B apples to his friend. How many apples does John have left?",
        "answer": "A - B"
    },
    {
        "question": "A school has B classrooms. If each classroom has C students and D teachers, how many people are in the school?",
        "answer": "(C + D) * B"
    },
    {
        "question": "A factory produces E widgets per hour. If the factory operates for F hours per day and G days per week, how many widgets does the factory produce in H weeks?",
        "answer": "E * F * G * H"
    },
    {
        "question": "A company has I employees. Each employee works J hours per week. If the average hourly wage is K dollars and the company spends L percent of its revenue on salaries, what is the company's weekly revenue?",
        "answer": "(I * J * K) / (L / 100)"
    },
    {
        "question": "A store has D shirts in stock. If they sell E shirts per day, how many days will it take to sell all the shirts?",
        "answer": "D // E"
    }
]


ALGEBRAIC_SYSTEM_PROMPT ='''
You are a highly qualified expert in finding algebra expressions for a given math problem in natural language. 
You are given a math word problem and you need to find the algebraic expression that represents the problem.
Only the algebraic expression is required, without explanations. 
'''

def algebric_expression_generation(question: str, temperature: float):
    question = question.strip()
    SERVICE = get_llm_service('openai', 'gpt-3.5-turbo', temperature=temperature, max_tokens=200)
    messages = SERVICE.create_prompt(system_prompt=ALGEBRAIC_SYSTEM_PROMPT, few_shot_examples=ALGEBRAIC_FEW_SHOT_PROMPT, question=question)
    response = SERVICE.make_request(messages=messages)
    expression = response.strip()
    return expression


# DISCLAIMER: The following examples inside the prompts are partly generated with Claude Opus 3
# NOTE: You may adapt the prompt based on the model you use
PYTHON_FEW_SHOT_PROMPT = [
    {
        "question": "John has A apples. He gives B apples to his friend. How many apples does John have left?",
        "answer": "def solution(A, B):\n    return A - B"
    },
    {
        "question": "A school has B classrooms. If each classroom has C students and D teachers, how many people are in the school?",
        "answer": "def solution(B, C, D):\n    return (C + D) * B"
    },
    {
        "question": "A factory produces E widgets per hour. If the factory operates for F hours per day and G days per week, how many widgets does the factory produce in H weeks?",
        "answer": "def solution(E, F, G, H):\n    return E * F * G * H"
    },
    {
        "question": "A company has I employees. Each employee works J hours per week. If the average hourly wage is K dollars and the company spends L percent of its revenue on salaries, what is the company's weekly revenue?",
        "answer": "def solution(I, J, K, L):\n    return (I * J * K) / (L / 100)"
    },
    {
        "question": "A store has D shirts in stock. If they sell E shirts per day, how many days will it take to sell all the shirts?",
        "answer": "def solution(D, E):\n    return D // E"
    }
]

PYTHON_SYSTEM_PROMPT = '''
You are a highly qualified expert in finding Python code for a given math problem in natural language.
You are given a math word problem and you need to find the Python code that solves the problem.
Only the Python code is required, without explanations.
'''

def python_code_generation(question, temperature: float):
    SERVICE = get_llm_service('openai', 'gpt-3.5-turbo', temperature=temperature, max_tokens=200)
    messages = SERVICE.create_prompt(system_prompt=PYTHON_SYSTEM_PROMPT, few_shot_examples=PYTHON_FEW_SHOT_PROMPT, question=question)
    response = SERVICE.make_request(messages=messages)
    function_code = response.strip()
    return function_code