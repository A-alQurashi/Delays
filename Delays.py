Delays can be also implemented by using the following methods.

The first method:

import time
time.sleep(5) # Delay for 5 seconds.
The second method to delay would be using the implicit wait method:

 driver.implicitly_wait(5)
The third method is more useful when you have to wait until a particular action is completed or until an element is found:

self.wait.until(EC.presence_of_element_located((By.ID, 'UserName'))