1. This file is configured in order to be able to connect the the web servers without needing to remember the ip.
2. Because everything is connected via proxy i can connect to each system from one another.
3. HAProxy configuration & documentation requirements
	- How to set up a HAProxy load balancer
		- The files modified are SSL is all deleted or commented out and Frontend and Backend is added to the etc/hapoxy file.
		- The configs set were frontend setup a bind and default backend, and backend setup balance, httpchk and, the server to connect to
		- The restart service use 'sudo systemctl restart haproxy.
		- Resources used are both websites 10.0.1.10 and 10.0.1.11.
	- How to set up a webserver
		- The files that were modified were i added a index.html file to both webservers located at /var/www/html
		- Configurations set was just apping index files given for project to display new webpage.
		- Site content files are lotacted in the index.html file that i made with a path of /var/www/html/index.html
		- Sudo reboot will restart the webservers.
		- Resources: https://www.haproxy.com/blog/the-four-essential-sections-of-an-haproxy-configuration/, and Lecture recordings.
	-webServer1:![photo description](Screenshots/webServer1.PNG)
	-webServer2:![photo description](Screenshots/webServer2.PNG)
