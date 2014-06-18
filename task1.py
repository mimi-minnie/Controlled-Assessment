symbols = ['GBP', 'USD', 'EUR', 'JPY']
rates = [1,2,3,4]

def conv (value, cfrom,cto):
  '''
  This function takes a value, and two indexex as inputs - the two indexes (cto and cfrom refer to the currencies being converted to and from.
  
  This function does the conversion between thew two currencies
  
  The output is the converted value
  

  '''
  answer = value / rates[cfrom]
  answer = answer * rates[cto]
  return (answer)

def ask (direction):
  '''
  say what you have to what you are converting to
  '''
    ans=raw_input("please the conrentce you are converting {0}".format(direction))
    return ans
    
def askv ():
  '''
  ask what the amount of money is that you are converting
  '''
    ans=raw_input("please enter amount {0}".format())
    return ans
    
