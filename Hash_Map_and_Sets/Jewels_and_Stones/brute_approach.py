def numJewelsInStones (jewels: str, stones: str) -> int:
        count = 0
        for stone in stones:
            if stone in jewels:
                count += 1
        return count
    
jewels = "aA"
stones = "aAAbbbb"
res = numJewelsInStones(jewels,stones)
print(res)