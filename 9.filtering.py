import numpy as np

# Filtering = Refers to the process of selecting elements
#             from an array that match a given condition

ages = np.array([[21,17,19,20,16,30,18,65],
                 [39,22,15,99,18,19,20,21]])

# Filtering data by using condition
teenagers = ages[ages < 18]
adults = ages[(ages >= 18) & (ages < 65)]
seniors = ages[ages >= 65]
evens = ages[ages % 2 == 0]
odds = ages[ages % 2 != 0]

print(f"teenagers: {teenagers}")
print(f"adults: {adults}")
print(f"seniors: {seniors}")
print(f"even: {evens}")
print(f"odds: {odds}")

adults1 = np.where(ages >= 18, ages, 0) # 0 here is replace all element that don't satisfy the condition is replaced by 0

print(adults1)