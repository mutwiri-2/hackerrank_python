# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up
# example 0
# Given list is [2,3,6,6,5]. The maximum score is 6, second maximum is 5. Hence, we print 5 as the runner-up score.

def runner_up(arr):
    unique_arr = list(set(arr))
    max1 = max(unique_arr)
    idx = unique_arr.index(max1)
    del(unique_arr[idx])
    return max(unique_arr)

# cleaner solution
# sorted() returns a new list with the numbers in the array sorted in ascending order (does not alter the original list) - different from .sort() list method, which sorts the list in place - mutates the list
def runner_up(arr):
    no_duplicates_arr = list(set(arr))
    runner_up_score = sorted(no_duplicates_arr)[-2]
    return runner_up_score


print(runner_up([2,3,6,6,5]))