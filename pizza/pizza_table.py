from tabulate import tabulate
import csv
import sys
ls = []
try:
    if len(sys.argv) == 2 and ".csv" in sys.argv[1]:
        with open(sys.argv[1],"r") as f:
            reader = csv.DictReader(f,fieldnames=["Sicilian Pizza","Small","Large"])



            for row in reader:
                 ls.append(row)
            headers = ls[0]
            print(headers)
            lista = ls[1:]
            print(tabulate(lista, headers, tablefmt="outline"))


    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    else:
        sys.exit("Not a CSV file ")
except FileNotFoundError:
    sys.exit("File does not exist")