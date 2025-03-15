# -*- coding: utf-8 -*-
"""
Created on Sat Mar 15 3:41:47 2025

@author: IAN CARTER KULANI

"""

from colorama import Fore
import pyfiglet
import os
font=pyfiglet.figlet_format("Side Channel Attack Detector")
print(Fore.GREEN+font)

import requests
import time
import numpy as np
import sys

# Function to detect timing vulnerabilities in the website's responses
def detect_timing_attack(url, num_requests=50):
    # List to store the response times for requests
    response_times = []

    print(f"Detecting timing attacks on: {url}...\n")
    
    # Perform multiple requests and measure the response times
    for i in range(num_requests):
        try:
            # Record the start time of the request
            start_time = time.time()
            
            # Make a GET request to the provided URL
            response = requests.get(url)
            
            # Record the end time of the request
            end_time = time.time()
            
            # Calculate the response time and add to the list
            response_time = end_time - start_time
            response_times.append(response_time)
            
            print(f"Request {i+1}: Response time = {response_time:.4f} seconds")
            
        except requests.exceptions.RequestException as e:
            print(f"Error with request {i+1}: {e}")
            continue

    # Analyze the response times to detect anomalies
    print("\nAnalyzing response times for potential timing vulnerabilities...")
    mean_time = np.mean(response_times)
    std_dev = np.std(response_times)

    # Print basic statistics
    print(f"Mean response time: {mean_time:.4f} seconds")
    print(f"Standard deviation of response times: {std_dev:.4f} seconds")

    # Detect if there's an unusually high deviation in the response times
    if std_dev > 0.1 * mean_time:
        print("\nWarning: High variability in response times detected. This may indicate a timing attack vulnerability.")
    else:
        print("\nNo significant timing anomalies detected.")

# Main function to prompt user input
def main():
    # Prompt the user to enter the URL of the website
    url = input("Enter the URL of the website to check for side-channel timing attacks:").strip()

    if not url.startswith("http://") and not url.startswith("https://"):
        print("Invalid URL. Make sure to include 'http://' or 'https://'.")
        sys.exit(1)

    # Call the function to detect timing attacks
    detect_timing_attack(url)

if __name__ == "__main__":
    main()
