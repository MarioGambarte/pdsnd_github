import time	import time
import pandas as pd	import pandas as pd
import numpy as np	import numpy as np
CITY_DATA = { 'chicago': 'chicago.csv',	CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',	              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }	              'washington': 'washington.csv' }
input_city = ["chicago","new york city","washington"]	input_city = ["chicago","new york city","washington"]
input_month = ('january', 'february', 'march', 'april', 'may', 'june')	input_month = ('january', 'february', 'march', 'april', 'may', 'june')
input_days = ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday',	input_days = ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday',
            'saturday')	            'saturday')
def get_filters():	def get_filters():
    """	    """
    Asks user to specify a city, month, and day to analyze.	    Asks user to specify a city, month, and day to analyze.
    Returns:	    Returns:
        (str) city - name of the city to analyze	        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter	        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter	        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """	    """
    print('Hello! Let\'s explore some US bikeshare data!')	    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs	    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:	    while True:
        city = str(input("Enter a city which you want to explore bikeshare data (chicago,new york city,washington)\n").strip().lower())	        city = str(input("Enter a city which you want to explore bikeshare data (chicago,new york city,washington)\n").strip().lower())
        if city not in ("chicago","new york city","washington"):	        if city not in ("chicago","new york city","washington"):
            print("wrong Input Please input city from this list {} ".format(input_city))	            print("wrong Input Please input city from this list {} ".format(input_city))
            continue;	            continue;
        else:	        else:
            print("Nice Choice, I think you like {} ".format(city))	            print("Nice Choice, I think you like {} ".format(city))
            break;	            break;
        # TO DO: get user input for month (all, january, february, ... , june)	        # TO DO: get user input for month (all, january, february, ... , june)
        print("")	        print("")
    while True:	    while True:
        month = str(input("Enter a month which you want to explore bikeshare data ( january, february, ... , june)\n").strip().lower())	        month = str(input("Enter a month which you want to explore bikeshare data ( january, february, ... , june)\n").strip().lower())
        if month not in ('january', 'february', 'march', 'april', 'may', 'june'):	        if month not in ('january', 'february', 'march', 'april', 'may', 'june'):
            print("Invalid Input Please enter valid input e.g. {}".format(input_month))	            print("Invalid Input Please enter valid input e.g. {}".format(input_month))
            continue	            continue
        else:	        else:
            print("Your favourate Month is {}".format(month))	            print("Your favourate Month is {}".format(month))
            break;	            break;
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)	    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        print(" ")	        print(" ")
    while True:	    while True:
        day = str(input("Enter a day which you want to explore bikeshare data (sunday,monday,.....,saturday)\n").strip().lower())	        day = str(input("Enter a day which you want to explore bikeshare data (sunday,monday,.....,saturday)\n").strip().lower())
        if day not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday'):	        if day not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday'):
            print("Invalid Input Please enter valid input e.g. {}".format(input_days))	            print("Invalid Input Please enter valid input e.g. {}".format(input_days))
            continue	            continue
        else:	        else:
            print("Nice choice ,Your day selected is {}".format(day))	            print("Nice choice ,Your day selected is {}".format(day))
            break;	            break;
    print('-'*40)	    print('-'*40)
    return city, month, day	    return city, month, day
def load_data(city, month, day):	def load_data(city, month, day):
    """	    """
    Loads data for the specified city and filters by month and day if applicable.	    Loads data for the specified city and filters by month and day if applicable.
    Args:	    Args:
        (str) city - name of the city to analyze	        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter	        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter	        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:	    Returns:
        df - Pandas DataFrame containing city data filtered by month and day	        df - Pandas DataFrame containing city data filtered by month and day
    """	    """
   	   
    start_time = time.time()	    start_time = time.time()
    df = pd.read_csv(CITY_DATA[city])	    df = pd.read_csv(CITY_DATA[city])
    # create columns to display statistics	    # create columns to display statistics
    df['Start Time'] = pd.to_datetime(df['Start Time'])	    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month	    df['Month'] = df['Start Time'].dt.month
   # df['Weekday'] = df['Start Time'].dt.day_name	   # df['Weekday'] = df['Start Time'].dt.day_name
    df['Weekday'] = df['Start Time'].dt.day_name()	    df['Weekday'] = df['Start Time'].dt.day_name()
    df['Start Hour'] = df['Start Time'].dt.hour	    df['Start Hour'] = df['Start Time'].dt.hour
    df = df[df['Month'] == (input_month.index(month)+1)]	    df = df[df['Month'] == (input_month.index(month)+1)]
    df = df[df['Weekday'] == day.title()]	    df = df[df['Weekday'] == day.title()]
    	    
    print("\nThis took {} seconds.".format((time.time() - start_time)))	    print("\nThis took {} seconds.".format((time.time() - start_time)))
    print('-'*40)	    print('-'*40)
    return df	    return df
