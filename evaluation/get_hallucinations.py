import pandas as pd

def get_hallucination_rows(input_file, output_file):
    df = pd.read_csv(input_file)
    
    # Replace 'None' with Python None (NaN)
    df.replace({'None': None}, inplace=True)

    # Define hallucination: Where the predicted total answer is not None, but is incorrect
    hallucinations_df = df[(df['Predicted Answer Total'] != df['Correct Answer']) & 
                           (df['Predicted Answer Total'].notna())]
    
    print("Hallucination rows count:", len(hallucinations_df))
    
    with open(output_file, 'w') as f:
        for index, row in hallucinations_df.iterrows():
            f.write(f"Question: {row['Question']}\n")
            f.write(f"Correct Answer: {row['Correct Answer']}\n")
            f.write(f"Predicted Answer Total: {row['Predicted Answer Total']}\n")
            f.write(f"Predicted Answer Algebraic Expression: {row['Predicted Answer Algebraic Expression']}\n")
            f.write(f"Predicted Answer Python Code: {row['Predicted Answer Python Code']}\n")
            f.write(f"Generated Algebraic Template: {row['Generated Algebraic Template']}\n")
            f.write(f"Generated Expression: {row['Generated Expression']}\n")
            f.write(f"Generated Python Code: {row['Generated Python Code']}\n")
            f.write(f"Variable Mapping: {row['Variable Mapping']}\n")
            f.write("Error: " + ("Yes\n" if row['Error'] else "No\n"))
            f.write("Error Message: " + (str(row['Error Message']) if row['Error Message'] else "None") + "\n")
            f.write("-" * 80 + "\n" + "\n" + "\n")

if __name__ == '__main__':
    input_csv = 'output_SVAMP_eval.csv'  # adjust path if located differently
    output_txt = 'hallucination_rows.txt'
    get_hallucination_rows(input_csv, output_txt)