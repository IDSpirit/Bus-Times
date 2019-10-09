import time as t
import datetime
import re


m_to_f_times_h = [6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 13, 13, 13, 13, 13, 13, 14, 14, 14, 14, 14, 14, 15, 15, 15, 15, 15, 16, 16, 16, 16, 16, 16, 17, 17, 17, 17, 17, 17, 18, 18, 18, 18, 18, 18, 18, 19, 19, 19, 19, 20, 20, 21, 21, 22, 22, 23]

m_to_f_times_m = [4, 20, 30, 40, 48, 57, 7, 16, 25, 34, 42, 51, 1, 11, 21, 31, 41, 51, 59, 9, 18, 27, 36, 44, 53, 3, 13, 23, 32, 42, 52, 2, 12, 22, 32, 42, 52, 2, 12, 22, 32, 42, 52, 2, 12, 22, 32, 42, 52, 2, 12, 22, 32, 43, 56, 6, 16, 27, 40, 52, 2, 12, 22, 32, 42, 52, 2, 11, 21, 31, 41, 51, 1, 9, 17, 25, 33, 41, 56, 11, 26, 41, 55, 15, 41, 11, 41, 11, 41, 41]


sat_times_h = [6, 6, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 12, 12, 13, 13, 13, 13, 13, 13, 14, 14, 14, 14, 14, 14, 15, 15, 15, 15, 15, 15, 16, 16, 16, 16, 16, 16, 17, 17, 17, 17, 17, 17, 18, 18, 18, 18, 19, 19, 19, 19, 20, 20, 21, 21, 22, 22, 23]

sat_times_m = [23, 53, 23, 38, 53, 8, 23, 38, 53, 6, 17, 29, 39, 50, 1, 11, 21, 31, 41, 51, 1, 11, 21, 31, 41, 51, 1, 11, 21, 31, 41, 51, 1, 11, 21, 31, 41, 51, 1, 11, 21, 31, 41, 51, 1, 11, 21, 31, 41, 51, 1, 11, 21, 31, 41, 51, 1, 11, 21, 31, 41, 56, 11, 26, 41, 56, 11, 26, 41, 56, 16, 42, 12, 41, 11, 41, 41]


sun_times_h = [7, 9, 9, 10, 10, 11, 11, 11, 12, 12, 12, 13, 13, 13, 14, 14, 14, 15, 15, 15, 16, 16, 17, 17, 18, 18, 19, 19, 20, 20, 21, 22]

sun_times_m = [58, 5, 45, 24, 44, 4, 24, 44, 4, 24, 44, 4, 24, 44, 4, 24, 44, 4, 24, 44, 9, 39, 9, 39, 6, 35, 5, 35, 5, 34, 34, 34]


def check_time():
    
    try:
        choice = int(input("\nDo you want to see the bus times for the 111 bus from Claremont (1 for yes, 2 for no): "))

    except:
        print("\nInvalid input, please try again...\n")
        t.sleep(3)
        print("\n------------------------------------------------------------------------------------------\n")
        check_time()
        
    if choice == 1:
        day = datetime.datetime.today().weekday()
        time = datetime.datetime.now().time()
        counter = 0
        difference = []
        difference_mins = []
        
        if day >= 0 and day <= 4:
            hours = m_to_f_times_h
            mins = m_to_f_times_m
            
        elif day == 5:
            hours = sat_times_h
            mins = sat_times_m
            
        elif day == 6:
            hours = sun_times_h
            mins = sun_times_m

        current_h = time.hour
        current_m = time.minute

        while True:
            indices = [i for i, x in enumerate(hours) if x == current_h]
            
            for x in indices:
                difference_mins.append(mins[x])
            
            if current_h == 24:
                current_h = 0
                if day == 4:
                    hours = sat_times_h
                    mins = sat_times_m
                    
                elif day == 5:
                    hours = sun_times_h
                    mins = sun_times_m
                    
                elif day == 6:
                    hours = m_to_f_times_h
                    mins = m_to_f_times_m
                difference_mins = [] #Reset this to make sure this list only contains elements from within an hour timeframe
                #counter doesn't increment here because otherwise it would increment at both 24:00 and 00:00
            elif indices == []:
                current_h = current_h + 1
                counter = counter + 1
                difference_mins = []
                
            elif max(difference_mins) < current_m and counter == 0: #e.g. if it's 10:50 and the latest bus at 10:"something" is 10:30, then the next hour is cheched i.e. current_h is incremented
                #counter must be 0 because if for example considering the e.g. above, if the next bus is at 11:40 thenwithout the counter == 0, the current_h would increment whihc we wouldn't want in this case
                current_h = current_h + 1
                counter = counter + 1
                difference_mins = []
                
            else:
                if counter == 0:
                    real_difference = difference
                    for x in difference_mins:
                        difference.append(x - current_m)

                    real_difference = list(difference) #"difference" needs to be set as a list so that changes in "difference" don't affect "real_difference"

                    #print("HFISDJFSAOJDOSA" + str(difference))
                        
                    for x in difference:
                            
                        if x < 0:
                            real_difference.remove(x)
                            #print(str(x) + " is smaller than 0")
                        else:
                            continue
                            #print(str(x) + " is bigger than 0") 
                                
                    smallest_difference = min(real_difference)
                    value = difference.index(smallest_difference)
                    
                    if difference_mins[value] <= 9:
                        mins_for_bus = str("0") + str(difference_mins[value])
                    else:
                        mins_for_bus = str(difference_mins[value])
                        
                    print("\nNext bus is scheduled for " + str(current_h) + ":" + str(mins_for_bus) + " and is coming in approximately " + str(smallest_difference) + " minutes")

                else: #i.e. if the next bus isn't within the hour (since if it isn't within the hour, counter will increment)
                    small_mins = min(difference_mins)
                    mins_left = 60 - current_m

                    if current_m > small_mins:
                        counter = counter - 1
                        
                    if small_mins <= 9:
                        small_mins_str = str("0") + str(small_mins)
                    else:
                    	small_mins_str = str(small_mins)

                    final_mins_left = small_mins + mins_left

                    if final_mins_left >= 60:
                        final_mins_left = 60 - final_mins_left
                        counter = counter - 1
                        
                    print("\nNext bus is scheduled for " + str(current_h) + ":" + small_mins_str + " which is coming in " + str(counter) + " hours and " + str(final_mins_left) + " minutes")
                break

        t.sleep(3)
        print("\n------------------------------------------------------------------------------------------\n")
        check_time()
            
    elif choice == 2:
        quit()
        
    else: #If they pick some other number (since this wouldn't trigger the "try, except" case
        print("\nInvalid input, please try again...\n")
        t.sleep(3)
        print("\n------------------------------------------------------------------------------------------\n")
        check_time()

check_time()
