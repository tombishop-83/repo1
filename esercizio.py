'''
Sample data

Mar 24 18:14:01 marco kernel: [10782.956702] usb 3-1.1.1: Manufacturer: Microsoft
Mar 24 18:14:01 marco kernel: [10782.956873] usb 3-1.1.1: configuration #1 chosen from 1 choice
Mar 24 18:14:01 marco kernel: [10782.973298] input: Microsoft Basic Optical Mouse as /devices/pci0000:00/0000:00:1d.1/usb3/3-1/3-1.1/3-1.1.1/3-1.1.1:1.0/input/input10
Mar 24 18:14:01 marco kernel: [10782.974880] generic-usb 0003:045E:0084.0003: input,hidraw0: USB HID v1.10 Mouse [Microsoft Basic Optical Mouse] on usb-0000:00:1d.1-1.1.1/input0
Mar 24 18:29:37 marco kernel: [11718.849291] usb 3-1.1.4: new full speed USB device using uhci_hcd and address 8
Mar 24 18:29:37 marco kernel: [11718.951275] usb 3-1.1.4: not running at top speed; connect to a high speed hub
Mar 24 18:29:37 marco kernel: [11718.979271] usb 3-1.1.4: New USB device found, idVendor=0fca, idProduct=8004
Mar 24 18:29:37 marco kernel: [11718.979276] usb 3-1.1.4: New USB device strings: Mfr=1, Product=5, SerialNumber=3
Mar 24 18:29:37 marco kernel: [11718.979281] usb 3-1.1.4: Product: RIM Composite Device

'''


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
