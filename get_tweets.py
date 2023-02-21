import re
import pandas as pd

def username_extract(filename, column_name):
    tweet_dict = {}
    username_list =[]

    #convert to dataframe
    df = pd.read_csv(filename)


    for i in range(len(df)):
        #deal with only tweet column
        tweet = df.loc[i, column_name]
        res = re.search('@\w+:', tweet)
        if (res != None):
            username_list.append(res.group())

    for i in range(len(username_list)):
            tweet_dict[username_list[i]] = []

    for i in range(len(df)):
            tweet = df.loc[i, "tweet"]
            res = re.search('@\w+:', tweet)
            if (res != None): 
                tweet_extract = tweet.split(res.group())
                tweet_dict[res.group()].append(tweet_extract[1])
    return tweet_dict

username_extract("data.csv", "tweet")
#username_extract("final_dataset.csv", "Tweets")