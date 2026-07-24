from collections import deque

class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        # max_deque speichert Indizes von Elementen in absteigender Reihenfolge (Maximum vorne)
        max_deque = deque()
        # min_deque speichert Indizes von Elementen in aufsteigender Reihenfolge (Minimum vorne)
        min_deque = deque()
        
        left = 0
        total_count = 0
        
        for right in range(n):
            # Update max_deque: Entferne Elemente, die kleiner als das aktuelle sind
            while max_deque and nums[max_deque[-1]] <= nums[right]:
                max_deque.pop()
            max_deque.append(right)
            
            # Update min_deque: Entferne Elemente, die größer als das aktuelle sind
            while min_deque and nums[min_deque[-1]] >= nums[right]:
                min_deque.pop()
            min_deque.append(right)
            
            # Prüfe, ob die Kosten des aktuellen Fensters [left, right] <= k sind.
            # Wenn nicht, verschiebe den 'left'-Zeiger nach rechts.
            while left <= right:
                current_max = nums[max_deque[0]]
                current_min = nums[min_deque[0]]
                length = right - left + 1
                
                if (current_max - current_min) * length <= k:
                    break
                
                left += 1
                # Entferne Indizes aus den Deques, die nicht mehr im Fenster sind
                if max_deque[0] < left:
                    max_deque.popleft()
                if min_deque[0] < left:
                    min_deque.popleft()
            
            # Alle Subarrays, die bei 'right' enden und an oder nach 'left' beginnen, 
            # erfüllen ebenfalls die Bedingung (da sie kürzer sind).
            total_count += (right - left + 1)
            
        return total_count
