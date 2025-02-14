"""
The flight ticket rates for a round-trip (Mumbai->Dubai) were as follows: 
Rate per Adult: Rs. 37550.0 
Rate per Child: 1/3rd of the rate per adult 
Service Tax: 7% of the ticket amount (including all passengers) 
As it was a holiday season, the airline also offered 10% discount on the final ticket cost (after inclusion of the service tax).
Find and display the total ticket cost for a group which had adults and children.
"""
no_of_adult=int(input("enter no of adults :"))
no_of_children=int(input("enter no of children :"))
holiday=bool(input("enter True if it is a holiday/ enter False :"))
cost_per_adult= 37550.0
cost_per_children=(1/3)*(cost_per_adult)
def totalcost(no_of_adult,no_of_children):
    travel_fare=0
    travel_fare=(7/100)*((no_of_adult*cost_per_adult)+(no_of_children*cost_per_children)) #include service tax
    if(holiday==True):
        travel_fare=(10/100)*travel_fare
    return travel_fare
travel_fare=totalcost(no_of_adult,no_of_children)
print("travel fare : ",travel_fare)