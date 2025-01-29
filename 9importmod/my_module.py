print("imporeted moduls..")
test ='test string'


def find_index(to_serch, target):
    for i, value in  enumerate(to_serch):
        if value == target:
            return i
        
    return -1