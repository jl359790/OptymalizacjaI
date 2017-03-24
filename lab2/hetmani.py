"""
 działa dla n od 3 do 26 włącznie (więcej może być problem bo zabrakło literek)
	reprezentacja w wynikowym kodzie
	  _______________   
	8|_|_|_|_|_|_|_|_|
	7|_|_|_|_|_|_|_|_|
	6|_|_|_|_|_|_|_|_|
	5|_|_|_|_|_|_|_|_|
	4|_|_|_|_|_|_|_|_|
	3|_|_|_|_|_|_|_|_|
	2|_|_|_|_|_|_|_|_|
	1|_|_|_|_|_|_|_|_|
	  a b c d e f g h
	  
	reprezentacja w pythonie
	  _______________
	8|_|_|_|_|_|_|_|_|
	7|_|_|_|_|_|_|_|_|
	6|_|_|_|_|_|_|_|_|
	5|_|_|_|_|_|_|_|_|
	4|_|_|_|_|_|_|_|_|
	3|_|_|_|_|_|_|_|_|
	2|_|_|_|_|_|_|_|_|
	1|_|_|_|_|_|_|_|_|
	  1 2 3 4 5 6 7 8
"""

def columnLetter(i):
    firstLetter = ord('a')
    return chr(firstLetter + i - 1)

def generateProblem(n):
    print "Maximize "
    f = True
    for i in range(1, n+1):
        for j in range(1, n+1):
            if f:
                f = False
            else:
                print '+',
            print columnLetter(i) + str(j),
    return

def hetmanInColumn(columnNumber, n):
    f = True
    for i in range(1, n+1):
        if f:
            f = False
        else:
            print '+',
        print columnLetter(columnNumber) + str(i),
    print("<= 1")
    return

def hetmanInRow(rowNumber, n):
    f = True
    for i in range(1, n+1):
        if f:
            f = False
        else:
            print '+',
        print columnLetter(i) + str(rowNumber),
    print("<= 1")
    return

def hetmanRows(n):
	for i in range(1, n+1):
		hetmanInRow(i, n)
	return
	
def hetmanColumns(n):
    for i in range(1, n+1):
        hetmanInColumn(i, n)
    return
	
def hetmanBackslashes(n):

	"""
	Wypiszemy "bicia" hetmanów po ukosie z prawego-dolnego rogu w lewy-górny zaczynając od "przekątnej" a1, potem a2 - b1, itd.
	Zamysł:
	Niech i oznacza nr kolumny, a j nr wiersza wg schematu podanego na początku.
	"Przekątne" identyfikujemy za pomocą sumy i + j = l, gdzie l przebiega od 2 do n+1 (normalnie do n, ale uwzględniamy od razu "główną przekątną")
	i oraz j przebiega od 1 do l-1.
	Z sumy mamy i = l - j, a stąd poniższy kod
	"""

	for l in range(2, n+2):
		f = True
		for j in range(1,l):
			if f:
				f = False
			else:
				print '+',
			print columnLetter(l-j) + str(j),
		print("<= 1")
		
	"""
		Po wypisaniu "głównej przekątnej" musimy troszkę zmodyfikować metodę:
		i + j = n + l, gdzie l przebiega od 2 do n-1, j od l do n i wyliczamy i
	"""
		
	for l in range(2, n+1):
		f = True
		for j in range(l, n+1):
			if f:
				f = False
			else:
				print '+',
			print columnLetter(n + l - j) + str(j),
		print("<= 1")
	return

def hetmanSlashes(n):

	"""
	Teraz mamy do czynienia z "przekątnymi" z lewego-dolnego rogu w prawy-górny zaczynając od a4.
	Trzeba lekko zmodyfikować warunek na i oraz j:
	i + n - j = l do "głównej przekątnej"
	oraz
	n - i + j = l poniżej
	"""
	
	for l in range(1,n+1):
		f = True
		for i in range(1,l+1):
			if f:
				f = False
			else:
				print '+',
			print columnLetter(i) + str(i + n - l),
		print("<= 1")
		
	for l in range(n-1, 0, -1):
		f = True
		for j in range(1, l+1):
			if f:
				f = False
			else:
				print '+',
			print columnLetter(n + j - l) + str(j),
		print("<= 1")
	return
	
def subjectTo(n):
    print("\nSubject To\n")
    hetmanRows(n)
    print("\n")
    hetmanColumns(n)
    print("\n")
    hetmanBackslashes(n)
    print("\n")
    hetmanSlashes(n)
	
    return

def generals(n):
    print("\nGenerals\n")
    for i in range(1, n+1):
        for j in range(1, n+1):
            print columnLetter(i) + str(j)
    return
	
def bounds(n):
    print("\nBounds\n")
    for i in range(1, n+1):
        for j in range(1, n+1):
            print("0 <="),
            print columnLetter(i) + str(j),
            print("<= 1")
    return

def run(n):
	generateProblem(n)
	subjectTo(n)
	bounds(n)
	generals(n)
	return
	
n = 4
run(n)
print("\nEnd")
