import csv
import sys
try:
    if len(sys.argv) == 3 and sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):
        with open(sys.argv[1], "r") as f:
            reader = csv.DictReader(f)
            with open(sys.argv[2], "w", newline="") as fa:
                writer = csv.DictWriter(fa, fieldnames=["last", "first", "house"])
                writer.writeheader()

                for row in reader:
                    last = row["name"].split(",")[0]
                    first = row["name"].split(",")[-1].strip()
                    house = row["house"]
                    writer.writerow({"last": last, "first": first, "house": house})
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Not a CSV file ")
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")
