# inverted-index
The and merge function first checks the edge cases where 0 query terms are used, giving a warning that a query term is needed, and 1 query term where the posting list is returned as normal for the single term. The function first grabs the posting list for the first query term and then loops through the rest of the query terms, finding the intersections in the posting list values and keeping the result. The total time is posted after the final result is formed.
