from simplecrypt import encrypt, decrpt
from pprint import pprint
import csv
import json

# Read in information from user
dc_in_filename = input('\nInput CSV filename (device-creds) : ') or 'device-creds'
key = input('Encrption key (cisco)            : ') or 'cisco'

with open(dc_in_filename, 'r') as dc_in:
    device_creds_reader = csv.reader(dc_in)
    device_creds_list = [device for device in device_creds_reader]

