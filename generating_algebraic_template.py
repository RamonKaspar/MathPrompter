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

def extract_numeric_value(text):
    """ Extracts the first found numeric value from the text. """
    numeric_value = re.search(r'[-+]?\d*\.?\d+', text.replace(',', ''))
    return float(numeric_value.group()) if numeric_value else None

def generating_algebraic_template(q):
    variable_names = generate_variable_names()
    pattern = re.compile(r"\s*([-+]?\s*[\$£€]?[\s]*\b\d[\d,]*\.?\d*\b)\s*")
    matches = re.findall(pattern, q)
    mapping = {}
    num_to_var = {}
    transformed_question = q
    idx = 0
    
    for full_match in matches:
        numeric_value = extract_numeric_value(full_match)
        if numeric_value not in num_to_var:
            if idx >= len(variable_names):
                raise OverflowError("Not enough variable names available.")
            num_to_var[full_match] = variable_names[idx]
            idx += 1
        var_name = num_to_var[full_match]
        mapping[var_name] = numeric_value
        transformed_question = transformed_question.replace(full_match,var_name, 1)
    
    return transformed_question, mapping