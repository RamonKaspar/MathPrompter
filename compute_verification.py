import random

def create_random_input(mapping):
    """ Generate a random test input based on variable mappings. """
    return {var: random.randint(1, 500) for var in mapping}

def evaluate_expression(expression, mapping):
    """ Evaluates a mathematical expression safely using a dictionary of variable replacements. """
    try:
        local_dict = mapping.copy()
        return eval(expression, {"__builtins__": None}, local_dict)
    except SyntaxError as e:
        print(f"Syntax error in the expression: {e}")
        return None
    except Exception as e:
        print(f"Runtime error during expression evaluation: {e}")
        return None

def execute_python_code(code, mapping):
    """
    Executes Python code with a specified input mapping.
    This code assumes the function 'solution' is defined within the passed code.
    """
    local_locals = mapping.copy()
    wrapped_code = code + f"\nresult = solution({', '.join(f'{k}={v}' for k, v in mapping.items())})"
    try:
        exec(wrapped_code, {"__builtins__": None}, local_locals)
        if 'result' in local_locals:
            return local_locals['result']
        else:
            print("No 'result' key was found in the local variables after executing the code.")
            return None
    except Exception as e:
        print(f"Error when executing Python code: {e}")
        return None

def perform_computational_verification(expression, code, variable_mapping, sample_size=5):
    """
    Verifies that the execution results of both an expression and Python code are consistent across random inputs.
    This verification is repeated for a defined number of times specified by 'sample_size'.
    If consistent results are found, it evaluates them again with actual mappings to ensure accuracy.
    """
    for _ in range(sample_size):
        test_input = create_random_input(variable_mapping)
        exp_result = evaluate_expression(expression, test_input)
        code_result = execute_python_code(code, test_input)
        
        if exp_result != code_result:
            return None
        
    # Consensus found, calculate result for real variable mapping
    exp_result = evaluate_expression(expression, variable_mapping)
    code_result = execute_python_code(code, variable_mapping)
    if exp_result == code_result:
        return exp_result
    else:
        return None
    
    



