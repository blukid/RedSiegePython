Project 5 - Living on the Land!

Scenario: You successfully delivered a phishing payload and now have access to a machine inside your target's network. It appears that your user is pretty locked down and you can't seem to get some of your favorite tools to run on the machine. Luckily for you, Python is installed on the machine and can be utilized in place of what's normally in your toolkit.

Beginner Task: Write a script that can perform a ping sweep of a range of IP addresses and port scan any host that responds.

Intermediate Task: Add "smart" functionality. Only port scan alive hosts, add functionality to allow the user to only scan the top 10, 100, 1000 Nmap ports. The list can be found in /usr/share/nmap/nmap-services if you have nmap installed on a system. sudo sort -r -k3 /usr/share/nmap/nmap-services

Advanced Task: Add some additional service enumeration based on open ports. This is a rabbit hole you can go down very deep. For this exercise, pick three different services and add some enumeration functionality of your choosing.
