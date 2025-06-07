"""
Yuslen Lopez 
z#23673549 
COP4610: Project 1 


FCFS:
Goals: 
1.CPU(utilization)
2.T(wait)
3.T(TurnAround)
4.T(response)

Known: 
-8 proccesses 
-we need a queue to take care of FCFS 
-loop to take care of unit time (possibly)

"""

#Creating a class to store each process
class Proccess:

    Burst=[]
    WaitingTime=0
    TurnaroundTime=0
    ResponseTime=0
    
    #variable to keep track of each proccess
    Proccess_Number=0
    #Holds total cpu bursts
    Total_CPU_Burst=0
    #Total IO bursts 
    Total_IO_Burst=0
    #index in the Burst array
    Burst_index=0
    #Stores total time of proccess 
    Completion_Time=0
    #Using this to keep track of witch proccess comes next for FCFS
    Arrival_Time=0

    #initialization function 
    def __init__(self, arr,number):
        self.Burst=arr
        self.Proccess_Number=number
        
   
#Creating array storing each proccess CPU and IO burst times
arr1=[5,27,3,31,5,43,4,18,6,22,4,26,3,24,4]
arr2=[4,48,5,44,7,42,12,37,9,76,4,41,9,31,7,43,8]
arr3=[8,33,12,41,18,65,14,21,4,61,15,18,14,26,5,31,6]
arr4=[3,35,4,41,5,45,3,51,4,61,5,54,6,82,5,77,3]
arr5=[16,24,17,21,5,36,16,26,7,31,13,28,11,21,6,13,3,11,4]
arr6=[11,22,4,8,5,10,6,12,7,14,9,18,12,24,15,30,8]
arr7=[14,46,17,41,11,42,15,21,4,32,7,19,16,33,10]
arr8=[4,14,5,33,6,51,14,73,16,87,6]

#creating and initializing each Process 
process1=Proccess(arr1,1)
process2=Proccess(arr2,2)
process3=Proccess(arr3,3)
process4=Proccess(arr4,4)
process5=Proccess(arr5,5)
process6=Proccess(arr6,6)
process7=Proccess(arr7,7)
process8=Proccess(arr8,8)

#Creating and adding processes to queue 
queue=[]
queue.append(process1)
queue.append(process2)
queue.append(process3)
queue.append(process4)
queue.append(process5)
queue.append(process6)
queue.append(process7)
queue.append(process8)
#creating second queue to store for printing later 
queue2 =queue
#keep track of time accumulated with t 
t=0
#variable for average Cpu utilization 
Total_All_CPU_Burst=0

#Sorting key function 
def p_sort(Proccess):
    return Proccess.Arrival_Time


#Loop to execute until queue is empty 
while queue !=[]:

    #sorting the queue by the arrival time in class to order by FCFS
    queue = sorted(queue, key=p_sort)
    
    #getting first proccess in queue 
    item=queue.pop(0)

    #If arrival time of proccess is ever less than current t (time) continue to iterate and increase time 
    if(item.Arrival_Time>t):
        while item.Arrival_Time>t:
            print("Queue is empty waiting on process +1")
            t+=1
        
    #when proccess runs first time store initial starting time 
    if item.Burst_index==0:
        item.ResponseTime=t #this works cause all proccesses are arriving at t=0 

    #printing Proccess status 
    print("\n-------------------------Proccess #",item.Proccess_Number)
    print("Current time before CPU burst=",t)
    print("CPU Burst = ", item.Burst[item.Burst_index])#test of each burst
    print("Arrival Time = ",item.Arrival_Time)#test for arrival times
    

    #updating total time elapsed 
    t+=item.Burst[item.Burst_index]
    
    #updating each proccesses total CPU Burst
    item.Total_CPU_Burst+=item.Burst[item.Burst_index]

    #updating combined CPU burst of all process (for CPU utilization)
    Total_All_CPU_Burst+=item.Burst[item.Burst_index]


    #add IO Burst to total IO Burst if it exists 
    if item.Burst_index+1<len(item.Burst)-1:
        item.Total_IO_Burst+=item.Burst[(item.Burst_index+1)]

    #print IO burst
    if item.Burst_index+1<len(item.Burst)-1:
        print("IO burst = ",item.Burst[(item.Burst_index+1)])
    

    #if not out of index update next arrival time of process 
    if item.Burst_index+1<len(item.Burst)-1:
        item.Arrival_Time=t+item.Burst[(item.Burst_index+1)]
        print("Next Arrival Time = ",item.Arrival_Time)
        
    #Update the Burst_index by two cause we accounted both CPU and IO Burst in each iteration 
    item.Burst_index+=2

    #if proccess is not complete add back to end of queue, else proccess is finished and set completion time to current time (t)  
    if item.Burst_index <= (len(item.Burst)-1):
        queue.append(item)
    else:
        
        print("==============================Proccess Complete time =",t)
        item.Completion_Time=t

    #while loop end 
        
"""
TurnaroundTime = CompletionTime - ArrivalTime (Arrival time is zero for all proccesses)
WaitingTime = TurnaroundTime - BurstTime (CPU+IO Bursts)
ResponseTime = FirstBurstTime 

CPU_util = Total Burst time / Total Time 
"""
#variables for calculating averages 
CPU_Utilization=Total_All_CPU_Burst/t
Waiting_Time_All=0
Turnaround_Time_All=0
Response_Time_All=0
#Calculating T(w), T(tr) and total times for averages 
for i in queue2:
    i.TurnaroundTime=i.Completion_Time 
    Turnaround_Time_All+=i.TurnaroundTime
    i.WaitingTime= i.TurnaroundTime-(i.Total_CPU_Burst+i.Total_IO_Burst)
    Waiting_Time_All+=i.WaitingTime
    Response_Time_All+=i.ResponseTime

print("")
#testing loop 
j=1
for i in queue2:
    #print("Proccess #",i.Proccess_Number)

    print("waiting time p"+str(j)," = ",i.WaitingTime)
    print("Turnaround time p"+str(j)," = ",i.TurnaroundTime)
    print("Response time p"+str(j)," = ",i.ResponseTime)
    print("CPU Burst time p"+str(j)," = ",i.Total_CPU_Burst)
    print("IO Burst time p"+str(j)," = ",i.Total_IO_Burst)
    print("Completion time p"+str(j)," = ",i.Completion_Time)
    print()
    j+=1

#Printing loop   
j=1
print("----------------------------------------------------------------------------")
print("   |Waiting Time|Turnaround Time|Response Time|")
for i in queue2:
    print("p"+str(j),"",i.WaitingTime,"        ",i.TurnaroundTime,"            ",i.ResponseTime)
    print()
    j+=1
print("Avg","",round(Waiting_Time_All/8,2),"    ",round(Turnaround_Time_All/8,2),"         ",round(Response_Time_All/8,2))
print("\nCPU utilization = ",round(CPU_Utilization,4)*100,"%\n")
print("Total time for completion = ",t,"time units")
print("----------------------------------------------------------------------------")


