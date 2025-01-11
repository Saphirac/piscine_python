def give_bmi(height: list[float], weight: list[float]) -> list[float]:
    return [x[1]/(x[0]**2) for x in zip(height, weight)]

def apply_limit(bmi: list[float], limit: int) -> list[bool]:
    return [x > limit for x in bmi]

height = [2.71, 1.15]
weight = [165.3, 38.4]
bmi = give_bmi(height, weight)

print(bmi, type(bmi))
print(apply_limit(bmi, 26))
