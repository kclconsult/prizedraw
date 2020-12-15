import yfinance as yf
import random, time, sys

if(len(sys.argv) < 2): 
    print("Upper bound required.");
    sys.exit();

data = yf.download("DJIA", start="2020-12-14", end="2020-12-15")
random.seed(data["Close"].values[0])

upper=int(sys.argv[1]);
sleep_time=0.01;
iteration=0;

while(iteration<250):
   print(random.randint(1, upper));
   if(iteration>200): sleep_time+=0.01;
   iteration+=1;
   time.sleep(sleep_time);

print("The winner is... " + str(random.randint(1, upper)) + "!");
