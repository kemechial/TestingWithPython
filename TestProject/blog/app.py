blogs = dict()
MENU_PROMPT = ("Please enter a key to continue. (q, quit, c, create blog \
                , l, print, r, read, p, create post)")

def menu():
    print_blogs()
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            read_blog()

def ask_create_blog():
    pass

def read_blog():
    pass

def print_blogs():
    for name,blog in blogs.items():
        print("name: {} - blog: {}".format(name,blog))

