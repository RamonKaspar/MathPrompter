import json
from tqdm import tqdm
import sys

# Add the root directory to sys.path to find the main module
sys.path.append('..')

from main import mathprompter

def evaluate_on_svamp():
    with open('SVAMP.json', 'r') as file:
        data = json.load(file)

    correct_counts = 0
    total_counts = len(data)
    
    for entry in tqdm(data, desc="Evaluating SVAMP dataset"):
        full_question = entry["Body"] + " " + entry["Question"]
        result = mathprompter(full_question, iterations=3, sample_size=5)
        
        try:
            if abs(result - entry["Answer"]) < 1e-5:
                correct_counts += 1
        except TypeError:
            # This occurs if result is None or cannot be directly compared to a float
            continue
    
    accuracy = (correct_counts / total_counts) * 100
    return accuracy

# Assuming mathprompter function is imported and available
if __name__ == '__main__':
    accuracy = evaluate_on_svamp()
    print(f"Accuracy: {accuracy:.2f}%")