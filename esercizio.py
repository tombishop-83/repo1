def check_name(n_1, n_2):
 return n_1 == n_2
'''
	str, str --> bool 
	
	Returns True whether the names match
	
	examples:
	
	check_name(marco, elena) 
	>>> False
	
	check_name(silvia, silvia)
	>>> True


'''
 
def _extract(tweet,delimiter):
 name = ''
 num_follw = ''
 p_1 = tweet.find(delimiter,0,len(tweet))
 p_2 = tweet.find(delimiter,p_1,len(tweet))
 for ch in tweet[p_1:p_2]:
  if ch != delimiter:
   name = name + ch
 for ch in tweet[p_2:]:
  if ch != delimiter:
   num_follw = num_follw + ch
  
  return int(num_follw), name
   
'''
	str --> str, str
	
	Retrieves the user name and the number of followers. Takes 
	two parameters as input, a tweet, and the delimiter character.
	
	MECHANISM
	
	Finds the first position at which the delimiter occurs. Starting
	there it retrieves the name. 

'''
