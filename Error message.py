def valid_input(inp):
    try:
        ret=int(inp)
        if not 0<ret<1000:
            print ("Invalid input!! Try Again")
            return None
        return ret
    except:
        print ("Invalid input!! Try Again")
        return None
        
        
while True:
  validinp = valid_input(input('pick a number between 1 and 999')
	if validinp:break
