import os

from datetime import datetime


if __name__ == "__main__":
    n_days_to_delete = 10
    for root, dirs, files in os.walk('./dir'):
        for file in files:
            file_full_path = os.path.join(root, file)
            if (
                datetime.now() -
                datetime.fromtimestamp(
                    os.path.getmtime(file_full_path)
                )
            ).days > n_days_to_delete:
                os.remove(file_full_path)
