q_file = open("C://Users//SSS//OneDrive//Documents//SLIC//Python//quotes.txt", "rt")
lines_data = q_file.readlines()
len(lines_data)
lines_data.sort()
for i in range(len(lines_data)):
  print(lines_data[i])
  print(lines_data[i], file=open("quote_1.txt","a"))
q_file.close()
