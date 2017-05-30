# Faculty Problem (Regular expression)
import csv
import re
f = open("/Users/lqa/Desktop/Metis/prework/dsp/python/faculty.csv", 'r')
faculty = list(csv.reader(f))
faculty = faculty[1:]
faculty


# Q1

Phd = 0
ScD = 0
MPH = 0
MS = 0
BSEd = 0
JD = 0
MA = 0

for f in faculty:
    if re.search("PhD|Ph.D.|Ph.D", f[1].strip()) != None:
        Phd += 1
    if re.search("ScD|Sc.D.", f[1].strip()) != None:
        ScD += 1
    if re.search("MA", f[1].strip()) != None:
        MA += 1
    if re.search("MPH", f[1].strip()) != None:
        MPH += 1
    if re.search("JD", f[1].strip()) != None:
        JD += 1
    if re.search("B.S.Ed.", f[1].strip()) != None:
        BSEd += 1
    if re.search("M.S.|MS", f[1].strip()) != None:
        MS += 1
print('PhD: ' + str(Phd))
print ('ScD: ' + str(ScD))
print ('MA: ' + str(MA))
print ('MPH: ' + str(MPH))
print ('JD: ' + str(JD))
print ('BSEd: ' + str(BSEd))
print ('MS: ' + str(MS))


# Q2
Professor = 0
Associate = 0
Assistant = 0
for f in faculty:
    if re.search("^Associate", f[2].strip()) != None:
        Associate += 1
    if re.search("^Assistant", f[2].strip()) != None:
        Assistant += 1
    if re.search("^Professor", f[2].strip()) != None:
        Professor += 1

print ('Professor of Biostatistics: ' + str(Professor))
print ('Associate Professor of Biostatistics: ' + str(Associate))
print ('Assistant Professor of Biostatistics: ' + str(Assistant))

# Q3
email = []
for f in faculty:
    email.append(f[3].strip())
print(email)
    
# Q4
domains = []
for account in email:
    domains.append(account.split('@'))

unique = []
for domain in domains:
    unique.append(domain[1])
print (list(set(unique)))
PLACE YOUR CODE HERE