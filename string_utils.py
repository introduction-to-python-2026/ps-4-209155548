
def split_before_each_uppercases(formula):
    return re.findall(r'[A-Z][a-z0-9]*', formula)



def split_at_first_digit(formula):
    match = re.search(r'\d', formula)
    if not match:
        return formula, ""  # אם אין ספרות
    idx = match.start()
    return formula[:idx], formula[idx:]
