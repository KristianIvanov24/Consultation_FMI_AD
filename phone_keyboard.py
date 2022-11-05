nums = [7, 9, 9, 9, 8, 4, 4, 6, 6, 6, -1, 6, 6]

phone = {1: '', 11: '', 111: '', 2: 'A', 22: 'B', 222: 'C', 3: 'D', 33: 'E', 333: 'F',
         4: 'G', 44: 'H', 444: 'I', 5: 'J', 55: 'K', 555: 'L', 6: 'M', 66: 'N', 666: 'O',
         7: 'P', 77: 'Q', 777: 'R', 7777: 'S', 8: 'T', 88: 'U', 888: 'V', 9: 'W', 99: 'X', 999: 'Y', 9999: 'Z', 0: ' '}

text = ''
number = nums[0]
for i in range(1, len(nums)):
    if nums[i] == -1:
        text += phone[number]
    elif nums[i-1] == -1:
        number = nums[i]
    elif number % 10 == nums[i]:
        number = number * 10 + nums[i]
    else:
        text += phone[number]
        number = nums[i]

text += phone[number]

print(text)
