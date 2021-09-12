
names_list = ["malki", "sari", "riki", "racheli", "lea", "miri"]
file_name = input("Please enter file name\n")
f = open(f'{file_name}.txt', "w+")
for n in names_list:
    f.write(n+"\n")
f = open(f'{file_name}.txt', "r")
f_read = f.read()
f_read = f_read.split()
for name in range(len(f_read)):
 if (name+1) % 2 == 0:
  print(f_read[name])

f.close
