# Horoscope_predictions
Using webscraping and Neural Networks to generate horoscopes.

### USAGE

driver.py contains the main method for the web scraping portion. Simply navigate into the
src directory and run:

```
python3 driver.py <DEST_FILE_PATH>
```

Where DEST_FILE_PATH is the destination file. If it exists, it will be appended to.
If it does not exist, it will be created.


This code includes use of time.sleep(1) for every page call, so as to not overload the
server, so please allow time for this to run. Removing this call could act as a DOS to
the server, and slow the page down, which would be unethical to other users and frankly
just a rude move to the host.
