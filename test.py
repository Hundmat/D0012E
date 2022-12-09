def stopwatch():
  start = int(input())
  times=[]
  on_off= False
  time=0
  for i in range(0,start):
    times+=[int(input())]
    
  for i in range(0,start):
    try:
      if on_off:
        time+=times[i]-times[i-1]
      on_off=not on_off
    except:
      on_off=not on_off
  if not on_off:
    print (time)
  else:
    print ("still running")
stopwatch()