

if __name__ == "__main__":
    a = [[1, 2, 3], [4, 5, 6]]
    print(
        [{f'k{idx + 1}': num for idx, num in enumerate(a_item)} for a_item in a]
    )
