# CYKParser
Implementation of the CYK Parser for NLP Course.

Note: This program is completed to the specifications of the professor.

Description:
This program will tell the user whether or not a given input string is within
a language, given a context free grammar in chomsky normal form.

Requirements:
	Python 3 (implemented in 3.6)
	Python modules: sys

Instructions for use:
	At command line, run program as follows:
		> python cyk.py cfgfile.txt <input string>
	Wherein <input string> is a sentence in the defined language, with spaces
	between individual "words" (which I defined as terminals).
		Example: for cfg2, a sentence might be "a a b b"

Further Notes:
	1. There is little error checking done for the sake of brevity, and because this is 		implemented within academia, so silly inputs and the like can crash this. That said, with 		reasonable inputs, this program should work to specs.

	2. For the sake of simplicity, I've converted the CFG within Jurafsky & Martin into what I 		believe to be a simpler, more brief version. My converted version is in file cfg1.txt. The 		original CFG, as well as the rules I've used for translation, are in cfg1_untranscribed.txt.
