import csv
import itertools
import random
import sys
import os
import time
from datetime import datetime

from Data import input_data
from tqdm import tqdm
# import GenerateData.Data.input_data
from random import randint

def writer():
    project_location = os.getcwd()

    file_directory = os.path.join(project_location,"Output")
    file_path = os.path.curdir
    print(file_path)

    if len(sys.argv) > 1:
        number_of_records = sys.argv[1]
    else:
        number_of_records = int(input("\nPLEASE ENTER NUMBER OF RECORDS :: "))

    print("Output file path is :", file_directory)
    with open(file_directory +'\\Test.csv', mode='a', newline='') as csv_file:
    # with open('.\\Output\\Test.csv', mode='a', newline='') as csv_file:
        csv_file_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_file_writer.writerow(["CUSTOMER_ID", "EMAIL_ADDRESS", "FIRST_NAME", "LAST_NAME", "GENDER","DOB","CITY","STATE","ADDRESS","ORDER_STATUS","ORDER_SOURCE","ORDER_DATE"])

        start_time = datetime.now()
        count = 0
        print("\n*** STARTED GENERATING FILE WITH ",number_of_records, " RECORDS ***\n")

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
            printProgressBar(i+1, int(number_of_records))
        time.sleep(1)
        end_time = datetime.now()
        total_time = get_run_time(end_time,start_time)
        print("\n*** FINISHED GENERATING FILE (Time Taken :: ",total_time,") ***")

def display_progress(max, curr):
    # for i in range(21):
    curr = int(curr)+int(1)
    sys.stdout.write('\r')
    bar_size = 20
    sys.stdout.write("[%-20s] %d%%" % ('#'*int((curr/max)*bar_size), (curr/max)*100))
    sys.stdout.flush()
    # time.sleep(0.25)

def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor

spinner = itertools.cycle(['/','_','\\'])
# spinner = spinning_cursor()

def printProgressBar (iteration, total, prefix = 'Progress :', suffix = 'Complete', decimals = 1, length = 50, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()

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


if __name__ == '__main__':
    writer()
