# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up
# example 0
# Given list is [2,3,6,6,5]. The maximum score is 6, second maximum is 5. Hence, we print 5 as the runner-up score.

def runner_up(arr):
    unique_arr = list(set(arr))
    max1 = max(unique_arr)
    idx = unique_arr.index(max1)
    del(unique_arr[idx])
    return max(unique_arr)


print(runner_up([2,3,6,6,5]))