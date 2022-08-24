class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        for day in range(n):
            for future_day in range(day + 1, n):
                if temperatures[future_day] > temperatures[day]:
                    answer[day] = future_day - day
                    break      
                
        return answer
