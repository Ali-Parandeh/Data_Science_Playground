# Refactor the code below:

            # sequenceString = "53,242,145,24,23,242,11,17,5,3"
            # targetNumber = 250

            # sequenceList = sequenceString.split(",")

            # lengthOfSequence = len(sequenceList)

            # unsortedListOfNumbers = [int(num) for num in sequenceList]

            # sorted_list_of_numbers = []

            # while unsortedListOfNumbers:
            #     minimum = unsortedListOfNumbers[0]  # arbitrary number in list
            #     for x in unsortedListOfNumbers:
            #         if x < minimum:
            #             minimum = x
            #     sorted_list_of_numbers.append(minimum)
            #     unsortedListOfNumbers.remove(minimum)

            # total = 0
            # counter = 0
            # for num in unsortedListOfNumbers:
            #     if total < targetNumber:
            #         total += int(num)
            #         counter += 1

            # print(total)
            # print(counter)
            # print(unsortedListOfNumbers)

def Refactored_Code(sequenceString, targetNumber):
    '''
    Take a sequence of numbers in string format and a target value.
    Then sort the list of numbers and add them up from the smallest to largest until
    you hit the target Value or go over it. How many numbers did you sum togther to reach the target value?
    Print out the sorted list of numbers, the count of add operations and the total sum.
    '''
    # Create a list of integer numbers and sort it
    ListOfNumbers = [int(num) for num in sequenceString.split(",")]
    ListOfNumbers.sort()

    total = 0
    counter = 0
    # Loop over the sorted list of numbers and add up values until you reach the target value
    # Keep track of how many numbers you add.
    for num in ListOfNumbers:
        if total < targetNumber:
            total += int(num)
            counter += 1

    # print the results
    print(total)
    print(counter)
    print(ListOfNumbers)


Refactored_Code("53,242,145,24,23,242,11,17,5,3", 250)

# OUTPUT
# ==================
# 281
# 8
# [3, 5, 11, 17, 23, 24, 53, 145, 242, 242]