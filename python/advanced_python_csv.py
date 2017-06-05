import csv
import re
f = open("/Users/lqa/Desktop/Metis/prework/dsp/python/faculty.csv", 'r')
faculty = list(csv.reader(f))
faculty = faculty[1:]

email = []
for f in faculty:
  email.append(f[3].strip())
  
with open("emails.csv", "w") as f:
  writer = csv.writer(f, delimiter=',', lineterminator ='\r\n')
  for email in email:
    writer.writerow([email])
