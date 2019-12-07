'''
Tokens-

Consumer API keys--
OKsluTUxSq1rD1LPY42iop5by (API key)
WR0JuTYsHIlcryp9riiL4LaWEb2AFXbUIX1zow2AMq7RtTbOc4 (API secret key)

Personal Access Tokens--
1183159972122677250-b9OjHmG4C0pN6BeO9Nbj6qDJgTkcnk (Access token)
OJYJtq9ZbUfoDaRaCKOWNu0EezZztCbDFei938TRPVaC6 (Access token secret)
Read and write (Access level)
'''
import twitter
import itertools

# Using opensource python wrapper for Twitter-API called "python-twitter


### Twitter-Authentication ###
def authenticator():
	consumer_token = 'OKsluTUxSq1rD1LPY42iop5by'
	consumer_secret_token = 'WR0JuTYsHIlcryp9riiL4LaWEb2AFXbUIX1zow2AMq7RtTbOc4'
	access_token = '1183159972122677250-b9OjHmG4C0pN6BeO9Nbj6qDJgTkcnk'
	secret_access_token = 'OJYJtq9ZbUfoDaRaCKOWNu0EezZztCbDFei938TRPVaC6'
	api = twitter.Api(consumer_key=consumer_token,
				consumer_secret=consumer_secret_token,
				access_token_key = access_token,
				access_token_secret = secret_access_token)
	return(api)
	
	
### New Tweet ###
def tweet(message):
	api = authenticator()
	post_update = api.PostUpdates(status=message)
	return(post_update)

### Rerieve/Get Tweets ###
def retrieve_tweets(user):
	'''
		user is name of account in twitter generally with @ reference which is called 'screen_name' in Twitter api
	'''
	api = authenticator()
	update = api.GetUserTimeline(screen_name=user)
	return(update)

### Delete Tweet ###
def delete_tweet(tweet_id):
	'''
		delete tweet by tweet_id
	'''
	api = authenticator()
	deleted = api.DestroyStatus(status_id=tweet_id)
	return deleted
	
### Pagination ###
def paginate(iterable, page_size):
    while True:
        i1, i2 = itertools.tee(iterable)
        iterable, page = (itertools.islice(i1, page_size, None),
                list(itertools.islice(i2, page_size)))
        if len(page) == 0:
            break
        yield page	

#print(tweet('Hello World2!'))
'''
api = authenticator()

New Tweet

#tweet('Third Tweet : Don''t know what I am doing.')


Retrieve All Tweets by userid

def paginate(iterable, page_size):
    while True:
        i1, i2 = itertools.tee(iterable)
        iterable, page = (itertools.islice(i1, page_size, None),
                list(itertools.islice(i2, page_size)))
        if len(page) == 0:
            break
        yield page
       
timeline = retrieve_tweets('ChinmayVadgama')
statusids = []
for i in paginate(timeline, 50):
    for twet in i:
        print(twet.id)
        statusids.append(twet.id)
    print(i)



#Delete the tweet by its id
#Lets delete first tweet from above list

deleted = delete_tweet(statusids[0])
print(deleted)


new_message = 'Hello There!'
post_message = api.PostDirectMessage(screen_name='GAMARAYBURST1',text=new_message)
print(post_message)

api.PostDirectMessage(user, text)
api.GetUser(user)
api.GetReplies()
api.GetUserTimeline(user)
api.GetHomeTimeline()
api.GetStatus(status_id)
api.GetStatuses(status_ids)
api.DestroyStatus(status_id)
api.GetFriends(user)
api.GetFollowers()
api.GetFeatured()
api.GetDirectMessages()
api.GetSentDirectMessages()
api.PostDirectMessage(user, text)
api.DestroyDirectMessage(message_id)
api.DestroyFriendship(user)
api.CreateFriendship(user)
api.LookupFriendship(user)
api.VerifyCredentials()
'''
