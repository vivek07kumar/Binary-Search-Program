# Limitation of the below written binary search function -:
# >> It requires List to be pre-sorted ither from smallest to greatest or from greatest to smallest.
def binary_search_smallest_to_greatest(user_list,user_query) :
    first = 0
    last = len(user_list) - 1
    if user_query >= user_list[first] and user_query <= user_list[last] :
        length = 2
        while length > 1 :
            length = (last + 1) - first 
            mid =  first + (length // 2)
            if user_list[mid] == user_query :
                c = True
                d = True
                small,great = mid,mid
                if mid > 0 :
                    while c and small > 0 :
                        small = small - 1
                        if user_list[small] < user_list[mid] :
                            c = False
                else :
                    small = mid
                if mid < len(user_list) - 1 :
                    while d and great < len(user_list) - 1 :
                        great = great + 1
                        if user_list[great] > user_list[mid] :
                            d = False
                else :
                    great = mid
                if user_list[small] == user_list[mid] :
                    index = small - 1
                    final_list = []
                    while index < (great - 1) :
                        index = index + 1
                        final_list = final_list + [index]
                elif user_list[great] == user_list[mid] :
                    index = small
                    final_list = []
                    while index < great :
                        index = index + 1
                        final_list = final_list + [index]
                else :
                    index = small
                    final_list = []
                    while index < (great - 1) :
                        index = index + 1
                        final_list = final_list + [index]
                return final_list
            elif user_query < user_list[mid] :
                last = mid - 1
            else :
                first = mid + 1
    return None
def binary_search_greatest_to_smallest(user_list,user_query) :
    first = 0
    last = len(user_list) - 1
    if user_query <= user_list[first] and user_query >= user_list[last] :
        length = 2
        while length > 1 :
            length = (last + 1) - first 
            mid =  first + (length // 2)
            if user_list[mid] == user_query :
                c = True
                d = True
                small,great = mid,mid
                if mid > 0 :
                    while c and great > 0 :
                        great = great - 1
                        if user_list[great] > user_list[mid] :
                            c = False
                else :
                    great = mid
                if mid < len(user_list) - 1 :
                    while d and small < len(user_list) - 1 :
                        small = small + 1
                        if user_list[small] < user_list[mid] :
                            d = False
                else :
                    small = mid
                if user_list[small] == user_list[mid] :
                    index = great
                    final_list = []
                    while index < small :
                        index = index + 1
                        final_list = final_list + [index]
                elif user_list[great] == user_list[mid] :
                    index = great - 1
                    final_list = []
                    while index < small - 1 :
                        index = index + 1
                        final_list = final_list + [index]
                else :
                    index = great
                    final_list = []
                    while index < small - 1 :
                        index = index + 1
                        final_list = final_list + [index]
                return final_list
            elif user_query < user_list[mid] :
                first = mid + 1
            else :
                last = mid - 1
    return None
def main() :
    from time import time
    user_list = list(eval(input('>> Please enter numbers seperated by comma : ')))
    user_query = eval(input('>> Please enter a number to search in the List : '))
    print()
    user_input = input('>> If the List is Sorted from smallest to greatest then input y, or if List is Sorted from greatest to smallest then input n : ')
    print()
    if user_input == 'y' or user_input == 'Y' :
        start = time()
        result_1 = binary_search_smallest_to_greatest(user_list,user_query)
        end = time()
        print()
        if result_1 != None :
            print('--> ',user_query,'is present at following index postion/s : ',result_1)
            print('--> Total Number of element Found : ',len(result_1))
            print('--> Time Taken : ',end - start,'Seconds')
        else :
            print('--> ',user_query,'Not Found In The Given List !')
    elif user_input == 'n' or user_input == 'N' :
        start = time()
        result_2 = binary_search_greatest_to_smallest(user_list,user_query)
        end = time()
        print()
        if result_2 != None :
            print('--> ',user_query,'is present at following index postion/s : ',result_2)
            print('--> Total Number of element Found : ',len(result_2))
            print('--> Time Taken : ',end - start,'Seconds')
        else :
            print('--> ',user_query,'Not Found In The Given List !')
    else :
        print('>> WRONG INPUT ! <<')
    print()
main()
