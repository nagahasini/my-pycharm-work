def cocobanana_sum(n):
    """
    Returns the sum of all numbers from 1 to n
    that are divisible by 3 or 5 (Coco or Banana).
    """
    total = 0
    for i in range(1, n + 1):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

# Example usage:
if __name__ == "__main__":
    num = int(input("Enter a number: "))
    result = cocobanana_sum(num)
    print("Coco-Banana Sum up to", num, "is:", result)
