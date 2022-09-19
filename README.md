# ExercisingProtectionPractices
This project serves as an introduction to server-side sandboxing and privilege separation within the context of the straightforward Python online application "zobar," which allows users to exchange "zoobars" (credits) with one another. We developed a privilege-separated web server, investigated any security holes, and divided the application code into lower-privileged areas in order to lessen the impact of any potential flaws. Additionally, you looked for buffer overflows vulnerabilities and how they may be used to upload code to a server remotely and bypass non-executable stack security.

This project may potentially be used as a learning aid for a new programming language or other infrastructure. For instance, you must master every nuance of the C programming language, x86 assembly language, gdb, etc. in this lab. One has to have a comprehensive awareness of a range of infrastructure components to understand attacks and defenses in real-world circumstances. Because security weaknesses regularly occur in unexpected settings, it need in-depth expertise to develop exploits and countermeasures against them.


The following issues needed to be resolved: 
* How to safeguard both tokens and passwords;
* What must run in the authentication service and what can run in the client.
* How to handle a new user authentication.

By keeping a hash of the user's password—that is, the outcome of applying a hash function to the password—instead of the password itself, hashing defends against this attack. An adversary won't be able to get the user's password directly if the hash function is hard to reverse (i.e., is a cryptographically secure hash). A server can still verify that a user entered the proper password during login by hashing the password and comparing the result to the value that was previously saved.




