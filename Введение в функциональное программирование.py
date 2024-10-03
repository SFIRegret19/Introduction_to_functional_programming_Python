def apply_all_func(int_list, *functions):
    int_list = list_converter(int_list)
    results = {}

    for function in functions:
        results.update({function.__name__: function(int_list)})

    return results

def list_converter(_list):
    for i in range(len(_list)):
        if isinstance(_list[i], int) or isinstance(_list[i], float):
            continue
        elif str(_list[i]).find('.').__eq__(True):
            _list.insert(i, float(_list.pop(i)))
        else:
            _list.insert(i, int(_list.pop(i)))
    return _list

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
