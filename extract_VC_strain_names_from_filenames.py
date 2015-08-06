##extracts the strain names from a .txt file called 'MMP_combined_vcf_filenames.txt'
##generated with the shell command: find . -name "VC*.combined.vcf" | sort | uniq > MMP_combined_vcf_filenames.txt
##which is a list of .vcf filenames containing strain names that starts with VC 
##and are < 8 characters long and writes the output to a .txt file called
##list_VCstrains_vcf.txt
##
##The purpose of generating a file containing a list of all the 2007 MMP strains is so that I can use Stephane's 
##perl script (create_gwas_vcf_MMP.pl) to generate a large merged .vcf file for every MMP strain (all 2007). This
##will be useful to test Stephane's new perl script to subset .vcf files for a given list of MMP strains from the 
##large merged .vcf file containing all the strains. It will also be useful to do SKAT on Nigel's MMP data.

##import regular expression library
import re

def extract_strain_names(file_to_read, file_to_write, strain_name_beg):
	''' Saves a file of strain names from a file listing filenames containing strain names. Selects
	only those strain names whose two letter lab designation match the provided two letters.
	Arguments: 
	file_to_read: a file listing filenames containing strain names
	file_to_write: name of file you want to save strain names too
	strain_name_beg: first two letters in strain name (i.e. lab designation)'''
	
	##opens file containing filenames from which to extract strain name
	filenames = open(file_to_read).read().strip().split('\n')
	
	##concatenates two letter lab designation into regular expression search pattern to extract 
	##strain names
	strain_name_pattern = '(' + strain_name_beg + '[0-9]{1,5})'

	##compiles this string as a regular expression search pattern
	pattern = re.compile(strain_name_pattern)
	
	##opens file to save strain names to
	target = open(file_to_write, 'w')
	target.truncate()
	
	##loops through every line in input file
	for val in filenames:
		##finds strain name from line of text
		strains = pattern.search(val)
		##writes strain name to file
		target.write(strains.group(1))
		##writes newline character so there will be a line break after each strain name 
		target.write("\n")
	
	##closes the file that was being written to
	target.close()

##calls extract_strain_names() function and asks for strain names starting with "VC" to be extracted
##from "MMP_combined_vcf_filenames.txt" and saved to "list_VCstrains_vcf.txt"
strain_names = extract_strain_names('MMP_combined_vcf_filenames.txt', 'list_VCstrains_vcf.txt', "VC")
