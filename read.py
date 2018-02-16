# opening the file
with open('AvaiationData.txt') as filename:
  
    lines=filename.read()
    aviation_data=lines.split("\n")
    # print(aviation_data)
    #
    aviation_list=[]
    for line in aviation_data:
        lineS=line.split(" | ")
        aviation_list.append(lineS)     


# This is not the optimal solution as the loop runs n*n times
    lax_code = []
    for i in range(len(aviation_list)):
        for j in range(len(aviation_list[i])):
            if aviation_list[i][j] == 'LAX94LA336':
                lax_code.append(aviation_list[i])
    #print(lax_code )
    
#create a dictionary instead of a list

titles=aviation_data[0].split(" | ")
data=aviation_data[1:]

aviation_dict_list=[]

for row in data:
    splitline=row.split(" | ")
    dict_data={}
    for i in range(len(splitline)):
        dict_data[titles[i]]=splitline[i]
    
    aviation_dict_list.append(dict_data)
    
#print(aviation_dict_list)

#Using the list of dictionaries, search for LAX94LA336
lax_dict = []
for dictionary in aviation_dict_list    :
    if "LAX94LA336" in dictionary.values():
        lax_dict.append(dictionary)
        
        
#Count up how many accidents occurred in each U.S. state
from collections import Counter
state_accident_list=[]

for dictionary in aviation_dict_list:
    if 'Country' in dictionary:
        if dictionary['Country']=='United States':
            state_list=dictionary['Location'].split(", ")
            try: 
                state=state_list[1]
            except:
                state=""
            
            if len(state)==2:
                state_accident_list.append(state)
count_state_accident=Counter(state_accident_list)
#print(count_state_accident)

#Count how many fatalities and serious injuries occured during each unique month and year
month_names=[]
for dictionary in aviation_dict_list:
    month_injuries=[]
    
    if 'Event Date' in dictionary:
        split_date=dictionary['Event Date'].split('/')
        try:
            s_injuries=int(dictionary['Total Serious Injuries'])
        except:
            s_injuries=0
        
        try:
            f_injuries=int(dictionary['Total Fatal Injuries'])
        except:
            f_injuries=0
            
        try:
            MM_YYYY=split_date[0]+'/'+split_date[2]
        except:
            MM_YYYY=""
        
        if len(MM_YYYY)==7:
            month_injuries.append(MM_YYYY)
            month_injuries.append(s_injuries)
            month_injuries.append(f_injuries)
    month_names.append(month_injuries)

#print(month_names)

#This list of lists contains a list for each accident that has occurred, we want to compact this list so it only shows each MM/YYYY once. A  way to do this is using a dictionary with MM/YYYY as keys then make another dictionary with Serious Injury and Fatal Injury as keys
monthly_injuries = {}
for accident in month_names:
    try:
        month = accident[0]
        s_injury = accident[1]
        f_injury = accident[2]
    except:
        continue
    if month not in monthly_injuries:
        monthly_injuries[month] = {'Serious Injury': s_injury, 'Fatal Injury': f_injury}
    
    if month in monthly_injuries:
        monthly_injuries[month]['Serious Injury'] += s_injury
        monthly_injuries[month]['Fatal Injury'] += f_injury
    
if 'Serious Injury' in monthly_injuries.values():
    print(month_injuries['Serious Injury'].values())

#          