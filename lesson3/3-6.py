is_logged_in = True
is_admin = True

if is_logged_in:
    print("Welcome back!")
    if is_admin:
        print("Show admin dashboard.")
    else:
        print("Show regular dashboard.")
else:
    print("Please log in to continue.")