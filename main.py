def balanced(numbers):

    # get the length of the array
    length = len(numbers)

    # create an empty dictionary to map a sum to the elements that make up that sum
    map = {}

    # loop through each element of the array
    for i in range(length):
        # loop through i+1th element to end of array
        # we exclude 0...i since we have already found the sum of i + 0...i-1
        for j in range(i+1, length):

            # find the sum of ith and jth elements 
            sum = numbers[i] + numbers[j]

            # if that sum has already been seen
            if sum in map:
                # add the elements just summed to value of map[sum]
                map[sum].append(numbers[i])
                map[sum].append(numbers[j])

                # return the answer as a set
                return set(map[sum])
            # if sum has not already been seen
            else:
                # set the sum as a new key
                # add the elements just summed as the value
                map[sum] = [numbers[i], numbers[j]]

    # if no answer has been found, return an empty set
    return set()


assert balanced([3, 10, 4, 5, 2, 14]) == set([3, 2, 4, 5])

assert balanced([60, 0, 10, -35, 90]) == set()

assert balanced([]) == set()

print("All tests passed!")
print("Discuss time & space complexity if time remains.")
