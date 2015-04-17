#!/usr/bin/env python
# script calculates percentage of available bases for each position in alignment
# sequence needs to be in single line!!
# written by Philipp Resl
# script has not be tested/optimized alot so be careful

import sys

Info = """
Send me an infile!
"""

if len(sys.argv) != 2:
	sys.stderr.write(Info)
	quit()
else:
	FileName = sys.argv[1]
#FileName =  "A_ITS_all_red_mafft_replaced_final.fst" 

TaxonList = []
SequenceList = []

File = open(FileName, "U")

for Line in File:
	if Line[0] == ">":
		TaxonList.append(Line)
	else:
		SequenceList.append(Line)

MaxSeq = len(TaxonList)
Percent = [0.0]*len(SequenceList[1])
#print SequenceList
print TaxonList
for Sequence in SequenceList:
	Sequence.replace("\n", "")
	for i in range(len(Sequence)):
		if Sequence[i] is "A" or Sequence[i] is "a": Percent[i] += 1
		if Sequence[i] is "C" or Sequence[i] is "c": Percent[i] += 1
		if Sequence[i] is "G" or Sequence[i] is "g": Percent[i] += 1
		if Sequence[i] is "T" or Sequence[i] is "t": Percent[i] += 1
		if Sequence[i] is "N" or Sequence[i] is "n": Percent[i] += 1
		if Sequence[i] is "R" or Sequence[i] is "r": Percent[i] += 1
		if Sequence[i] is "Y" or Sequence[i] is "y": Percent[i] += 1
		if Sequence[i] is "M" or Sequence[i] is "m": Percent[i] += 1
		if Sequence[i] is "K" or Sequence[i] is "k": Percent[i] += 1
		if Sequence[i] is "S" or Sequence[i] is "s": Percent[i] += 1
		if Sequence[i] is "W" or Sequence[i] is "w": Percent[i] += 1
		if Sequence[i] is "H" or Sequence[i] is "h": Percent[i] += 1
		if Sequence[i] is "B" or Sequence[i] is "b": Percent[i] += 1
		if Sequence[i] is "V" or Sequence[i] is "v": Percent[i] += 1
		if Sequence[i] is "D" or Sequence[i] is "d": Percent[i] += 1
		

Number = 0
Complete_Nucleotides = 0

for Element in Percent:
	#print Number
	#print Number, Element, ((Element*100)/MaxSeq)
	#Percent[Number] = ((Element*100)/MaxSeq)
	perce = ((Element*100)/MaxSeq)
	Complete_Nucleotides += Element
	#print Number,  " %.2f" % Percent[Number]
	print "%.2f" % perce
	Number += 1
print "Complete Number of Nucleotides in Alignment: %.2f"  % Complete_Nucleotides
print "Total number of positions %.2f" % (len(Percent)*MaxSeq)
print "Alignment is %.2f percent complete " % ((Complete_Nucleotides*100)/(len(Percent)*MaxSeq))

		

File.close()