def time_stats(df):	def time_stats(df):
    """Displays statistics on the most frequent times of travel."""	    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')	    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()	    start_time = time.time()
    # TO DO: display the most common month	    # TO DO: display the most common month
    most_common_month = df['Month'].mode()[0]	    most_common_month = df['Month'].mode()[0]
    print("most_common_month is = {}".format(input_month[most_common_month-1]))	    print("most_common_month is = {}".format(input_month[most_common_month-1]))
    # TO DO: display the most common day of week	    # TO DO: display the most common day of week
    most_common_day = df['Weekday'].mode()[0]	    most_common_day = df['Weekday'].mode()[0]
    print("The most common day of week is =  {}".format(most_common_day))	    print("The most common day of week is =  {}".format(most_common_day))
    # TO DO: display the most common start hour	    # TO DO: display the most common start hour
    most_common_start_hour = df['Start Hour'].mode()[0]	    most_common_start_hour = df['Start Hour'].mode()[0]
    print("most_common_start_hour is = {}".format(most_common_start_hour))	    print("most_common_start_hour is = {}".format(most_common_start_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))	    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)	    print('-'*40)
def station_stats(df):	def station_stats(df):
    """Displays statistics on the most popular stations and trip."""	    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')	    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()	    start_time = time.time()
    # TO DO: display most commonly used start station	    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]	    most_common_start_station = df['Start Station'].mode()[0]
    print("most_common_start_station is {}".format(most_common_start_station))	    print("most_common_start_station is {}".format(most_common_start_station))
    # TO DO: display most commonly used end station	    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]	    most_common_end_station = df['End Station'].mode()[0]
    print("most_common_start_station is {}".format(most_common_start_station))	    print("most_common_start_station is {}".format(most_common_start_station))
    # TO DO: display most frequent combination of start station and end station trip	    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_comb = df['Start Station'] +" "+ df['End Station']	    most_frequent_comb = df['Start Station'] +" "+ df['End Station']
    print("most frequent combination of start station and end station trip is {}".format(most_frequent_comb.mode()[0]))	    print("most frequent combination of start station and end station trip is {}".format(most_frequent_comb.mode()[0]))
    print("\nThis took {} seconds.".format((time.time() - start_time)))	    print("\nThis took {} seconds.".format((time.time() - start_time)))
    print('-'*40)	    print('-'*40)
