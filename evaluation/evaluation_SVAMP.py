import json
from tqdm import tqdm
import sys
import pandas as pd

# Add the root directory to sys.path to find the main module
sys.path.append('..')

from main import *
from compute_verification import *

def evaluate_on_svamp(sample_size):
    with open('SVAMP.json', 'r') as file:
        data = json.load(file)
    data = random.sample(data, k=sample_size)  # Take a random sample of 100 rows
    
    header = ["Question", "Correct Answer", "Predicted Answer Total", "Predicted Answer Algebraic Expression", "Predicted Answer Python Code", "Generated Algebraic Template", "Generated Expression", "Generated Python Code", "Variable Mapping", "Error", "Error Message"]
    df = pd.DataFrame(columns=header)
    
    for entry in tqdm(data, desc="Evaluating SVAMP dataset"):
        full_question = entry["Body"] + " " + entry["Question"]
        result, qt, exp, code, variable_mapping = None, None, None, None, None
        try:
            qt, variable_mapping = generating_algebraic_template(full_question)
            exp = algebric_expression_generation(qt)
            code = python_code_generation(qt)
            result = perform_computational_verification(exp, code, variable_mapping, sample_size=3)
            exp_result = evaluate_expression(exp, variable_mapping)
            code_result = execute_python_code(code, variable_mapping)
            error, error_message = False, ""
        except Exception as e:
            error, error_message = True, str(e)
            print(f"An error occurred during the verification process: {e}")

        data_row = pd.DataFrame([{
            "Question": full_question, "Correct Answer": entry["Answer"], "Predicted Answer Total": result,
            "Predicted Answer Algebraic Expression": exp_result, "Predicted Answer Python Code": code_result,
            "Generated Algebraic Template": qt, "Generated Expression": exp, "Generated Python Code": code,
            "Variable Mapping": variable_mapping, "Error": error, "Error Message": error_message
        }])
        
        df = pd.concat([df, data_row], ignore_index=True)
        df.to_csv("output_SVAMP_eval.csv", encoding='utf-8', index=False)
    return 

# Assuming mathprompter function is imported and available
if __name__ == '__main__':
    evaluate_on_svamp(sample_size=1000)
