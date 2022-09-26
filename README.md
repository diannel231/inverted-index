# inverted-index
## buildIndex()
Implemented in two parts because direct converson to inverted indes was having issues
First creates token dictionary and builds a dictionary of docID value as key and token dictionary as value
Iterates through that list and add them to an inverted index to create the working list
## and_query function()
The and merge function first checks the edge cases where 0 query terms are used, giving a warning that a query term is needed, and 1 query term where the posting list is returned as normal for the single term. The function first grabs the posting list for the first query term and then loops through the rest of the query terms, finding the intersections in the posting list values and keeping the result. The total time is posted after the final result is formed.
## getPostingListForTerm()
Loops through the document list and add the docId to list 
## intersect()
Takes two posting lists and returns a list of values that are contained in both posting lists by incrementing through each value
## post_process_results()
Takes the resulting posting list and prints it with the option to include the positions of the search terms in each document
## print_dict()
Iterate through the words and posting list in inverted index then print
## print_doc_list()
Iterate through docID dictionary and print index, which is the docId and file name that is stored as key of the dictionary
