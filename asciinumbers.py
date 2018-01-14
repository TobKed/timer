
n0="""\0
 ██████╗ \0
██╔═████╗\0
██║██╔██║\0
████╔╝██║\0
╚██████╔╝\0
 ╚═════╝ \0
"""

n1="""\0
 ██╗\0
███║\0
╚██║\0
 ██║\0
 ██║\0
 ╚═╝\0
"""
 
n2="""\0
██████╗ \0
╚════██╗\0
 █████╔╝\0
██╔═══╝ \0
███████╗\0
╚══════╝\0
"""
 
n3="""\0
██████╗ \0
╚════██╗\0
 █████╔╝\0
 ╚═══██╗\0
██████╔╝\0
╚═════╝ \0
"""
 
n4="""\0
██╗  ██╗\0
██║  ██║\0
███████║\0
╚════██║\0
     ██║\0
     ╚═╝\0
"""
 
n5="""\0
███████╗\0
██╔════╝\0
███████╗\0
╚════██║\0
███████║\0
╚══════╝\0
"""
 
n6="""\0
 ██████╗ \0
██╔════╝ \0
███████╗ \0
██╔═══██╗\0
╚██████╔╝\0
 ╚═════╝ \0
"""
 
n7="""\0
███████╗\0
╚════██║\0
    ██╔╝\0
   ██╔╝ \0
   ██║  \0
   ╚═╝  \0
"""
 
n8="""\0
 █████╗ \0
██╔══██╗\0
╚█████╔╝\0
██╔══██╗\0
╚█████╔╝\0
 ╚════╝ \0
"""
 
n9="""\0
 █████╗ \0
██╔══██╗\0
╚██████║\0
 ╚═══██║\0
 █████╔╝\0
 ╚════╝ \0
"""

n_colon="""\0
   \0
██╗\0
╚═╝\0
██╗\0
╚═╝\0
   \0
"""

n_space="""\0
   \0
   \0
   \0
   \0
   \0
   \0
"""
 
num_list_raw = [n0, n1, n2, n3, n4, n5, n6, n7, n8, n9, n_colon, n_space]
num_list = []
for number in num_list_raw:
    num_list.append(number.splitlines())

num_sliced={'0':num_list[0],
          '1':num_list[1],
          '2':num_list[2],
          '3':num_list[3],
          '4':num_list[4],
          '5':num_list[5],
          '6':num_list[6],
          '7':num_list[7],
          '8':num_list[8],
          '9':num_list[9],
          ':':num_list[10],
          ' ':num_list[11]}

def print_ASCII(str):
    print_dict=[]
    for x in range(len(num_sliced['1'])+1):   # number or rows based on number 1
        print_dict.append([])
    for c in str:
        if c in num_sliced.keys():
            row = 0
            for line in num_sliced[c]:
                print_dict[row].append(line)
                row+=1
    for row in print_dict:
        row = "".join(row)
        print (row)     

