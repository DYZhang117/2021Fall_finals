## Monte Carlo Simulation-Waiting Time for Available Machines in Laundry Room
Team: Diyan Zhang (diyanz2, GitHub: DYZhang117), Hao Jia (haoj4, GitHub: Kivi1998)

GitHub link: https://github.com/DYZhang117/2021Fall_finals
 
Communal laundry rooms are very common in the United States. The main customers in this industry include renters, college students, and residents of multi-family residential apartments. Many old-fashioned apartments in the United States only provide public laundry and are not equipped with independent washing machine/dryer services.
 
Even though many newly built luxury apartments are equipped with individual washing machines/dryers for each residence, most of the apartments managed by the university still only have a communal laundry room in Champaign. Students have to wait a long time to start their washing/drying process.
 
This Monte Carlo simulation is to calculate the average waiting time for students in the laundry room for available machines (calculate the washing machine and dryer respectively) based on the Orchard Downs community of UIUC.
 
It should be noted that Orchard Downs is a community that primarily provided for graduate students and their families. The room types contain 2B2B and 1B1B. About 40% of 2B2B tenants are families (more than 3 people), 20% are one person, and 40% are two people. For 1B1B, 50% are two people living, and 50% are living alone.
 
## Design Assumptions
1. The laundry room is only available to tenants in the Orchard Downs community. And the laundry room runs for 24 hours.
2. According to the rules of the laundry room, if the previous user did not take the clothes out in time, the next student would only need to wait maximum 15 minutes to use that machine.
3. Typically, people start their washing from 8 am to 10 pm, and they are more likely to wash their clothes at 6:00 PM-9:00 PM. In addition, people prefer to do laundry on weekends.
4. Every time washing clothes, they need to use both washing machines and dryers.
5. Assume that all the apartments are rented out.
6. If the washing frequency is once a week:
Each family (more than 3 people) and a unit with 2 people must use 3 washing machines and 2 dryers each time. A tenant living alone uses 2 washing machines and 1 dryer at a time.
If the washing frequency is twice a week or more:
Each family (more than 3 people) and a unit with 2 people will use 2 washing machines and 1 dryer instead. A tenant living alone uses 1 washing machine and 1 dryer each time.
 
## Variables
1. The number of dryers and washing machines (input fixed values).
2. The number of residents (input value).
3. The Maximum time to wait for the user to take out the clothes each time the washing machine or dryer finishes its work (0 min< time< 15 mins)
4. The Maximum time interval between two machine (end-beginning) [both washing machines and dryers](0 min< time< 15 mins)
5. Each maximum washing time of the washing machine (25 mins<time<70 mins). Each maximum working time of the dryer (35 mins<time<140 mins).
6. The washing frequency of each unit.
7. Simulation times.
 
## Hypotheses
1.	80% of the waiting durations are less than 2 hours.
2.	If 20% of residents reduce their washing frequency per week, the average queue time will be reduced by more than 20%.

## Reference
https://housing.illinois.edu/Tools/Laundry

https://housing.illinois.edu/Living-Options/Apartments/Orchard-Downs/map-floor-plans

