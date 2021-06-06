from typing import List


def hamming_distance(
    previous_generation: List[int], current_generation: List[int]
) -> int:
    prev_len: int = len(previous_generation)
    curr_len: int = len(current_generation)
    bonus_distance: int = 0
    small: List[int] = previous_generation
    large: List[int] = current_generation
    if prev_len > curr_len:
        bonus_distance = prev_len - curr_len
        small = current_generation
        large = previous_generation
    elif prev_len < curr_len:
        bonus_distance = curr_len - prev_len
    total_hamming_distance: int = 0
    for ix in range(len(small)):
        if small[ix] != large[ix]:
            total_hamming_distance += 1
    return total_hamming_distance + bonus_distance
