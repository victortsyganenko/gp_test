import csv


if __name__ == "__main__":
    unique_rows = {}
    with open('./task_1.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='|')
        next(reader)
        for row in reader:
            unique_rows['|'.join(row)] = row
    print(list(unique_rows.values()))
