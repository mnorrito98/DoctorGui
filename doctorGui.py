"""
Program doctorGui.py
'GUI BASED VERSION OF THE NONDIRECTIVE PSCYCOTHERAPY DOCTOR PROGRAM FROM CHP 5'

MIKE NORRITO

"""

from breezypythongui import EasyFrame
import random

#Global variables and constants 

goOn = ("Please tell me more.", "Many of my patients tell me the same thing.", "Please go on.", "I'm listening", "Oh I see, please continue...")
qualifiers = ("Why do you say that ", "You seem to think that ", "Can you explain why ")

replacements = {"I":"you", "me":"you", "my":"your","we":"you","us":"you","mine":"yours", "am":"are", "you":"I"}

class DoctorGUI(EasyFrame):
	""" def init"""
	def __init__(self):
		EasyFrame.__init__(self, title = "Hello MY Patient", width= 345, height = 234)
		self.addLabel(text = "Good Morning. I hope you are well today.", row = 0, column = 0, sticky = "NEWS")
		self.addLabel(text = "What can I do for you?", row = 1, column = 0, sticky = "NEWS")
		self.userText = self.addTextField(text = "", row = 2, column = 0, sticky = "NEWS")
		#Bind the user text field to the enter key also 
		self.userText.bind("<Return>", lambda event: self.reply())
		self.responseLabel = self.addLabel(text = "", row = 3, column = 0, sticky = "NEWS")
		self.addButton(text = "Submit", row = 4, column = 0, command = self.reply)

	def reply(self):
		sentence = self.userText.getText()
		probzbility = random.randint(1, 4)
		if probzbility == 1: 
			self.responseLabel["text"] = random.choice(goOn)
		else:
			self.responseLabel["text"] = random.choice(qualifiers) + changePerson(sentence)
		if self.userText.getText() == "hello":
			self.responseLabel["text"] = "Hello there how can I help you today?"

def changePerson(sentence):
	"""Replaces first person pronouns with second person pronouns ."""
	words = sentence.split()
	replyWords = []
	#Loop through the lsit of thw words the user gave
	for word in words:
		replyWords.append(replacements.get(word, word))
	return " ".join(replyWords)


def main():
	DoctorGUI().mainloop()
main()