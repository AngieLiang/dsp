with open('/Users/lqa/Desktop/faculty2.csv', newline = '') as csvfile:
    reader = csv.reader(csvfile)
    fac = []
    for line in reader:
        fac.append(line)
        faculty = fac[1:]
        #print(faculty)
names = [item[0] for item in faculty]
values = [item[1:] for item in faculty]
# degrees = [item[1] for item in faculty]
# titles = [item[2] for item in faculty]
# emails = [item[3] for item in faculty]


last_name = []
first_name = []
full_name = []
for name in names:
    last= name.split()[-1]
    last_name.append(last)
    first= name.split()[:-1]
    full = tuple(first + [last])
    full_name.append(full)

# print(last_name)
# print(first_name)
# print(values)

#Q6
def get_dict():
    
    faculty_dict = {}
    for lname, val in zip(last_name,values):
        if lname not in faculty_dict:
            faculty_dict[lname] = []
            faculty_dict[lname].append(val)
        else:
            faculty_dict[lname].append(val)
    return faculty_dict

i = 0
for k,v in faculty_dict.items():
    i += 1
    if i < 4:
        print ((k,v))
            
#Q7
def get_dict2():
    faculty_dict2 = {}
    for fname, val in zip(full_name,values):
        faculty_dict2[fname] = val
    return faculty_dict2
  
i = 0
for k,v in faculty_dict2.items():
    i += 1
    if i <= 3:
        print ((k,v))        
    
  
