import numpy

def binarr2binstr(arr):
    if type(arr) == numpy.ndarray:
        arr = arr.tolist()
    match arr:
        case []:
            return ""
        case [True, *tail]:
            return "1" + binarr2binstr(tail)
        case [False, *tail]:
            return "0" + binarr2binstr(tail)
        case [1, *tail]:
            return "1" + binarr2binstr(tail)
        case [0, *tail]:
            return "0" + binarr2binstr(tail)

def solve(data):
    total_entry = len(data)
    gamma_rate_array = sum(data) > total_entry / 2
    gamma_int = int(binarr2binstr(gamma_rate_array.tolist()), base=2)
    epsilon_rate_int = int(binarr2binstr(numpy.logical_not(gamma_rate_array).tolist()), base=2)
    return gamma_int * epsilon_rate_int

def sub_solve2(data, solve_type, offset=0):
    total_entry = len(data)
    if total_entry == 1:
        return binarr2binstr(data[0])
    match solve_type, (sum(data) >= total_entry / 2)[offset]:
        case "oxygen", is_one:
            filtered_data = data[numpy.array(data)[:,offset] == int(is_one)]
            return sub_solve2(filtered_data, solve_type, offset+1)
        case "co2", is_one:
            filtered_data = data[numpy.array(data)[:,offset] == int(not is_one)]
            return sub_solve2(filtered_data, solve_type, offset+1)

def solve2(data):
    data = numpy.array(data)
    oxygen_last_entry = sub_solve2(data, "oxygen")
    oxygen_int = int(oxygen_last_entry, base=2)
    co2_last_entry = sub_solve2(data, "co2")
    co2_int = int(co2_last_entry, base=2)
    return oxygen_int * co2_int

with open("d3/input", "r") as f:
    data = [numpy.array(list(map(int, line))) for line in f.read().splitlines()]
    print(solve(data))
    print(solve2(data))
