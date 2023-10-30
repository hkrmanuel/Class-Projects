def lower_upper_count(s):
    lower_count = 0
    upper_count = 0
    uppercase = s.upper()
    lowercase = s.lower()
    for c in s:
        if c in uppercase:
            upper_count += 1
        elif c in lowercase:
            lower_count += 1
    new_dict = dict()
    new_dict["lower"] = lower_count
    new_dict["upper"] = upper_count
    return new_dict
print(lower_upper_count("kWAme Bamfo"))