# Bug bounty scripts
Here are some bug bounty scripts for testing an assett through automatic scripts and predefined lists

### wp\_ssrf\_exploit.py
This is a wordpress exploit that takes advantage of the `xmlrpc.php` file in the wordpress source code, it has a function called `system.pingback` designed to check if a blog has linked a page on the site. 

This can be exploited to gain an SSRF or DDoS another site, the code is used in the following way, you run it using python3, then supply a domain name and a file of urls, ips or hostnames to request.

`python3 wp_ssrf_exploit.py domain.name wordlists/common-ips.txt`

### ip\_CIDR\_splitter.py
This is simply a script to convert and internal IP range to a list of ips the other scripts can use. It's most effective to save it to a file unless the program takes stdin as a source.

The code is run by running it with python3, and supplying it with an CIDR IP range. Supplying it with a regular IP just produces that single IP to the output.

`python3 ip_CIDR_splitter.py 192.168.1.0/24 > optional.file`

