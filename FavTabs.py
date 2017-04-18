import webbrowser

file = open("Bookmarks.txt")

for line in file:
	webbrowser.open(str(line.strip()))