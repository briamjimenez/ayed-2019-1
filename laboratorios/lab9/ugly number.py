primes = {2, 7, 13, 19}
set (list  = {12})
for i in range(1,n-1):
  set (k = list[0])
  for p in primes:
    insert (p*k) in to list unless (p*k) is in list
  remove list[0] from list
return list[0]
