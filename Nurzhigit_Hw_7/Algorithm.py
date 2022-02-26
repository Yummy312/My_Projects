from random import shuffle
import random
nums = [2, 4, 6, 7, 1, 3, 9, 6, 8, 5, 10]
random.shuffle(nums)
print(f'Исходный массив:{nums}')


def buble_sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return print(f'Отсортированный массив:{nums}')


buble_sort(nums)

numbers = [20, 34, 56, 88, 94, 11, 5, 9, 44, 75]
random.shuffle(numbers)
print(f'Исходный массив{numbers}')


def selection_sort(numbers):
    for num in range(len(numbers)):
        min_value = num

        for item in range(num, len(numbers)):
            if numbers[min_value] > numbers[item]:
                min_value = item
        numbers[num], numbers[min_value] = numbers[min_value], numbers[num]
    return print(f'Отсортированный массив{numbers}')


selection_sort(numbers)


