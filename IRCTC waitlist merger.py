"""3) Merge Sort — The IRCTC Waitlist Merger
IRCTC has two separately sorted waitlists — one from its mobile app, one from railway counters.
To produce a final unified waitlist, they don't re-sort from scratch.
They merge both sorted lists in one pass — compare the front of each list, pick the smaller token,
 and advance.
This is exactly merge sort's merge step."""
l1 = [3, 5, 7, 12]
l2 = [1, 8, 9, 13]

i =0
j = 0
merged = []

while i < len(l1) and j < len(l2):
    if l1[i] < l2[j]:
        merg.append(l1[i])
        i += 1
    else:
        merg.append(l2[j])
        j += 1

merg.extend(l1[i:])
merg.extend(l2[j:])

print(merg)
