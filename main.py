import re

class Recipe:
	"""docstring for Recipe
	   object = Recipe(filename)
	   __init__ will change all the numbers in front of tokens to whole fractions and assign to original_txt
	   printshit() for testing
	   get_newrecipe(portion) will adjust the numbers to n*portion
	   convertfrac(matchobj) will change numbers to fractions

	   example: 	recipeobject = Recipe("chicken.txt") <<< chicken.txt == "1 pounds of chicken, 2 1/2 tsp of salt"
	   				recipeobject.get_newrecipe(3)
	   				>>>"3 pounds of chicken, 15/2 tsp of salt"
	"""

	tokens = ['cup', 'cups', 'tbsp', 'tsp', 'lb', 'pounds', 'pound', 'lbs']
	token_pattern = "(?:" +"|".join(tokens) + ")"
	pattern = "(?:[0-9]+\/[0-9]+|[0-9]+)\s*((?:" + "|".join(tokens) + "))"
	#pattern = "[0-9]+|(?:[0-9]+\/[0-9]+)\s*" + pattern

	#original text gets formatted to have only fractional numbers in front of ingredients
	def __init__(self, txtrecipe):
		with open(txtrecipe, 'r') as f:
			self.original_txt = re.sub("([0-9]+)\s([0-9]+)\/([0-9])", self.convertfrac, f.read())
			self.original_txt = re.sub("(?<=\n)([0-9]+)" + "(?=\s(?:" +"|".join(self.tokens) + "))", r"\1/1" , self.original_txt)

	def printshit(self):
		print(999999999999999)
		print(self.original_txt)
	
	def get_newrecipe(self, portion):
		if type(portion) != float:
			print("portion has to be a float")
			return None
		# lowercased, divided by new line
		lines = self.original_txt.lower().split("\n") 
		for i, line in enumerate(lines):
			lines[i] = re.sub("([0-9]+)/([0-9]+)\s+" + "(?=" + self.token_pattern + ")", lambda x: "{:.2f}".format(float(x.group(1))*portion) + "/" + x.group(2) +" ", line)

		return "\n".join(lines)

	def convertfrac(self, matchobj):
		newgroups = list(map(int, matchobj.groups()))
		numer = newgroups[0]*newgroups[2] + newgroups[1]
		denom = newgroups[2]
		return str(numer) + "/" + str(denom)

"""
recipeobject = Recipe("chickenrecipe.txt")

with open("Output.txt", "w") as text_file:
    print(recipeobject.get_newrecipe(1/3.), file=text_file)
"""