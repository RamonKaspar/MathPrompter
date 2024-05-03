import re

def generate_variable_names(limit=26):
    """ Generates a list of unique variable names. """
    base_names = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    extended_names = base_names.copy()
    idx = 0
    while len(extended_names) < limit:
        extended_names.append(base_names[idx % 26] + str(idx // 26 + 1))
        idx += 1
    return extended_names

def generating_algebraic_template(q):
    """
    Transforms numeric values in a math word problem into unique variables.

    Steps:
    1. Split the text to isolate numbers and mathematical operators.
       This preserves the structure in which numbers and mathematical operators such as '+',
       '-', '*', '/', '=', and '^' are treated separately.
    
    2. Process each element from the split to detect numeric values.
       Identify segments that contain digits, potentially including numbers attached to units or symbols.

    3. For segments that include numeric values with non-numeric substrings at the beginning or end (e.g., units or currency symbols):
       - Split any directly attached non-numeric characters from the numbers. This might be units like 'cm', or symbols like '$'.
       - For example, transform "3cm" into "3 cm" or "$20" into "$ 20", ensuring that numbers and their associated units or symbols are separated by a space.

    4. Adjust number formatting by:
       - Removing characters used as thousands separators such as commas (',') or apostrophes ('’', '`').
       - Standardizing decimal points by replacing commas with dots ('.').

    5. Assign a unique variable name to each unique numeric value.
       Each number, once identified and formatted correctly, is replaced by a unique variable name,
       ensuring that each numeric value is distinctly represented by a variable in the transformed text.

    Parameters:
        q (str): The math word problem as a string.

    Returns:
        tuple: The transformed expression with variables replacing numbers, and a dictionary mapping variables to original numeric values.
    """
    variable_names = generate_variable_names(limit=26) # TODO: Dynamically adjust the limit when we run out of variable names.
    var_index = 0
    mapping = {}
    reverse_mapping = {}
    
    # 1. Split the text to isolate numbers and mathematical operators.
    elements = [split for element in q.split() for split in re.split(r'([+\-*/=^()])', element) if split]

    # 2. Process each element from the split to detect numeric values.
    processed_elements = []
    for element in elements:
        numeric_match = re.match(r'([^\d]*)(\d[\d,.\'`]*)([^\d]*)', element)
        # 3. Segments that include numeric values with potential non-numeric substrings at the beginning or end
        if numeric_match:
            prefix, number, suffix = numeric_match.groups()
            # 4. Adjust number formatting
            if re.match(r"^\d{1,3}(?:(?:[,'`]\d{3})*|\d*)(?:\.\d+)?$", number):
                number = re.sub(r"[,'`]", "", number)
            number = number.replace(',', '.')   
            # 5. Assign a unique variable name to each unique numeric value.
            if number not in reverse_mapping:
                variable_name = variable_names[var_index]
                mapping[variable_name] = float(number)
                reverse_mapping[float(number)] = variable_name
                var_index += 1
            if prefix != '': processed_elements.append(prefix)
            processed_elements.append(reverse_mapping[float(number)])
            if suffix != '': processed_elements.append(suffix)
        else:
            processed_elements.append(element)
    final_expression = " ".join(processed_elements)
    return final_expression, mapping