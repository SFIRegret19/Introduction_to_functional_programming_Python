def apply_all_func(int_list, *functions):
    results = {}

    for function in functions:
        results.update({function.__name__: function(int_list)})
    
    return results

def _min(_list):
    return min(_list)

def _max(_list):
    return max(_list)

def _len(_list):
    return len(_list)

def _sum(_list):
    return sum(_list)

def _sorted(_list):
    return sorted(_list)

print(apply_all_func([6, 20, 15, 9], _max, _min))
print(apply_all_func([6, 20, 15, 9], _len, _sum, _sorted))