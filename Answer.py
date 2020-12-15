import time
import numpy as np
import requests

timeout = time.time() + 5*60 # seconds from now, time to fire HTTP request

list = [ ] #list of responses
total_success = 0 #total success in seconds


while True:
    r = requests.get('https://www.youtube.com/')
    list.append(r.status_code)
    if int(str(r.status_code)[:1]) == 2:
        total_success = total_success + r.elapsed.total_seconds()
    if time.time() > timeout:
        break

numpy_list = np.array(list)
(unique, counts) = np.unique(numpy_list, return_counts=True)
frequencies = np.asarray((unique, counts)).T
all = np.sum(frequencies, axis =0)


print('total number of attempts = ', all[1])
print('total success time', total_success , 'seconds')
print('response details: ')
print(frequencies)


for code in frequencies[:, 0]:
    if int(str(code)[:1]) == 1:
        print('1xx informational response',
              ((frequencies[np.where(frequencies == code)[0], np.where(frequencies == code)[1] + 1] / all[1])[0])*100 , '%')
    elif int(str(code)[:1]) == 2:
        print('2xx successful response',
              ((frequencies[np.where(frequencies == code)[0], np.where(frequencies == code)[1] + 1] / all[1])[0])*100 , '%')
    elif int(str(code)[:1]) == 3:
        print('3xx redirection response',
              ((frequencies[np.where(frequencies == code)[0], np.where(frequencies == code)[1] + 1] / all[1])[0])*100 , '%')
    elif int(str(code)[:1]) == 4:
        print('4xx client error response',
              ((frequencies[np.where(frequencies == code)[0], np.where(frequencies == code)[1] + 1] / all[1])[0])*100 , '%')
    elif int(str(code)[:1]) == 5:
        print('5xx server error response',
              ((frequencies[np.where(frequencies == code)[0], np.where(frequencies == code)[1] + 1] / all[1])[0])*100 , '%')
    else:
        print('Unknown HTTP status code')
