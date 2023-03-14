

def print_blank_line():
    print('')


def convert_tuple_to_str(t) -> str:
    values = list(t)
    str_values = ", ".join(str(i) for i in values)
    return str_values


def header_to_str(description):
    header = [i[0] for i in description]
    header_str = ", ".join(header)
    return header_str