def trip_duration_stats(df):	def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""	    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')	    print('\nCalculating Trip Duration...\n')
    start_time = time.time()	    start_time = time.time()
    	    
    # display total travel time	    # display total travel time
    total_travel_time = df['Trip Duration'].sum()	    total_travel_time = df['Trip Duration'].sum()
    total_travel_time = (str(int(total_travel_time//86400)) +	    total_travel_time = (str(int(total_travel_time//86400)) +
                         'd ' +	                         'd ' +
                         str(int((total_travel_time % 86400)//3600)) +	                         str(int((total_travel_time % 86400)//3600)) +
                         'h ' +	                         'h ' +
                         str(int(((total_travel_time % 86400) % 3600)//60)) +	                         str(int(((total_travel_time % 86400) % 3600)//60)) +
                         'm ' +	                         'm ' +
                         str(int(((total_travel_time % 86400) % 3600) % 60)) +	                         str(int(((total_travel_time % 86400) % 3600) % 60)) +
                         's')	                         's')
    print('Total Travel time is {} '.format(total_travel_time))	    print('Total Travel time is {} '.format(total_travel_time))
    # display mean travel time	    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()	    mean_travel_time = df['Trip Duration'].mean()
    mean_travel_time = (str(int(mean_travel_time//60)) + 'm ' +	    mean_travel_time = (str(int(mean_travel_time//60)) + 'm ' +
                        str(int(mean_travel_time % 60)) + 's')	                        str(int(mean_travel_time % 60)) + 's')
    print('Mean travel time is {} .'.format(mean_travel_time))	    print('Mean travel time is {} .'.format(mean_travel_time))
    print("\nThis took {} seconds.".format((time.time() - start_time)))	    print("\nThis took {} seconds.".format((time.time() - start_time)))
    print('-'*40)	    print('-'*40)
def user_stats(df,city):	def user_stats(df,city):
    """Displays statistics on bikeshare users."""	    """Displays statistics on bikeshare users."""
    # TO DO: Display earliest, most recent, and most common year of birth	    # TO DO: Display earliest, most recent, and most common year of birth
    print('\nCalculating User Stats...\n')	    print('\nCalculating User Stats...\n')
    start_time = time.time()	    start_time = time.time()
    # Display counts of user types	    # Display counts of user types
    user_types = df['User Type'].value_counts().to_string()	    user_types = df['User Type'].value_counts().to_string()
    print("Distribution for user types:")	    print("Distribution for user types:")
    print(user_types)	    print(user_types)
    # Display counts of gender	    # Display counts of gender
    try:	    try:
        gender_distribution = df['Gender'].value_counts().to_string()	        gender_distribution = df['Gender'].value_counts().to_string()
        print("\nDistribution for each gender:")	        print("\nDistribution for each gender:")
        print(gender_distribution)	        print(gender_distribution)
    except KeyError:	    except KeyError:
        print("We're sorry! There is no data of user genders for {}."	        print("We're sorry! There is no data of user genders for {}."
              .format(city.title()))	              .format(city.title()))
    # Display earliest, most recent, and most common year of birth	    # Display earliest, most recent, and most common year of birth
    try:	    try:
        earliest_birth_year = str(int(df['Birth Year'].min()))	        earliest_birth_year = str(int(df['Birth Year'].min()))
        print("\nFor the selected filter, the oldest person to ride one "	        print("\nFor the selected filter, the oldest person to ride one "
              "bike was born in: " + earliest_birth_year)	              "bike was born in: " + earliest_birth_year)
        most_recent_birth_year = str(int(df['Birth Year'].max()))	        most_recent_birth_year = str(int(df['Birth Year'].max()))
        print("For the selected filter, the youngest person to ride one "	        print("For the selected filter, the youngest person to ride one "
              "bike was born in: " + most_recent_birth_year)	              "bike was born in: " + most_recent_birth_year)
        most_common_birth_year = str(int(df['Birth Year'].mode()[0]))	        most_common_birth_year = str(int(df['Birth Year'].mode()[0]))
        print("For the selected filter, the most common birth year amongst "	        print("For the selected filter, the most common birth year amongst "
              "riders is: " + most_common_birth_year)	              "riders is: " + most_common_birth_year)
    except:	    except:
        print("We're sorry! There is no data of birth year for {}."	        print("We're sorry! There is no data of birth year for {}."
              .format(city.title()))	              .format(city.title()))
    print("\nThis took {} seconds.".format((time.time() - start_time)))	    print("\nThis took {} seconds.".format((time.time() - start_time)))
    print('-'*40)	    print('-'*40)
   	   
def raw_data(df):	def raw_data(df):
    """	    """
    Asks user if they want to see 5 lines of raw data.	    Asks user if they want to see 5 lines of raw data.
    Returns the 5 lines of raw data if user inputs `yes`. Iterate until user response with a `no`	    Returns the 5 lines of raw data if user inputs `yes`. Iterate until user response with a `no`
    """	    """
    print('\nCalculating raw data...\n')	    print('\nCalculating raw data...\n')
    start_time = time.time()	    start_time = time.time()
    count = 0	    count = 0
    while True:	    while True:
        answer = input('Would you like to see 5 lines of raw data? Enter yes or no: ')	        answer = input('Would you like to see 5 lines of raw data? Enter yes or no: ')
        # Check if response is yes, print the raw data and increment count by 5	        # Check if response is yes, print the raw data and increment count by 5
        if answer=='yes':	        if answer=='yes':
            for i in range(count,len(df.index)):	            for i in range(count,len(df.index)):
                print(" ")	                print(" ")
                print(df.iloc[count:count+5])	                print(df.iloc[count:count+5])
                print(" ")	                print(" ")
                count+=5	                count+=5
                print("-"*100)	                print("-"*100)
                break;	                break;
        else:	        else:
             break;	             break;
                	                
        # otherwise break	        # otherwise break
    	    
    print("\nThis took {} seconds.".format((time.time() - start_time)))    	    print("\nThis took {} seconds.".format((time.time() - start_time)))    
    print('-'*40)	    print('-'*40)
        	        
def main():	def main():
    while True:	    while True:
        '''	        '''
        Here we get Input From user In which base that want to filter data	        Here we get Input From user In which base that want to filter data
        '''	        '''
        city, month, day = get_filters() 	        city, month, day = get_filters() 
        while True:	        while True:
            print("**********Your selected city,month,day is mentioned Below **********")	            print("**********Your selected city,month,day is mentioned Below **********")
            print("Your Selected City  is = {}.".format(city))	            print("Your Selected City  is = {}.".format(city))
            print("Your Selected Month is = {}.".format(month))	            print("Your Selected Month is = {}.".format(month))
            print("Your Selected Day   is = {}".format(day))	            print("Your Selected Day   is = {}".format(day))
            verify = str(input("If above show data is right enter 'y' else 'n'\n "))	            verify = str(input("If above show data is right enter 'y' else 'n'\n "))
            print("")	            print("")
            if verify== 'n':	            if verify== 'n':
                print("*****************Let's Try Again**********")	                print("*****************Let's Try Again**********")
                get_filters()	                get_filters()
                continue	                continue
            else:	            else:
                print("\t\tGreat we are ready to go ahead >>>")	                print("\t\tGreat we are ready to go ahead >>>")
                break;	                break;
            	            
        print("*"*100)  	        print("*"*100)  
        #load the city,month and day which user provide    	        #load the city,month and day which user provide    
        df = load_data(city, month, day)	        df = load_data(city, month, day)
        print()	        print()
        print()	        print()
        print("\t\tThe Bikeshare Data represent based on Your filter mentoned Below")	        print("\t\tThe Bikeshare Data represent based on Your filter applied mentoned Below")
        # Display the Data based on user applied filter	        # Display the Data based on user applied filter
        time_stats(df)	        time_stats(df)
        station_stats(df)	        station_stats(df)