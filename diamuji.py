def simple_diamond(n): 
    total_rows = 2* n-1
    for i in range(total_rows):
        distance=abs (i - n - 1)
        spaces=distance 
        stars=total_rows - 2* distance
        print(" "* spaces + "*" * stars)
        
print("\nDiamond Pattern (n=5): ")
simple_diamond(5)