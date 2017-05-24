# Hint:  use Google to find python function

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

dt_start_a = datetime.strptime(date_start,"%m-%d-%Y" )
dt_stop_a = datetime.strptime(date_stop,"%m-%d-%Y" )

days_a = dt_stop_a - dt_start_a
print(days_a) # 937 days

####b)  
date_start = '12312013'  
date_stop = '05282015'  

dt_start_b = datetime.strptime(date_start,"%m%d%Y" )
dt_stop_b = datetime.strptime(date_stop,"%m%d%Y" )

days_b = dt_stop_b - dt_start_b
print(days_b) # 513 days

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

dt_start_c = datetime.strptime(date_start,"%d-%b-%Y" )
dt_stop_c = datetime.strptime(date_stop,"%d-%b-%Y" )

days_c = dt_stop_c - dt_start_c
print(days_c) # 7850 days
