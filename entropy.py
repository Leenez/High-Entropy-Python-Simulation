'''Algorithm will create folder "EntropiaData" and store
all the results to this folder. You can just see what it does by running with Pythdon 3.x or check detailed description from  thesis. 

You can find it from here:

https://helda.helsinki.fi/bitstream/handle/10138/229535/KorkEntTerm.pdf?sequence=2

or

https://helda.helsinki.fi/handle/10138/229535
'''

# -*- coding: utf-8 -*
import random, math, os, sys
from operator import itemgetter

namespace = globals()
Kb = 1.38064852 * (10 ** -23)

try:
 if (os.path.isdir('EntropiaData') != True):
  os.mkdir('EntropiaData')
 le = open('EntropiaData\\Tulosdata.asc', 'w')
 le.write('L ' + 'Nmaara ' + 'Entropia ' + 'Virhe')
 le.close()
except:
 print('\nCant create file or folder')
 sys.exit()

NmaaraTable = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
Ltable = [2,3,4,10,60]

for Nm in NmaaraTable:
 Nmaara = Nm
 for Llen in Ltable:
  L = Llen
  Ntot = L ** 3
  N0maara = []
  Stable = []
  toistoMaara = 100 * Ntot
  for statistics in range(0,toistoMaara):
   MaxN = Ntot
   for i in range(0, Nmaara - 1):
    namespace['N%d' % i] = random.randint(0,MaxN)
    MaxN = MaxN - namespace['N%d' % i]
   Tmp1 = Nmaara-1
   namespace['N%d' % Tmp1] = MaxN
   LogPermutations = Ntot * math.log(Ntot)
   for i in range(0,Nmaara):
    if (namespace['N%d'%i] > 0):
     LogPermutations = LogPermutations - (namespace['N%d'%i] * math.log(namespace['N%d'%i]))
   S = Kb * LogPermutations
   N0maara.append(N0)
   Stable.append(S)

  isoTable=[]
  for i in range(0, toistoMaara):
   tupleTable = [N0maara[i], Stable[i]]
   isoTable.append(tupleTable)
  isoTable.sort(key=itemgetter(0))
  leNimi='EntropiaData/L%dNm%dP.asc' % (L, Nmaara)
  le = open(leNimi,'w')
  Ssumma = 0
  Slaskuri = 0
  isoTable.append([-1, 0])

  for i in range(0, toistoMaara):
   tmp1 = isoTable[i]
   tmp2 = isoTable[i+1]
   Ssumma = Ssumma + tmp1[1]
   Slaskuri += 1
   if(tmp1[0] != tmp2[0]):
    le.write(str(tmp1[0]) + ' ' + str(Ssumma/(Slaskuri)) + '\n')
  Ssumma = 0
  Slaskuri = 0
  le.close()
  Savg = sum(Stable)/(len(Stable))
  Serror = 0
  for S in Stable:
   Serror = Serror + ((S - Savg) ** 2)
   Serror = math.sqrt(Serror/ (len(Stable) - 1))
   Serror = Serror / math.sqrt( (len(Stable)))
  leNimi = 'EntropiaData/TulosData.asc'
  le = open(leNimi,'a')
  le.write('\n' + str(L) + ' ' + str(Nmaara) + ' ' + str(Savg) + ' ' + str(100*(Serror/Savg)))
  le.close()