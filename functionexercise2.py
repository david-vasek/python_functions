# Find the smallest number
def find_smallest_number(list_of_number):
    smallest = list_of_number[0]
    for num in list_of_number:
        print("current number: " + str(num))
        print("smallest is: " + str(smallest))
        if num < smallest:
            print("current is smaller than smallest!!")
            smallest = num
    return smallest

print("The smallest number is: " + str(find_smallest_number([1,2,3,4,5,6,7,8,9,10])))


# ================================================================================================================================


# Find the largest number
def find_largest_number(list_of_number):
    largest = list_of_number[0]
    for num in list_of_number:
        print("current number: " + str(num))
        print("largest is: " + str(largest))
        if num > largest:
            print("current is the largest out of the list!!")
            largest = num
    return largest

print("The largest number is: " + str(find_largest_number([1,2,3,4,5,6,7,8,9,10])))


# ================================================================================================================================


# # Find the shortest string
def shortest_string(list_of_strings): 
    shortest = str(1e99)
    for string in list_of_strings:
        if len(string) < len(shortest):
            shortest = string
    print(shortest)

shortest_string(["apple", "banana", "carrot cake"])


# ================================================================================================================================


# # Find the longest string
def longest_string(list_of_strings): 
    longest = str(num)
    for string in list_of_strings:
        if len(string) > len(longest):
            longest = string
    print(longest)

shortest_string(["apple", "banana", "carrot cake"])


# ================================================================================================================================