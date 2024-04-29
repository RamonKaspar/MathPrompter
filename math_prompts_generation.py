from llm_inference.llm_factory import get_llm_service

# NOTE: Specify the LLM API you want use here
# SERVICE = get_llm_service('google', 'gemini-pro')
# SERVICE = get_llm_service('huggingface', 'meta-llama/Meta-Llama-3-8B-Instruct')
SERVICE = get_llm_service('azure', 'gpt-35-turbo')

# DISCLAIMER: The following examples inside the prompts are partly generated with Claude Opus 3
# NOTE: You may adapt the prompt based on the model you use
algebric_prompt = '''
<Question>: John has A apples. He gives B apples to his friend. How many apples does John have left?
Answer = A - B
<Question>: A school has B classrooms. If each classroom has C students and D teachers, how many people are in the school?
Answer = (C + D) * B
<Question>: A factory produces E widgets per hour. If the factory operates for F hours per day and G days per week, how many widgets does the factory produce in H weeks?
Answer = E * F * G * H
<Question>: A company has I employees. Each employee works J hours per week. If the average hourly wage is K dollars and the company spends L percent of its revenue on salaries, what is the company's weekly revenue?
Answer = (I * J * K) / (L / 100)
<Question>: A store has D shirts in stock. If they sell E shirts per day, how many days will it take to sell all the shirts?
Answer = D // E
<Question>: {question}
'''

def algebric_expression_generation(question: str):
    question = question.strip()
    prompt = algebric_prompt.format(question=question).strip() + "\n"
    response = SERVICE.make_request(prompt=prompt)
    expression = response.split(f"<Question>: {question}")[-1].strip()
    return expression.split("Answer = ")[-1]


# DISCLAIMER: The following examples inside the prompts are partly generated with Claude Opus 3
python_prompt = '''
<Question>: John has A apples. He gives B apples to his friend. How many apples does John have left?
<Function>:
def solution(A, B):
    return A - B
<Question>: A school has B classrooms. If each classroom has C students and D teachers, how many people are in the school?
<Function>:
def solution(B, C, D):
    return (C + D) * B
<Question>: A factory produces E widgets per hour. If the factory operates for F hours per day and G days per week, how many widgets does the factory produce in H weeks?
<Function>:
def solution(E, F, G, H):
    return E * F * G * H
<Question>: A company has I employees. Each employee works J hours per week. If the average hourly wage is K dollars and the company spends L percent of its revenue on salaries, what is the company's weekly revenue?
<Function>:
def solution(I, J, K, L):
    return (I * J * K) / (L / 100)
<Question>: A store has D shirts in stock. If they sell E shirts per day, how many days will it take to sell all the shirts?
<Funtion>:
def solution(D, E):
    return D // E
<Question>: {question}
<Function>:
'''

def python_code_generation(question):
    prompt = python_prompt.format(question=question.strip()).strip() + "\n"
    response = SERVICE.make_request(prompt=prompt)
    function_code = response.split("<Function>:")[-1].strip()
    return function_code