# Create a queue system have the stub functions return after set of seconds to simulate processing or server return time


import time
import random
import queue
import threading
import requests
import datetime
import subprocess
import re
import socket
import urllib3

def queueSystem() :
    # Create a queue
    q = queue.Queue()
    # Create a thread to process the queue
    t1 = threading.Thread(target=processQueue, args=(q,))
    # Start the thread
    t1.start()
    # Create a thread to add items to the queue
    t2 = threading.Thread(target=addToQueue, args=(q,))
    # Start the thread
    t2.start()


def processQueue(q) :
    # Process the queue
    while True :
        # Check if there are items in the queue
        if not q.empty() :
            # Get the item from the queue
            item = q.get()
            # Process the item
            processItem(item)
            # Put the item back on the queue
            q.put(item)
        else :
            # Sleep for a second
            time.sleep(1)


def processItem(item) :
    # Print the item
    print(item)
    # Sleep for a random amount of time
    time.sleep(random.randint(1,3))


def addToQueue(q) :
    # Add items to the queue
    while True :
        # Add an item to the queue
        q.put(random.randint(1,100))
        # Sleep for a second
        time.sleep(1)


# create successful and failed processes randomly
def create_processes():
    # create a list of processes
    processes = ['process1', 'process2', 'process3', 'process4', 'process5', 'process6', 'process7', 'process8', 'process9', 'process10']
    # create a list of successful processes
    successful_processes = []
    # create a list of failed processes
    failed_processes = []
    # create a list of successful processes
    for i in range(0, len(processes)):
        # create a random number
        random_number = random.randint(0, 1)
        # if the random number is 0
        if random_number == 0:
            # add the process to the successful processes list
            successful_processes.append(processes[i])
        # if the random number is 1
        else:
            # add the process to the failed processes list
            failed_processes.append(processes[i])
    # return the successful and failed processes
    return processes, successful_processes, failed_processes


# how many processes are running in the system and success of each process
def get_process_count():
    # create a list of processes
    processes = ['process1', 'process2', 'process3', 'process4', 'process5', 'process6', 'process7', 'process8', 'process9', 'process10']
    # create a list of successful processes
    successful_processes = []
    # create a list of failed processes
    failed_processes = []
    # create a list of successful processes
    for i in range(0, len(processes)):
        # create a random number
        random_number = random.randint(0, 1)
        # if the random number is 0
        if random_number == 0:
            # add the process to the successful processes list
            successful_processes.append(processes[i])
        # if the random number is 1
        else:
            # add the process to the failed processes list
            failed_processes.append(processes[i])
    # return the successful and failed processes
    return len(successful_processes), len(failed_processes)

def main() :
    # Call the queue system
    queueSystem()

    # create a list of processes
    processes, successful_processes, failed_processes = create_processes()

    # Get the number of processes running
    number_of_processes_running = len(processes)
    # Get the number of processes that have completed successfully
    number_of_processes_successful = len(successful_processes)
    # Get the number of processes that have failed
    number_of_processes_failed = len(failed_processes)


    # print the processes
    print("Processes: ", number_of_processes_running)
    # print the successful processes
    print("Successful processes: ", number_of_processes_successful)
    # print the failed processes
    print("Failed processes: ", number_of_processes_failed)


    # Show when a process is successful
    for i in range(0, len(successful_processes)):
        print(successful_processes[i], " was successful")

    # Show when a process is failed
    for i in range(0, len(failed_processes)):
        print(failed_processes[i], " failed")


if __name__ == '__main__':
    main()