# Req_HTTP

Level 1: I provided Python code 'Answer.py.' 

It fires HTTP requests for 'timeout' seconds to a web page, and return the 'status_code.'

It saves all status codes in a 'list' and keeps the success amount of time in the 'total_success' variable using the elapsed method.

Based on the first digit of the status code calculates the count and percentage of different responses based on five classes defined by the standard:

1xx informational response – the request was received, continuing process

2xx successful – the request was successfully received, understood, and accepted

3xx redirection – further action needs to be taken in order to complete the request

4xx client error – the request contains bad syntax or cannot be fulfilled

5xx server error – the server failed to fulfil an apparently valid request


The output is something like:

total number of attempts =  834

total success time 139.84401699999998 seconds

response details: 

[[200 834]]

2xx successful response 100.0 %

