-----------------------------------------------
	THE DBPEDIA BOOK LOOKUP TOOL 
-----------------------------------------------

NECESSARY PACKAGES!
-----------------------------------

* !pip install tqdm
* !pip install rich

!!!!!!!!!! IMPORTANT: 
THESE ARE JUST PACKAGES TO MAKE THE OUTPUT LOOK FANCY.
IF THE RICH PACKAGE OR THE TQDM PACKAGE CAUSES YOU TROUBLE, PLEASE OPEN ONE OF THESE FILES IN THE ASSIGNMENTS FOLDER:

"INFORMATION_SCIENCE_EXAM_TessDejaeghere_No_Rich_package.ipynb"
OR
"INFORMATION_SCIENCE_EXAM_TessDejaeghere_No_Rich_package.py"

THEY DO THE SAME THING, BUT IN RAW PYTHON.

> run the first code block to import all the necessary modules

APP INFO
----------------------------------

This app lets you search through the DBPedia API book collection.

SCHEMA 
----------------------------------

1) Do you want to perform a key word search or a full title search?

scenario 1: KEY WORD SEARCH

2) Is the book in your list? Yes or no.
! list of options
	2.5) If not: the app will take you back to the start.
	2.6) If it is: the app will let you pick the correct book from the list
3) If available in the api, the app returns:
> the title 
> an image of the book cover (FROM THE OPEN LIBRARY API)
> the book summary (DBPEDIA API)
> the literary genre (DBPEDIA API)
> the date published (DBPEDIA API)
> the isbn code (DBPEDIA API)

metadata on the author:
> the author name (DBPEDIA API)
> author abstract (DBPEDIA API)
> birth name (DBPEDIA API)
> birth date (DBPEDIA API)

4) The app asks you if you want to search for another book.
	4.1) If not: goodbye! 
	4.2) If you do: the program restarts.


scenario 2: TITLE SEARCH 

2) Type in the full title of the book you're after.
3) If available in the api, the app returns:
> the title 
> an image of the book cover (FROM THE OPEN LIBRARY API)
> the book summary (DBPEDIA API)
> the literary genre (DBPEDIA API)
> the date published (DBPEDIA API)
> the isbn code (DBPEDIA API)

metadata on the author:
> the author name (DBPEDIA API)
> author abstract (DBPEDIA API)
> birth name (DBPEDIA API)
> birth date (DBPEDIA API)

4) The app asks you if you want to search for another book.
	4.1) If not: goodbye! 
	4.2) If you do: the program restarts.

! If you enter an invalid book number, the program will restart.
! If you enter anything other than yes or no, the program will restart.


LIMITATIONS!
----------------------------------
Please know that we have a lot of other exam projects which are difficult and time-consuming.
I did everything I could to get a result that worked, but sadly I had to take the time
limitations into account.

> The app will fail if the author name contains extended ASCII. I tried everything,
nothing worked.

> I wrote this program with the link we initially got. This returned an ISBN for about 7/10 books.
Consequently, I was able to fetch an image for a lot of books from the Open Library API.
Sadly, the new link does not return a lot of ISBNs (the info is simply NOT THERE.).
So this app doesn't return a lot of images. If you would like to test this feature, please try the following searches:

		> Harry Potter and the Deathly Hallows
		> Wonderland (novella)
		> ...


