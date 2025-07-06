# def balanced(numbers):
#     result = set()

#     # Bruteforce
#     for i in range(len(numbers)):
#         for j in range(i+1, len(numbers)):
#             current_sum = numbers[i] + numbers[j]

#             for idx1 in range(len(numbers)):
#                 for idx2 in range(idx1+1,len(numbers)):
#                     if idx1 != i and idx2 != j:
#                         if numbers[idx1]+numbers[idx2] == current_sum:
#                             result.add(numbers[idx1])
#                             result.add(numbers[idx2])

#     return result

# Hashtable approach
def balanced(numbers):
    sum_map = {}

    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            current_sum = numbers[i] + numbers[j]
            
            # Updates sum-map with current_sum
            if current_sum in sum_map:
                sum_map[current_sum].append(numbers[i])
                sum_map[current_sum].append(numbers[j])
            
                return set(sum_map[current_sum])
            
            # Initiate the key/value in sum_map
            else:
                sum_map[current_sum] = [numbers[i], numbers[j]]

    return set()


numbers= [3, 10, 4, 5, 2, 14]
print(balanced(numbers))
assert balanced([3, 10, 4, 5, 2, 14]) == set([3, 2, 4, 5])

assert balanced([60, 0, 10, -35, 90]) == set()

assert balanced([]) == set()

print("All tests passed!")
print("Discuss time & space complexity if time remains.")
