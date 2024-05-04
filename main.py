from generating_algebraic_template import generating_algebraic_template
from math_prompts_generation import algebric_expression_generation, python_code_generation
from compute_verification import perform_computational_verification

def mathprompter(question: str, temperatures=[0], n_test_random_values=5):
    """
    Attempts to verify a mathematical prompt via repeated computations and returns the most frequently computed result.
    Parameters:
        question (str): The mathematical question in natural-language form.
        temperatures (list[float]): Sequences of temperature settings used to vary generation randomness.
                                    Defines the number of self consistency iterations.
        n_test_random_values (int): Number of random samples to test for each verification.

    Returns:
        The most frequently computed result over iterations, or None if no consistent result was found.
    """
    result_counts = {}
    for temp in temperatures:     # TODO: Parallelize this
        try:
            qt, variable_mapping = generating_algebraic_template(question)
            exp = algebric_expression_generation(qt, temperature=temp)
            code = python_code_generation(qt, temperature=temp)
            res = perform_computational_verification(exp, code, variable_mapping, sample_size=n_test_random_values)
            if res is not None:
                if res in result_counts:
                    result_counts[res] += 1
                else:
                    result_counts[res] = 1
        except Exception as e:
            print(f"An error occurred during the verification process: {e}")
            continue
    
    if result_counts:
        max_result = max(result_counts, key=result_counts.get)
        return max_result
    else:
        print("No successful computations were found.")
        return None

# Example usage
if __name__ == '__main__':
    question = 'At a restaurant, each adult meal costs $5 and kids eat free. If a group of 15 people came in and 8 were kids, how much would it cost for the group to eat?'
    res = mathprompter(question, temperatures=[0.0, 0.2, 0.4, 0.6, 0.8], n_test_random_values=3)
    print(f"Result: {res}")
    