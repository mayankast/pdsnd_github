import time
import pandas as pd
import numpy as np

#This is the doc-string for this program

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
val_months={'january':1,'february':2,'march':3,'april':4,'may':5,'june':6,'july':7,'august':8,'september':9,'october':10,'november':11,'december':12}
val_days={'monday':0,'tuesday':1,'wednesday':2,'thursday':3,'friday':4,'saturday':5,'sunday':6}
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    chk_dig = False
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while (chk_dig == False):
        city = input("Enter the city. Enter '1' to get list of cities.  ").lower()
        if (city == '1'):
            print("Valid input city names are 'chicago', 'new york city', 'washington' \n")
            continue
        elif (city in CITY_DATA.keys()):
            chk_dig = True
        else:
            print("Invalid city name. Please try again \n")
            continue
    # TO DO: get user input for month (all, january, february, ... , june)
    chk_dig = False
    while (chk_dig == False):
        valid_mnth=['january','february','march','april','may','june','july','august','september','october','november','december','all']
        month = input("Enter the month or 'all' for all months. Enter '1' to get list of valid month names \n").lower()
        if (month == '1'):
            print(valid_mnth)
            continue
        elif (month in valid_mnth):
            chk_dig = True
        else:
            print("Invalid month. Please try again")
            continue

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    chk_dig = False
    while (chk_dig == False):

        valid_day=['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
        day = input(" Enter the day. Enter '1' to get list of valid day names. \n").lower()
        if (day == '1'):
            print(valid_day)
            continue
        elif (day in valid_day):
            chk_dig = True
        else:
            print("Invalid month. Please try again")
            continue

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """


    if city=='chicago':
        df = pd.read_csv('./chicago.csv')
        if month=='all' and day=='all':
            #df = pd.read_csv('./chicago.csv')
            pass
        elif month!='all' and day !='all':
            #df = pd.read_csv('./chicago.csv')
            df = df[(pd.to_datetime(df['Start Time']).dt.month == val_months[month]) & (pd.to_datetime(df['Start Time']).dt.dayofweek ==val_days[day])]
        elif month!='all' and day =='all':
            #df = pd.read_csv('./chicago.csv')
            df = df[(pd.to_datetime(df['Start Time']).dt.month == val_months[month])]
        elif month=='all' and day !='all':
            #df = pd.read_csv('./chicago.csv')
            df = df[(pd.to_datetime(df['Start Time']).dt.dayofweek ==val_days[day])]
    if city=='new york city':
        df = pd.read_csv('./new_york_city.csv')
        if month=='all' and day=='all':
            #df = pd.read_csv('./new_york_city.csv')
            pass
        elif month!='all' and day !='all':
            #df = pd.read_csv('./new_york_city.csv')
            df = df[(pd.to_datetime(df['Start Time']).dt.month == val_months[month]) & (pd.to_datetime(df['Start Time']).dt.dayofweek ==val_days[day])]
        elif month!='all' and day =='all':
            #df = pd.read_csv('./new_york_city.csv')
            df = df[(pd.to_datetime(df['Start Time']).dt.month == val_months[month])]
        elif month=='all' and day !='all':
            #df = pd.read_csv('./new_york_city.csv')
            df = df[(pd.to_datetime(df['Start Time']).dt.dayofweek ==val_days[day])]
    if city=='washington':
        df = pd.read_csv('./washington.csv')
        if month=='all' and day=='all':
            #df = pd.read_csv('./washington.csv')
            pass
        elif month!='all' and day !='all':
            #df = pd.read_csv('./washington.csv')
            df = df[(pd.to_datetime(df['Start Time']).dt.month == val_months[month]) & (pd.to_datetime(df['Start Time']).dt.dayofweek ==val_days[day])]
        elif month!='all' and day =='all':
            #df = pd.read_csv('./washington.csv')
            df = df[(pd.to_datetime(df['Start Time']).dt.month == val_months[month])]
        elif month=='all' and day !='all':
            #df = pd.read_csv('./washington.csv')
            df = df[(pd.to_datetime(df['Start Time']).dt.dayofweek ==val_days[day])]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    max_mnth = (pd.to_datetime(df['Start Time']).dt.month).value_counts().idxmax()
    for months,val in val_months.items():
        if val == max_mnth:
            print("Most common month of travel is {}".format(months))

    # TO DO: display the most common day of week
    max_day = (pd.to_datetime(df['Start Time']).dt.dayofweek).value_counts().idxmax()
    for days,val in val_days.items():
        if val == max_day:
            print("Most common day of travel is {}".format(days))

    # TO DO: display the most common start hour
    max_hour = (pd.to_datetime(df['Start Time']).dt.hour).value_counts().idxmax()
    print("Most common start hour of travel is {}".format(max_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    max_strt_stn = df['Start Station'].value_counts().idxmax()
    print ("Most commonly used start station is {}".format(max_strt_stn))
    # TO DO: display most commonly used end station
    max_stp_stn = df['End Station'].value_counts().idxmax()
    print ("Most commonly used end station is {}".format(max_stp_stn))
    # TO DO: display most frequent combination of start station and end station trip
    df['Combo'] = df['Start Station'] + ' -To- ' + df['End Station']
    max_combo = df['Combo'].value_counts().idxmax()
    print ("Most frequent station trip is {}".format(max_combo))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    df['Total_secs'] = (pd.to_datetime(df['Start Time']).dt.hour.astype(int))*3600 + (pd.to_datetime(df['Start Time']).dt.minute.astype(int))*60 + (pd.to_datetime(df['Start Time']).dt.second.astype(int)) - (pd.to_datetime(df['End Time']).dt.hour.astype(int))*3600 + (pd.to_datetime(df['End Time']).dt.minute.astype(int))*60 + (pd.to_datetime(df['End Time']).dt.second.astype(int))
    total_time = (df.Total_secs.sum().astype(int)/60).astype(int)
    print ("Total travelling time is {} minutes".format(total_time))
    # TO DO: display mean travel time
    mean_time = (df.Total_secs.mean().astype(int)/60).astype(int)
    print ("Mean travelling time is {} minutes".format(mean_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    if('User Type' in df):
        print(df['User Type'].fillna(value='No User Type').value_counts())
    else:
        print('No User Type data available for this city')

    # TO DO: Display counts of gender
    if('Gender' in df):
        print(df['Gender'].fillna(value='No Gender available').value_counts())
    else:
        print('No Gender data available for this city')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        early_year = int(df['Birth Year'].min())
        recent_year = int(df['Birth Year'].max())
        com_year = int(df['Birth Year'].value_counts().idxmax())
        print(" Following are birth year stats: \n Earliest Birth Year: {} \n Most recent Birth Year: {} \n Most common Birth Year: {}". format(early_year, recent_year, com_year))
    else:
        print("No birth year data for this city")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    df.drop("Combo", axis=1, inplace=True)
    num_choice = False
    init_row = 0
    pagination = False
    while num_choice == False:
        page_size = int(input("How many rows of data would you like to analyze? Enter range of 1-10"))
        num_of_rows = page_size
        if (num_of_rows >=1 and num_of_rows <=10):
            while pagination == False:
                print(df[init_row:num_of_rows])
                if init_row == 0:
                    while num_choice == False:
                        page_choice = input("Do you want to see next rows. Enter 'N' for next and 'E' to end")
                        if page_choice.lower() == 'n':
                            init_row = num_of_rows
                            num_of_rows+=page_size
                            print(df[init_row:num_of_rows])
                            #init_row = num_of_rows
                            #num_of_rows+=page_size
                            num_choice = True
                        elif page_choice.lower() == 'e':
                            pagination = True
                            num_choice = True
                        else:
                            print("Please enter valid input")
                else:
                        num_choice = False
                        while num_choice == False:
                            page_choice = input("Do you want to see next rows. Enter 'N' for next page, 'P' for previous page and 'E' to end")
                            if page_choice.lower() == 'n':
                                init_row = num_of_rows
                                num_of_rows+=page_size
                                print(df[init_row:num_of_rows])
                            elif page_choice.lower() == 'p':
                                num_of_rows = init_row
                                init_row-=page_size
                                print(df[init_row:num_of_rows])
                            elif page_choice.lower() == 'e':
                                pagination = True
                                num_choice = True
                            else:
                                print("Please enter a valid choice")


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        input_choice = False
        while input_choice==False:
            choice = input("Do you want to see raw date? Enter your choice Y/N: \n")
            if (choice.lower()=='y') or (choice.lower()=='yes'):
                display_data(df)
                input_choice = True
            elif (choice.lower()=='n') or (choice.lower()=='no'):
                input_choice = True
            else:
                ("Please enter valid input 'Y/N'")
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
