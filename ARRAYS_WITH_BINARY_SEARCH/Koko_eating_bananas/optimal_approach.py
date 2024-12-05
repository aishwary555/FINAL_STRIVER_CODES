import math

def calculate_total(arr,hourly):
    
    total_hours = 0
    for pile in arr:
        total_hours += (pile + hourly - 1) // hourly  # Efficient way to calculate ceil(pile / div)
    return total_hours


def coco(arr,h):
    
    low = 1
    high = max(arr)
    ans = -1
    
    while low <= high :
        mid = (low + high) // 2
        total_sum = calculate_total(arr,mid)
        if(total_sum <= h):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

piles = [30,11,23,4,20]
h = 6
res = coco(piles,h)
print(res)