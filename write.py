from datetime import datetime

with open("log.txt","a")as log:
	log.write(f"[{datetime.now()}] - User logged in \n")

with open("open.txt","w") as f:
	f.write("\n New line addedd")



with open("open.txt","a")as f:
	f.write("\n This line was appended")
