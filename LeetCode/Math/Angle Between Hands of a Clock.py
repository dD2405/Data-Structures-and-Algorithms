''' Input: hour = 3, minutes = 15
Output: 7.5

Example 4:

Input: hour = 4, minutes = 50
Output: 155

Example 5:

Input: hour = 12, minutes = 0
Output: 0 '''

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_angle = (hour*60 + minutes) * 0.5
        minutes_angle = minutes * 6
        
        angle = abs(hour_angle - minutes_angle)
        min_angle = min(360-angle, angle)
        
        return min_angle
        
