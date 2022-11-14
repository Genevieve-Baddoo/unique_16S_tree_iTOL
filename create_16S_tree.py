'''
How to create a phylogenetic tree in iTOL from project fasta file

STEP 1: Read in unique_16S_db_align.fasta file to start (contains 292 sequences). Parse sequence headers from fasta file. Starts with ">" 

STEP 2: To pull out all Genera, pull out the first word, which is the Genus (seperated by '_') 

STEP 3: Read in all_genera.txt as a list (check to see how many items in list to make sure it's 292) 

STEP 4: Find how many unique genera there are 

note: will color phylgenetic tree by Order instead of Genus (Order>Family>Genus>Species) to get reasonable amount of colors (19 Orders=19 colors)

STEP 5: Create look up table (dictionary) with the key as the scientific name and the Order as the value

STEP 6: Create file to upload to iTOL
'''

#STEP 1: read in unique_16S_db_align.fasta file. Parse out headers from fasta file.
from Bio import SeqIO #use biopython to parse out headers in unique_16S_align.fasta file


with open('/Users/genevievebaddoo/Downloads/unique_16S_db_align.fasta') as handle: #open fasta file
    for record in SeqIO.parse(handle, "fasta"):
        print(record.id, file=open('headers_genera.txt', 'a')) #print to a new txt file


#STEP 2: pull out genera by pulling out the first word
with open('headers_genera.txt', 'r') as f: 
    for line in f:
        print(line.split('_')[0], file=open('all_genera.txt', 'a'))      
            
        
#STEP 3: read in all_genera.txt as a list (check to make sure there are 292 items in list)
 with open('all_genera.txt') as file:
    all_genera = file.read().splitlines() 
    elements = len(all_genera)
    print(elements) #just to check how many items in list. There are 292 items in all_genera list!       

#STEP 4: find how many unique genera there are     
def unique (all_genera):
    #insert list to set
    list_set = set(all_genera) #a set is like a dictionary but it HAS NO DUPLICATES
pwd
#convert set to list
    unique_list = (list(list_set))
    x = unique_list.sort() #puts list in alphabetical order
    for x in unique_list:
        print(x + ' OR ', end='') #adds OR in between each item in list to be put into NCBI>Taxonomy search bar. Display settings drop down menu>Info. Items per page 100
    return len(unique_list)

unique(all_genera) #call function to get unique genera  

x = unique(all_genera) #return the number of items in function 

print(x) #61

#STEP 5: create lookup table (dictionary) after reading in csv file I made (16s_genus_to_order.csv).
'''
Copy and paste below into Taxonomy Search Bar in NCBI Taxonomy database

Acinetobacter OR Actinomyces OR Actinotignum OR Aerococcus OR Alloscardovia OR Anaerococcus OR Bacillus OR Bifidobacterium OR Brachybacterium OR Brevibacterium OR Campylobacter OR Citrobacter OR
Corynebacterium OR Curtobacterium OR Cutibacterium OR Dermabacter OR Dermacoccus OR Dolosicoccus OR Enterobacter OR Enterococcus OR Escherichia OR Facklamia OR Falseniella OR Finegoldia OR Fusobacterium OR
Gardnerella OR Gemella OR Gleimia OR Globicatella OR Gordonia OR Granulicatella OR Haemophilus OR Klebsiella OR Kocuria OR Kytococcus OR Lacticaseibacillus OR Lactobacillus OR Limosilactobacillus OR Microbacterium OR
Micrococcus OR Moraxella OR Morganella OR Neisseria OR Nosocomiicoccus OR Oligella OR Paenibacillus OR Pantoea OR Prevotella OR Priestia OR Proteus OR Pseudoclavibacter OR Pseudoglutamicibacter OR Pseudomonas OR Rothia OR
Schaalia OR Shigella OR Sphingomonas OR Staphylococcus OR Streptococcus OR Trueperella OR Varibaculum

Returns 67 Scientific names. Copy each Genus as plain text into excel doc(save as a .csv file). Under display settings, click Info and then Apply. Hover over mouse to Order. Copy as plain text and paste next to Scientific name
'''
#1st column in csv file is keys k (Scientific Name) and 2nd column is the values v (Order)

import csv #read in csv file

reader = csv.reader(open('/Users/genevievebaddoo/16s_genus_to_order.csv', 'r')) #read in excel file I made

order_dict = {} #create dict
for row in reader: #loop through rows in csv file
    k, v = row #rows are keys followed by values
    order_dict[k] = v

#create list of just the values (Orders)
list_values = set(order_dict.values()) #choose set to see see how many Orders there are (in sets there are no duplicates)
print(len(list_values)) #19=the number of values (which are the Orders). That will determine the amount of colors I need


#pick color scheme with 19 colors. Create a list
#googled sequence of 20 hex colors. Pasted color codes into script and created a list [] called colors
colors = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0', '#f032e6', '#bcf60c', '#fabebe', '#008080', '#e6beff', '#9a6324', '#fffac8', '#800000', '#aaffc3', '#808000', '#ffd8b1', '#000075', '#808080', '#ffffff', '#000000']

color_dict = {} #create a dictionary for the hex colors so I can assign hex colors to each value (Order)
j=0 #initialize colors 
for value in list_values: #loop through list of values (Orders) 
    color_dict[value] = colors[j] #value (Order) in color dictionary is equal to a hex color (assigns hex color to each value(Order))
    j += 1 #add the next hex color

headers_file = open('/Users/genevievebaddoo/headers_genera.txt') #open the txt file that has the headers w/ the genus and species (created in STEP 1)
headers = headers_file.readlines() #read lines in file


for i in color_dict: #loop through hex colors in the color dictionary
    print(i, color_dict[i]) #prints out the 19 orders (i), and the hex color). THIS is the output that is pasted into the itol_file.txt



#STEP 6: Create file to upload to iTOL
#I created another file called itol_file.txt. I used this file to copy and paste content into tol_color_strip_source.txt. Save.

itol = open('Users/genevievebaddoo/itol_file.txt' ,'w') #has fasta headers, hex number, and bacterial Order. 


for line in headers: #loop through headers_file
    z=line.split('_')[0] #create a variable (z) for the genus. Split lines of file by _ to get the Genus key to Order_dict 
    zz=order_dict[z] #create a variable (zz) for the Order names w/ key as the Genus (z variable)
    c=color_dict[zz] #create variable for hex colors w/ key as the Order (zz variable)
    itol.write(line.rstrip()+' '+c+' '+zz+'\n') #write to itol_file the fasta header, the hex color (c), and the bacterial Order (zz)
itol.close() #always close file

#tol_color_strip_source.txt is the file used to upload to iTOL (has format for iTOL. Delete everything under #ID2 value2 from raw file and paste output from itol_file.txt into this file. Save.

#UPLOAD tol_color_strip_source.txt into Datasets tab on iTOL (upload annotated dataset)
