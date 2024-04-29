import re

def generating_algebraic_template(q: str):
    names = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    pattern = re.compile(r"([-+]?[\$\£\€]?[a-zA-Z]*\b\d+\b[a-zA-Z]*)")
    map = {}
    matches = re.findall(pattern, q)
    current_var_index = 0
    for full_match in matches:
        var_name = names[current_var_index]
        current_var_index += 1
        # Replace the full matched expression with a variable
        q = q.replace(full_match, var_name, 1)  # Remove only the first exact occurrence
        # Extract numeric value and ignore both preceding and following non-numeric parts
        numeric_value = re.search(r"[+-]?\d*\.\d+|\d+", full_match)
        if numeric_value:
            map[var_name] = float(numeric_value.group())
        if current_var_index >= len(names):
            # TODO: Handle this case by using another set of variable names
            raise Exception("Not enough variable names for the numbers in the question")
    return q, map