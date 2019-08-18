def flip(some_list):
    if len(some_list) == 1:
        return some_list

    else:
        next_list = some_list[:len(some_list)-1]
        last_list = some_list[len(some_list)-1:len(some_list)]

        return last_list + flip(next_list)
        
some_list = [1, 2]
some_list = flip(some_list)
print(some_list)