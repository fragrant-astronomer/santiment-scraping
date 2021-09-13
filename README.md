# Setup Instructions
Query santiment on-chain insights with Python

# Step 1: 
Install Python 3 and pip on your machine if you have not already done so:

https://www.python.org/downloads/

https://pip.pypa.io/en/stable/installation/

# Step 2:
Verify your Python 3 and pip installations on a terminal:
> python3 --version;
> pip --version

# Step 3:
Make an account on santiment.net if you have not already done so:

https://santiment.net/

Once you have created your account, navigate to the following page and generate an API key:
https://api.santiment.net/account

You will want to save this key for future reference. By including this key in programmatic queries, Santiment knows that the queries are coming from authenticated users.

![image](https://user-images.githubusercontent.com/90649342/133146245-1f47a92a-1975-42f4-9ae0-e83d72999610.png)


# Step 4:
We will now install a few Python dependencies to be able to run and visualize our queries.

> pip install sanpy

> pip install matplotlib

# Step 5:
Download the sample python script sampleQuery.py to your machine. You can do this by cloning this repository.

Replace the dummy api key on line 3 with the API key you generated on step 3

> san.ApiConfig.api_key = 'my-api-key'

# Step 6:
Open a new terminal and navigate to the directory containing sampleQuery.py. Then, run the script to execute the query!

> python3 sampleQuery.py


You should expect to see a graph of the price of Ethereum as shown below:

![image](https://user-images.githubusercontent.com/90649342/133147892-b82cae44-4927-4060-99cf-8223246121de.png)


# Step 7: run some queries of your own!

Feel free to play around with different queries and explore the API.

For more information about what's possible in Santiment, see the following link:
https://github.com/santiment/sanpy#retrieving-data-from-the-api

