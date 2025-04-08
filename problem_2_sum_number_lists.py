from testhelper import test

def sum_number_lists(list1, list2):
    list3 = []
    num = 0
    if len(list1) == len(list2):
        for i in range(len(list1)):
            listot = int(list1[num]) + int(list2[num])
            list3.append(listot)
            num = num + 1
        print(list3)
    else:
        print("List sizes are not equal")
    return(list3)



### TESTS - Run the code that calls the function to check it works.
test("Sum number lists 1", [4,5,7,8,10,11,13], sum_number_lists([1,2,3,4,5,6,7], [3,3,4,4,5,5,6]))
test("Sum number lists 2", [11,12,13,14,15,16,17], sum_number_lists([1,2,3,4,5,6,7], [10,10,10,10,10,10,10]))
