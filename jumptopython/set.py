#집합 자료형으로 원소간 중복을 허락하지 않으며 순서가 없다.

set1 = set([1,2,3])

set2 = set([3,4,5])

print(set1,set2)

print (set1 & set2)

print (set1 | set2)

set1.add(4)
set1.update([3,7,8,9])
set1.remove(1)

print(set1)