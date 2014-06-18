symbols = ['GBP', 'USD', 'EUR', 'JPY']
rates = [1,2,3,4]

def conv (value, cfrom,cto):
  answer = value / rates[cfrom]
  answer = answer * rates[cto]
  return (answer)

def ask (direction):
    ans=raw_input("please the conrentce you are converting {0}".format(direction))
    return ans
    
def askv ():
    ans=raw_input("please enter amount {0}".format())
    return ans
    
