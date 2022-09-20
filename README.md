# ExercisingProtectionPractices
This project serves as an introduction to server-side sandboxing and privilege separation within the context of the straightforward Python online application "zoobar," which allows users to exchange "zoobars" (credits) with one another. We developed a privilege-separated web server, investigated any security holes, and divided the application code into lower-privileged areas in order to lessen the impact of any potential flaws. Additionally, we looked for buffer overflows vulnerabilities and how they may be used to upload code to a server remotely and bypass non-executable stack security.

This project was used as a learning aid for a new programming language or other infrastructure. For instance, iad to understand C programming language, x86 assembly language, gdb, etc. in order to verify some of the security holes. One has to have a comprehensive awareness of a range of infrastructure components to understand attacks and defenses in real-world circumstances. Because security weaknesses regularly occur in unexpected settings, it need in-depth expertise to develop exploits and countermeasures against them.


The following issues needed to be resolved: 
* Safeguard both tokens and passwords entered by users in the zoobar site.
* Configure the authentication service and what can run in the client.
* Configure how to handle a new user authentication.

Many security exploits are due to software bugs. This lab will introduce you to a powerful technique for finding bugs in software: symbolic execution. This can be a good way to audit your application for security vulnerabilities so that you can then fix them. By the end of this lab, you will have a symbolic execution system that can take the Zoobar web application and mechanically find inputs that trigger different kinds of bugs in Zoobar that can lead to security vulnerabilities. (More precisely, this lab will be building a concolic execution system; we will explain what this means later on.)



