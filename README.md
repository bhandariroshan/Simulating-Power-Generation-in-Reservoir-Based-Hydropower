# Simulating-Power-Estimation-in-Hydropower

This algorithm helps simulate power generated for different time during pick hour and off hour in a reservoir using height of the water available in reservoid for each day for 12 months

NOTE: To run the code, you need to have python 2.7 installed 
Running the code:

1. python power.py
2. Input following:
   a. Number of days in the month
   b. Input in the month
   c. Number of "I" in per peak shift
   d. Number of hrs in non peak shift

# Equation of height of water in reservoir
f(h)= 13557.8282850575x2 - 23743654.1706026000x + 10398688014.4791000000 

# Equation of derivative of height
f'(h)=2* 13557.8282850575-23743654.1706026000

# Algorithm:
1. Ask for intial height of water "h", power to be generated "p" ,month count=1
2. Main loop starts here;  month count = monthcount + 1
3. If month count > 12, exit all the loops go to 4 and type year finished
 3.1 day=1
 
 3.1.1 Ask for number of days in the month and input in the month, number of "I" in per peak shift, number of hrs in non peak shift
 
  3.1.1.1 day = day+1
 
  3.1.1.2 if day>no. of days in month, go to step 2
  
  3.1.1.3 First shift loop starts here; i=1
    
    3.1.1.3.1 dh=f(h)*(p/9810/h-input)*3600*10/f'(h)
    
    3.1.1.3.2 h=h-dh
    
    3.1.1.3.3 i=i+1
    
    3.1.1.3.4 if i> number of "I" per peak shift, go to 3.1.1.4 else go to 3.1.1.3.1
  
  3.1.1.4 new volume=f(h)+input*number of hours in non peak shift*3600
  
  3.1.1.5 new height h= solution of eqn(13557.8282850575x2 - 23743654.1706026000x + 10398688014.4791000000 = new volume from step 3.1.1.4) *precision upto  0.001 needed here*
  
  3.1.1.6  second shift loop starts here; i=1
    
    3.1.1.6.1  dh=f(h)*(p/9810/h-input)*3600*10/f'(h)
    
    3.1.1.6.2  h=h-dh
    
    3.1.1.6.3  i=i+1
    
    3.1.1.6.4  if i> number of "I" per peak shift, go to step 3.1.1.7 else, go to 3.1.1.6.1
    
    3.1.1.7 new volume=f(h)+input*number of hours in non peak shift*3600
    
    3.1.1.8 new height h= solution of eqn(13557.8282850575x2 - 23743654.1706026000x + 10398688014.4791000000=new volume from step 3.1.1.7) *precision upto  0.001 needed here*
    
    3.1.1.9 print the end of the day height "h" and go to 3.1.1.1

4. Print f(h) at the end of year

5. End
