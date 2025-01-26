from textwrap import dedent


welcome = dedent(
    """
    *****************************
    * Airport Management System *
    *****************************
    """
)

prompt = dedent(
    """
    Choose one of the following options by pressing its number:
    1. List all Boeing planes
    2. Add a new plane
    3. Change incorrect \"Boieng\" plane name
    4. List airports in a selected city
    5. Delete a plane
    6. List cities with Boeing planes between specified dates
    7. Quit the program
    
    Choice: 
    """.rstrip() + " "
)

goodbye = dedent(
    """
    ***********
    * Goodbye *
    ***********
    """
)
