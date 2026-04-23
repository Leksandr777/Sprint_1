origin_str = "1h 45m,360s,25m,30m 120s,2h 60s"
work_str = origin_str.split(',')
summ_minutes = 0

for i in work_str:
    hours=0
    minutes=0
    seconds=0

    if 'h' in i:
        h_pos = i.find("h")
        hours = int(i[:h_pos].strip())
        i = i[h_pos+1:]

    if 'm' in i:
        m_pos = i.find("m")
        minutes = int(i[:m_pos].strip())
        i = i[m_pos+1:]
    
    if 's' in i:
        s_pos = i.find("s")
        seconds= int(i[:s_pos])

    summ_minutes =summ_minutes + hours*60 + minutes + seconds//60

print(f"Общее количество минут: {summ_minutes}")