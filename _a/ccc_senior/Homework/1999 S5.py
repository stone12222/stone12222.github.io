from itertools import permutations
import cProfile

def doing_thing(dict,w):
  ww=len(w)
  num=0
  for i in w:
      num+=dict[i]*10**ww
      ww-=1
  return num

def main_program():
  n = int(1)
  for i in range(n):
      a = 'SEND'
      b = 'MORE'
      c = 'MONEY'
      s = set()
      s.update(a)
      s.update(b)
      s.update(c)
      s = list(s)
      dicts={}

      for i in s:
          dicts[i]=0
      b_start=s.index(b[0])
      a_start=s.index(a[0])

      for p in permutations(range(0, 10), len(s)):
          if p[a_start]!=0 and p[b_start]!=0:
              for n in range(len(dicts)):
                  dicts[s[n]]=p[n]
              an = doing_thing(dicts, a)
              bn = doing_thing(dicts,b)
              cn = doing_thing(dicts,c)
              if an + bn == cn:
                  print(an)
                  print(bn)
                  print(cn)
                  # break
cProfile.run('main_program()')