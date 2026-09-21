class Release:
	def __init__(self, name):
		self.name = name

	def printRecords(self):
		print(f"Release name: {self.name}")

class Book(Release):
	def __init__(self, writer, pages, name):
		super().__init__(name)
		self.writer = writer
		self.pages = pages

	def printRecords(self):
		super().printRecords()
		print(f"Writer: {self.writer}\nLength: {self.pages} pages\n")

class Paper(Release):
	def __init__(self, leadEditor, name):
		super().__init__(name)
		self.leadEditor = leadEditor

	def printRecords(self):
		super().printRecords()
		print(f"Lead editor: {self.leadEditor}\n")

releases = []
releases.append(Book("Rosa Liksom", 200, "Hytti n:o 6"))
releases.append(Paper("Aki Hyyppä", "Aku Ankka"))

for r in releases:
	r.printRecords()