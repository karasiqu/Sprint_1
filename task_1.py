time = '1h 45m,360s,25m,30m 120s,2h 60s'
t = time.split(',')
count = 0

for period in t:
    for i in period.split():    

        numbers = i[:len(i) - 1]
        time_unit = i[-1]

        if time_unit == 'h':
            count += int(numbers) * 3600
        elif time_unit == 'm':
            count += int(numbers) * 60
        elif time_unit == 's':
            count += int(numbers) 
        
print(count // 60)