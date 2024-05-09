
def print_merged_str(s1: str, s2: str, min_merge_criteria: int = 1) -> None:
    if s1 != s2:
        cut_l = min(len(s1), len(s2))
        while cut_l >= min_merge_criteria:
            s1_end = s1[-cut_l:]
            s2_start = s2[:cut_l]
            if s1_end == s2_start:
                print(s1 + s2[cut_l:])
                break
            else:
                cut_l -= 1

    return None


if __name__ == "__main__":

    with open('./task_5.txt', 'r', encoding='utf-8') as f:
        items = [row.strip() for row in f]

    input_item = input('Введите слово: ')
    for item in items:
        print_merged_str(input_item, item)
