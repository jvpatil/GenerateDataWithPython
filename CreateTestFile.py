# -*- coding: utf-8 -*-
import csv
import itertools
import random
import sys
import os
import time
from datetime import datetime,timedelta
from Data import input_data
import config
#from tqdm import tqdm
# import GenerateData.Data.input_data
from random import randint


def writer():
    global batch_size,new_batch_size
    project_location = os.getcwd()
    file_directory = os.path.join(project_location,"Output")
    file_path = os.path.curdir
    sys.stdout.write(file_path)

    if len(sys.argv) > 1:
        number_of_records = sys.argv[1]
    else:
        number_of_records = input("\nPLEASE ENTER NUMBER OF RECORDS :: ")
        # file = input("\nPLEASE ENTER FILE NAME :: ")
    batch_size = (int(number_of_records) / 100)  # = (1/100)*total_count
    new_batch_size = (int(number_of_records) / 100)

    if len(sys.argv) > 2 :
        if '.' not in sys.argv[2]:
            extension = input("You missed to enter file extension. Please enter extension :" )
            file = sys.argv[2] + "." + extension.replace('.','').strip()
        else:
            file = sys.argv[2].strip()
    else:
        file = config.file

    print("Output file path is :", file_directory)
    #with open(file_directory +'\\Test.csv', mode='a', newline='') as csv_file:
    with open(file_directory + "\\" + file, mode='w',newline='') as csv_file:
        # csv_file_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_file_writer = csv.writer(csv_file, delimiter=config.delimeter, quotechar=config.quote, quoting=csv.QUOTE_ALL)
        csv_file_writer.writerow(["CUSTOMER_ID", "EMAIL_ADDRESS", "FIRST_NAME", "LAST_NAME", "GENDER","DOB","CITY","STATE","ADDRESS","ORDER_STATUS","ORDER_SOURCE","ORDER_DATE"])

        start_time = datetime.now()
        time_for_batch,time_to_finish = start_time,start_time

        sys.stdout.write('\n\n*** STARTED GENERATING FILE WITH %s RECORDS ***\n\n' %(number_of_records))
        # for i in tqdm(range(0,int(number_of_records))):
        for i in range(0,int(number_of_records)):
            cust_id = i
            email = "rsys"+str(i)+"@oracle.com"
            gender = random.choice(input_data.gender)
            if gender == 'M':
                first_name = random.choice(input_data.male_first)
            else:
                first_name = random.choice(input_data.female_first)
            last_name = random.choice(input_data.last_names)
            dob = random_date()
            city = random.choice(input_data.cities)
            state = random.choice(input_data.states)
            address = random.choice(input_data.address)
            order_status = random.choice(input_data.order_status)
            order_source = random.choice(input_data.order_source)
            web_events = random.choice(input_data.web_events)
            purchase_date = random_timestamp("date")
            csv_file_writer.writerow([cust_id, email, first_name, last_name,gender,dob,city,state,address,order_status,order_source,purchase_date])
            # display_progress(int(number_of_records),i)
            # batch_time, total_time = get_average_time(int(number_of_records), i+1, start_time)
            # if batch_time:
            #     time_for_batch = batch_time
            #     time_to_finish = total_time
            printProgressBar(i+1, int(number_of_records))
        time.sleep(1)
        end_time = datetime.now()
        total_time = get_run_time(end_time,start_time)
        sys.stdout.write("\n*** FINISHED GENERATING FILE ***\n")

def display_progress(max, curr):
    curr = int(curr)+int(1)
    sys.stdout.write('\r')
    bar_size = 20
    sys.stdout.write("[%-20s] %d%%" % ('#'*int((curr/max)*bar_size), (curr/max)*100))
    sys.stdout.flush()

def printProgressBar (iteration, total_count,prefix = 'Progress :', suffix = 'Complete', decimals = 2, length = 50, fill = '█'):
    global start_time
    # fill = '░'
    if iteration == 1:
        start_time = datetime.now()
    elapsed_time, eta_time = calculate_time(total_count,iteration,start_time)
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total_count)))
    filledLength = int(length * iteration // total_count)
    bar = fill * filledLength + '-' * (length - filledLength)
    sys.stdout.write('\r%s |%s| [%s%% %s] [Time elapsed %s] [ETA %s] %s' % (prefix, bar, percent, suffix,elapsed_time,eta_time,''))
    sys.stdout.flush()

def calculate_time(total_count,iteration,start_time):
    end_time = datetime.now()
    time_in_seconds = end_time-start_time
    time_elapsed = str(time_in_seconds)[:7]
    # time_elapsed = '{}'.format(time_in_seconds)[:7]

    remaining_time = (time_in_seconds *float((total_count / iteration))) - time_in_seconds
    remaining_time = str(remaining_time)[:7]
    # return time_elapsed, "..."
    return time_elapsed, remaining_time

def get_average_time(total_count,iteration,start_time):
    global batch_size, new_batch_size
    if iteration == new_batch_size:
        batch_time = datetime.now()
        average_time = batch_time - start_time
        time_required_to_finish = average_time * float((total_count) / new_batch_size)
        # print("Time for Batch ",batch_size, "is ",time_required_to_finish)
        new_batch_size += batch_size
        return batch_time, time_required_to_finish
    else:
        return None,None


def random_timestamp(date_or_timestamp="timestamp"):
    import datetime
    date = datetime.date(randint(2015, 2025), randint(1, 12), randint(1, 28))
    time = datetime.time(randint(0, 23), randint(0, 59), randint(0, 59))
    timestamp = str(date)+ ' ' +str(time)
    return timestamp

def random_date(date_or_timestamp="timestamp"):
    # format = "YYYY-MM-DD HH24:MI:SS"
    import datetime
    date = datetime.date(randint(2015, 2025), randint(1, 12), randint(1, 28))
    return date

def get_run_time(end_time,start_time):
    # timeTaken+=60
    timeTaken = (end_time-start_time).total_seconds()
    if timeTaken > 3600:
        Hour, R = divmod(int(timeTaken), 3600)  # Qoutient is stored in Hour and Remainder in R
        Minutes, Seconds = divmod(R, 60)
        totalTime = str(Hour) + " hour" + "," + str(Minutes) + " Min" + "," + str(Seconds) + " Sec"
    elif timeTaken > 60:
        Minutes, Seconds = divmod(int(timeTaken), 60)  # Qoutient is stored in Minutes and Remainder in Seconds
        totalTime = str(Minutes) + " Min" + "," + str(Seconds) + " Sec"
    else:
        totalTime = str(int(timeTaken)) + " Sec"
    return totalTime

def spinning_cursor():
    while True:
        # for cursor in '◐◓◑◒':
        for cursor in '⏳-⌛':
            yield cursor


if __name__ == '__main__':
    writer()
