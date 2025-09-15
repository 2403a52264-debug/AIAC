import csv

with open('input.csv', newline='') as infile:
    reader = csv.DictReader(infile)
    rows = list(reader)

for row in rows:
    row['salary'] = int(row['salary'])

sorted_rows = sorted(rows, key=lambda r: (r['dept'], -r['salary']))

with open('output.csv', 'w', newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=['name', 'dept', 'salary'])
    writer.writeheader()
    for row in sorted_rows:
        writer.writerow({'name': row['name'], 'dept': row['dept'], 'salary': row['salary']})