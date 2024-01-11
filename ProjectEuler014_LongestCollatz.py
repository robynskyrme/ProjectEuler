# 23.2.2023
# Project Euler 14: Longest Collatz sequence below 1,000,000


def collatz_seq_count(n):
   seq = 1
   while n > 1:
       if n%2 == 0:
           n = n/2
       else:
           n = n*3+1
       seq = seq + 1


   return seq


def collatz_seq_print(n):
   seqstring = ""
   seq = 1
   first = True
   if n == 1:
       seqstring = seqstring + "1"
   while n > 1:
       if not first:
           seqstring = seqstring + " → "
       else:
           first = False
       seqstring = seqstring + str(int(n))
       if n%2 == 0:
           n = n/2
       else:
           n = n*3+1
       seq = seq + 1


   seqstring = seqstring + " → 1  [" + str(seq) + " steps]"




   #seqstring = seqstring + "1"
   return seqstring


def find_longest(m):
   # Seed for the longest
   longest_seed = 1
   longest = 0
   for c in range(m):
       check = collatz_seq_count(c)
       #print(c)
       # print(check)
       if check > longest:
           longest = check
           longest_seed = c
           print ("NEW RECORD: " + str(c))


   return longest_seed


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   j = int(input("Below: "))
   largest = find_longest(j)
   print("\nLongest sequence below " + str(j) + " starts with " + str(largest) + ":")
   print(collatz_seq_print(largest))
