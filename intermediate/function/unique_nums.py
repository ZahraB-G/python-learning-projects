def unique_nums(*args):
    # result = []
    # for item in args:
    #     if item not in result:
    #         result.append(item)
    # result.sort()
    # return result
    result = set(args)
    return list(result)

print(unique_nums(1,2,4,5,3,3,3,5,2))
print(unique_nums(9,8,8,4,23,12,12,5,2))