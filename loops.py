# iterating a list

nums = [1,2,3,4,5,6];

for num in nums:
    print(num);

# range function is used for index based iteration
# as python doesn't provide implicit index based iteration

for index in range(5):
    print(num[index]);

# range(5) = [0,1,2,3,4,5], useful when you need a simple iteration
# range(5,10) = [5,6,7,8,9], useful when you wish to have your own starting point
# range(5, 10, 2) = [5,7,9], useful when you want to have your own step factor

# break and continue works similar to JS
# while loop works the same as well