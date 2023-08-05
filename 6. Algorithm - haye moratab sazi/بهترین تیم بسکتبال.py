heights = list(map(int,input().split()))

index_finder = heights.copy()
heights.sort()
top3 = []
for i in range(1,4):
  print(f"شماره {index_finder.index(heights[-i])+1} با قد {heights[-i]}")

