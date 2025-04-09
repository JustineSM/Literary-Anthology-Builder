def create_anthology():
    # Allows the user to specify book excerptts and creates a basic anthoology file!!

    print("Welcome to Justine's Literary Anthology Builder!")

    excerpts = []

    while True:
        book_title = input("Enter the title of a book (or type 'done' to finish): ")
        if book_title.lower() == "done":
            break

        try:
            start_page = int(
                input(f"Enter the starting page for the excerpt from '{book_title}': ")
            )
            end_page = int(
                input(f"Enter the ending page for the excerpt from '{book_title}': ")
            )
            if start_page > end_page or start_page < 1:
                print("Invalid page range. Please try again! :(")
                continue
        except ValueError:
            print("Invalid page number. Please enter a number! :(")
            continue

        # In a real application, I would try and read the content from the book file
        excerpt = (
            f"\n--- Excerpt from '{book_title}', pages {start_page}-{end_page} ---\n"
        )
        # Temporary placeholder content simulated
        excerpt += f"(Simulated content from pages {start_page} to {end_page} of '{book_title}')\n"
        excerpts.append(excerpt)

    if excerpts:
        output_filename = input(
            "Enter the name for your anthology file (e.g., my_anthology.txt): "
        )
        try:
            with open(output_filename, "w") as outfile:
                outfile.writelines(excerpts)
            print(f"\nAnthology created successfully in '{output_filename}'! :)")
        except Exception as e:
            print(f"Error creating the output file: {e}")
    else:
        print("No excerpts added. Anthology not created! :()")


if __name__ == "__main__":
    create_anthology()
