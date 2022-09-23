# ExercisingProtectionPractices
This project containts lab 1 and lab 2 of the 6.858 spring 2020 lab from MIT, it serves as an introduction to server-side sandboxing and privilege separation within the context of the straightforward Python online application "zoobar," which allows users to exchange "zoobars" (credits) with one another. Using the provided code we developed a privilege-separated web server, investigated any security holes, and divided the application code into lower-privileged areas in order to lessen the impact of any potential flaws. Additionally, we looked for buffer overflows vulnerabilities and how they may be used to upload code to a server remotely and bypass non-executable stack security.

Both labs wwere used as a learning aid for a new programming language or other infrastructure. For instance, i had to understand C programming language, x86 assembly language, gdb, etc. in order to verify some of the security holes. One has to have a comprehensive awareness of a range of infrastructure components to understand attacks and defenses in real-world circumstances. Because security weaknesses regularly occur in unexpected settings, it requires in-depth expertise to develop exploits and countermeasures against them.

The following issues needed to be resolved for lab#1: 
* Safeguard both tokens and passwords entered by users in the zoobar site.
* Configure the authentication service and what can run in the client.
* Configure how to handle a new user authentication.
* Fix any buffer overflows present.
* Manage permision and service aquisition.

The following issues needed to be resolved for lab#2: 
