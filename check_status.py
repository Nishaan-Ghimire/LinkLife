import sys
import requests
# Check if the file name is provided as a command-line argument
if len(sys.argv) < 2:
    print("Usage: python script.py <file_name>")
    sys.exit(1)

# Get the file name from the command-line argument
file_name = sys.argv[1]

try:
    # Open the file for reading
    with open(file_name, 'r') as file:
        if(len(sys.argv) == 3):
            output_file_name = sys.argv[2]
            print(f'Output of scan is saved in file : {output_file_name}')
        else:
            output_file_name = 'subdomain_status_code.txt'
            print(f'Output of scan is saved in file : {output_file_name}')
        with open(output_file_name, 'w') as output_file:    
        # Loop through each line in the file
            for line in file:
                # Process each line here
                # print(f'https://{line}')
                line = line.strip()
                try:
                    req = requests.get(f'https://{line}')
                    status = req.status_code
                    # For example, you can print the line
                    print(f'https://{line} -- > {status}')
                    output_file.write(f'https://{line} -- > {status}\n')
                except:
                    print(f'https://{line} -- > error')
                    output_file.write(f'https://{line} -- > error\n')
                continue    
except FileNotFoundError:
    print("File not found: " + file_name)
    sys.exit(1)
