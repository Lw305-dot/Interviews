def find_duplicate_elements(numbers):
    duplicates=[]
    seen=set()
    for num in numbers:
        if num in seen:
            duplicates.append(num)
        else:
            seen.add(num)
    return duplicates

numbers = [1, 2, 3, 2, 4, 3,6,4,4,6, 5]
print(find_duplicate_elements(numbers))
#When solving problems involving duplicates, think about using a set first. 
# Sets provide average O(1) membership checks, which often help you reduce an O(n²)
 solution to O(n).