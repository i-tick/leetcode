class Solution:
    def diet_plan_performance(calories, k, lower, upper):
        points = 0
        current_sum = sum(calories[:k])

        if current_sum < lower:
            points -= 1
        elif current_sum > upper:
            points += 1

        for i in range(k, len(calories)):
            current_sum = current_sum - calories[i - k] + calories[i]
            if current_sum < lower:
                points -= 1
            elif current_sum > upper:
                points += 1

        return points