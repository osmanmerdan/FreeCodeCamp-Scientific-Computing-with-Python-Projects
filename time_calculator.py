def add_time(start,duration,day=False):
#Create a listfor week days and a dictionary.
#Late I will use them to to calculate new day.

    week_days={'Monday':0, 'Tuesday':1,'Wednesday':2, 'Thursday':3,\
               'Friday':4,'Saturday':5,'Sunday':6}
    list_days=['Monday','Tuesday','Wednesday', 'Thursday','Friday',\
               'Saturday','Sunday']

#Extracting data
    anahtar=start.split()[1]
    s=start.split()[0]
    s_h=int(s.split(':')[0])
    s_m=int(s.split(':')[1])
    p_h=int(duration.split(':')[0])
    p_m=int(duration.split(':')[1])

#Defining start origin 
#Sorry Einstein. I will define a zero time point. 
#And calculate everyting in minute scale. 
# Dealing with PM and AM.
    
    if anahtar=='PM' and s_h!=12:
        s_h=s_h+12
    if anahtar=='AM' and s_h==12:
        s_h=0

#Calculate Total minutes passed from origin of zero
    total=(s_h*60+s_m)+(p_h*60+p_m)

#Calculate how many days passed 
    days_passed=int(total/(60*24))

#Calculate hour
    hour=int((total%(60*24))/60)
    if hour>12:
        hour=int(hour-12)
        yeni_anahtar='PM'
    elif hour==0:
        hour=12
        yeni_anahtar='AM'
    elif hour==12:
        hour=12
        yeni_anahtar='PM'
    else:
        yeni_anahtar='AM'

#Calculated minute
    minute=int((total%(60*24))%60)
    if minute<10:
       minute='0'+str(minute)

#Format
    format=str(hour)+':'+str(minute)+' '+str(yeni_anahtar)

#Refining format according to rules defined.
    if day:
        new_day= list_days[(int(week_days[day.title()])+days_passed)%7]
        if days_passed==1:
            format=format+', '+new_day+' (next day)'
        elif days_passed>1:
            format=format+', '+new_day+' ('+str(days_passed)+' days later)'
        else:
            format=format+', '+new_day
    else:
        if days_passed==1:
            format=format+' (next day)'
        elif days_passed>1:
            format=format+' ('+str(days_passed)+' days later)'

    
    return(format)