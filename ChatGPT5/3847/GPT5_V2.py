"""Calculate the score difference between two players."""

class Solution(object):
"""Calculate the score difference according to the game rules."""

```
# pylint: disable=too-few-public-methods

def scoreDifference(self, nums):  # pylint: disable=invalid-name
    """
    Calculate the first player's score minus the second player's score.

    :type nums: List[int]
    :rtype: int
    """
    first_score = 0
    second_score = 0
    first_player_active = True

    for game_index, points in enumerate(nums):
        # Odd points switch the active player.
        if points % 2 == 1:
            first_player_active = not first_player_active

        # Every sixth game switches the active player again.
        if (game_index + 1) % 6 == 0:
            first_player_active = not first_player_active

        # Award the points to the currently active player.
        if first_player_active:
            first_score += points
        else:
            second_score += points

    return first_score - second_score
```
