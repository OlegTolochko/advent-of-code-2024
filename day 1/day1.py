import math
input = open("input.txt", "r")
left = []
right = []
for line in input.readlines():
    segment1, segment2 = line.strip("\n").split("   ")
    left.append(int(segment1))
    right.append(int(segment2))

left.sort()
right.sort()
total_dist = 0
for l, r in zip(left,right):
    dist = math.sqrt((l-r)**2)
    total_dist += dist

print(total_dist)

similarity_score = 0
for l in left:
    similarity = right.count(l)
    similarity_score += similarity*l

print(similarity_score)