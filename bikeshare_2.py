import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:
        print('\nWhat city do you want to analyze the data for?')
        city = input('Chicago, New York City or Washington? \n').lower()
        if city == 'chicago' or city == 'new york city' or city == 'washington':
            city = city.capitalize()
            print(f"\n{city}! Okay Let's go further\n")
            city = city.lower()
            break
        else:
            print('enter a valid city!', '\n, chicago, new york city or washington')
            continue
        break
        
    while True:
        # if choice:
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        filter = input('How do you want to filter the data? \nBy month, day, both, or you do not want to filter at all? Type "no" for no filter.\n').lower() 
        if filter == 'month': 
            print('\nYou chose to filter by month!')                                
            # months = ['January', 'February', 'March', 'April', 'May', 'June']
            day = 'all' 
            month = input('Which month do you want explore? ').capitalize()
            if month in months:
                print(f'Selected month is {month}.\n') 
                break
            else:
                print('\ninput a valid month!', '\n, January to June or "all" for all months\n')
                continue
            break


        elif filter == 'day':
            print('\nYou chose to filter by day of week!')
            month = 'all' 
            day = input('Which day do you want to explore? ').capitalize()
            if day in days:
                print(f'Selected day is {day}.\n') 
                break                 
            else:
                print('\ninput a valid day of week or "all" for all days!\n')  
                continue
            break

        elif filter == 'both':
            print('\nYou chose to filter by both month and day!')
            month = input('Which month do you want to explore? ').capitalize()
            day = input('Which day do you want to explore? ').capitalize()
            if (month in months) and (day in days):
                print(f'Selected month and day are {month} and {day}\n')
                break 
            elif (month not in months) or (day not in days):
                print('\nYou entered an invalid input, please re-enter your choice\n')
                continue
            break

        elif filter == 'no':
            month = 'all'
            day = 'all'
            break

        else:
            print('input a valid filter!') 
            continue
        break
            
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    
    newCity = pd.read_csv(CITY_DATA[city])

    df = newCity

    df['Start Time'] = pd.to_datetime(df['Start Time'], format = '%Y-%m-%d %H:%M:%S')
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()

    
    if month.lower() != 'all':
        # filter by month to create the new dataframe
        df = df[df['month'] == month.capitalize()]
    

    # filter by day of week if applicable
    if day.lower() != 'all':
        df = df[df['day_of_week'] == day.capitalize()]    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # display the most common month
    commonest_month = df.month.mode()
    print(f'The most common day for bike riding is {commonest_month}')

    # display the most common day of week
    commonest_day = df.day_of_week.mode()
    print(f'The most common month for bike riding is {commonest_day}')

    # display the most common start hour
    df['hour'] =  df['Start Time'].dt.strftime("%I %p")
    most_common_start_hour = df['hour'].mode()[0]
    print(f'The most common hour for bike riding is {most_common_start_hour}.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_used_start_station = df['Start Station']
    most_frequent_start_station = most_used_start_station.mode()
    print(f'The most commonly used Start Station is {most_frequent_start_station}.')
    # display most commonly used end station
    most_used_end_station = df['End Station']
    most_frequent_end_station = most_used_end_station.mode()
    print(f'The most commonly used Start Station is {most_frequent_end_station}.')

    # display most frequent combination of start station and end station trip
    most_frequent_combination_of_start_station_and_end_station_trip = 'From ' + df['Start Station'] + ' to ' + df['End Station']
    print('\n Most Frequent Combination Of Start Station And End Station Trip :\n', most_frequent_combination_of_start_station_and_end_station_trip.mode()[0])
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
#     """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()


#     # display total travel time
    total_ride_time = np.sum(df['Trip Duration'])
    time_day = total_ride_time // (24 * 3600)
    d_time = total_ride_time % (24 * 3600)
    hour = d_time // 3600
    d_time %= 3600
    minutes = d_time // 60
    d_time %= 60
    seconds = d_time
    print (f"\nThe total travel time is {time_day} days {hour}:{minutes}:{seconds}. \n")

#     # display mean travel time
    avg_ride_time = np.mean(df['Trip Duration'])
    time_day = avg_ride_time // (24 * 3600)
    d_time = avg_ride_time % (24 * 3600)
    hour = d_time // 3600
    d_time %= 3600
    minutes = d_time // 60
    d_time %= 60
    seconds = d_time
    print (f"\nThe average travel time is {time_day} days {hour}:{minutes}:{seconds}. \n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def user_stats(df):
#     """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

#     # Display counts of user types
    
    print(df['User Type'].value_counts())
    print(' ')

    print(df['Gender'].value_counts())
    print(' ')

    earliest = int(df['Birth Year'].min())
    print (f"\nThe earliest year of birth is\n {earliest}.\n")

    latest = int(df['Birth Year'].max())
    print (f"The latest year of birth is\n {latest}.\n")
    
    most_frequent= int(df['Birth Year'].mode()[0])
    print (f"The most frequent year of birth is\n {most_frequent}.\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.upper() == 'YES' or restart.upper() == "Y":
            main()
        else:
            break

if __name__ == "__main__":
	main()
