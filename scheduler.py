import time
from billing_pull import fetch_billing

while True:
    fetch_billing()
    time.sleep(300)