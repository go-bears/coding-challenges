import json

from tinydb import TinyDB, Query # required module, install with: pip install tinydb

DB = TinyDB('db.json')

FILEPATH = 'contacts.json'


# only run once to load and initialize DB with contacts.json; 
# else DB will have duplicate entries
def load_DB(FILEPATH):
    """
    Loads TinyDB with json data, normalizes email and name for db input,
    returns searchable db

    """

    with open(FILEPATH, 'r') as fn:    
        data = json.load(fn)

        for element in data:
            element = OrderedDict(element)

            for key, value in element.items():
                
                try:
                    element['name'] = element['name'].lower().strip()
                    element['email'] = element['email'].lower().strip()
                    
                except:
                    # exception for non-ascii characters in sam smith email entry
                    pass
            
            DB.insert(element)


def input_search():
    """Takes in command line input, normalizes input, returns search_term"""

    search_term  = raw_input('Please enter your search term: ').lower()

    while len(search_term) < 1:
        print 'Your input was empty. Try again'
        
        search_term  = raw_input('Please enter your search term: ')
        
    return search_term


def search_DB(DB, search_term):
    """
    Takes in search_term, queries db, and returns JSON encoded search results .
    
    Displays relevant results ranked by name, email, number
    """

    User = Query()
    results = []

    # search performs regex search on DB; adds matches to results
    if DB.search(User.name.search('%s+' % search_term)):
        searched_name = DB.search(User.name.search('%s+' % search_term))
        
        if searched_name not in results:
            results.extend(searched_name)     

    if DB.search(User.email.search('%s+' % search_term)):
        searched_email = DB.search(User.email.search('%s+' % search_term))
        
        if searched_email not in results:
            results.extend(searched_email)

    if DB.search(User.phone.search('%s+' % search_term)):
        searched_num = DB.search(User.phone.search('%s+' % search_term))
        
        if searched_num not in results:
            results.extend(searched_num)


    if len(results) < 1:
        print "Sorry, search term not found"       


    print json.dumps(results, indent=4, sort_keys=True, 
                     separators=(',',':')
                     )
    return results

def main():
    """
    Main logic control for application
    """

    search_term = input_search()
    # DB=load_DB(FILEPATH) # only need to run once
    search_DB(DB, search_term)

if __name__ == '__main__':
    main()
    

###########-----Tests----#############################
    import doctest

    """
        >>> search_DB(DB, 'zz')
    [
        {
            "email":"zz@zed.com",
            "name":"zed",
            "phone":"111.111.4444"
        }
    ]

    >>> search_DB(DB, '@yahoo')
    [
        {
            "email":"jj@yahoo.com",
            "name":"Jenny J"
        }
    ]
    """

    if doctest.testmod().failed == 0:
        print "\n*** All doctest integration tests passed!\n"