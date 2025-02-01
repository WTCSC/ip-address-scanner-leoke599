# IP Address Scanner
This program takes a cidr address from the command line and scans all the available hosts to see if they're up or down. If a host is up, it will also show the time in miliseconds it took for the host to respond. There is a general error handling message if it encounters a problem.

## Installation
To use the scanner, follow these steps:

1. Clone the repository onto your machine 
2. Use this command: "python scanner.py (cidr_address)" in the command line

It does take time to ping every host

## Troubleshooting
I didn't face any problems while testing, but if you do, you can try these solutions:

1. Make sure you have python downloaded
2. Make sure spelling is correct in the command line
3. Make sure the cidr address is a cidr address and not any other type of ip address (check this website for detailed information regarding cidr addresses: https://aws.amazon.com/what-is/cidr/#:~:text=Classless%20Inter%2DDomain%20Routing%20)