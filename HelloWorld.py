#merge two array using Binary sorted

def merge(a, b):
    i = 0
    j = 0
    c = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    if i < len(a):
        c.extend(a[i:])
    if j < len(b):
        c.extend(b[j:])
    return c

if __name__ == '__main__':
    a = [1, 3, 5, 7, 9]
    b = [2, 4, 6, 8, 10]
    print(merge(a, b))


#sorting the elements using binary search

def binary_search(a, x):
    l = 0
    r = len(a) - 1
    while l <= r:
        m = (l + r) // 2
        if a[m] == x:
            return m
        elif a[m] < x:
            l = m + 1
        else:
            r = m - 1
    return -1

if __name__ == '__main__':
    a = [1, 3, 5, 7, 9]
    print(binary_search(a, 7))


# finding the index of the first occurrence of a number in a sorted array

def first_occurrence(a, x):
    l = 0
    r = len(a) - 1
    while l <= r:
        m = (l + r) // 2
        if a[m] == x and (m == 0 or a[m - 1] < x):
            return m
        elif a[m] < x:
            l = m + 1
        else:
            r = m - 1
    return -1

if __name__ == '__main__':  
    a = [1, 3, 5, 7, 7, 7, 9]
    print(first_occurrence(a, 7))

# finding the index of the last occurrence of a number in a sorted array

def last_occurrence(a, x):
    l = 0
    r = len(a) - 1
    while l <= r:
        m = (l + r) // 2
        if a[m] == x and (m == len(a) - 1 or a[m + 1] > x):
            return m
        elif a[m] > x:
            r = m - 1
        else:
            l = m + 1
    return -1

if __name__ == '__main__':
    a = [1, 3, 5, 7, 7, 7, 9]
    print(last_occurrence(a, 7))


# finding the smallest five elements in a sorted array in O(n) time

def smallest_five(a):
    if len(a) < 5:
        return a
    return a[:5]

if __name__ == '__main__':
    a = [1,2]
    print(smallest_five(a))

    











         
    









