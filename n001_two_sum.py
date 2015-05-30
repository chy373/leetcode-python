#Given an array of integers, find two numbers such that they add up to a specific target number.
#solution: use hashmap; enumerate() with the start of index is 1
def two_sum(nums, target):
    s = {}
    for value, key in enumerate(nums,1):
        sub = s.get(target-key)
        if sub != None:
            return sub, value
        else:
            s[key] = value

if __name__ == '__main__':
    nums = [1,1,2]
    target = 2
    print two_sum(nums,target)
