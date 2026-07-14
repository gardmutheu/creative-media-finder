# ==========================================
# Interactive Creative Media Finder Tool
# Developed by: gardmutheu
# ==========================================

media_database = {
    "Inception": {
        "Genre": "Sci-Fi",
        "Rating": 8.8,
        "User_Reviews": [8.8],
        "Comments": []
    },

    "La La Land": {
        "Genre": "Musical/Romance",
        "Rating": 8.0,
        "User_Reviews": [8.0],
        "Comments": []
    },

    "Interstellar": {
        "Genre": "Sci-Fi",
        "Rating": 8.7,
        "User_Reviews": [8.7],
        "Comments": []
    },

    "Whiplash": {
        "Genre": "Drama/Music",
        "Rating": 8.5,
        "User_Reviews": [8.5],
        "Comments": []
    }
}


def search_movie():

    title = input("\nEnter movie name: ").strip().title()

    if title in media_database:

        movie = media_database[title]

        print("\n========== MOVIE DETAILS ==========")
        print("Title :", title)
        print("Genre :", movie["Genre"])
        print("Rating:", movie["Rating"], "/10")

        if movie["Comments"]:
            print("\nPublic Comments")
            print("----------------")

            for comment in movie["Comments"]:
                print("-", comment)

        else:
            print("\nNo comments yet.")

        return title

    else:
        print("\nMovie not found.")
        return None


def rate_movie(title):

    try:

        score = float(input("Rate this movie (0-10): "))

        if 0 <= score <= 10:

            media_database[title]["User_Reviews"].append(score)

            average = sum(media_database[title]["User_Reviews"]) / len(
                media_database[title]["User_Reviews"]
            )

            media_database[title]["Rating"] = round(average, 1)

            print("Rating submitted successfully!")

        else:

            print("Rating must be between 0 and 10.")

    except ValueError:

        print("Please enter a valid number.")


def add_comment(title):

    comment = input("Write your public comment: ")

    if comment.strip():

        media_database[title]["Comments"].append(comment)

        print("Comment published successfully!")

    else:

        print("Comment cannot be empty.")


def display_movies():

    print("\nAvailable Movies")
    print("---------------------------")

    for movie in media_database:
        print(movie)


def main():

    while True:

        print("\n==============================")
        print("CREATIVE MEDIA FINDER")
        print("==============================")

        print("1. View Movies")
        print("2. Search Movie")
        print("3. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":

            display_movies()

        elif choice == "2":

            movie = search_movie()

            if movie:

                print("\n1. Rate Movie")
                print("2. Add Public Comment")
                print("3. Back")

                option = input("Choose: ")

                if option == "1":
                    rate_movie(movie)

                elif option == "2":
                    add_comment(movie)

        elif choice == "3":

            print("\nGoodbye!")

            break

        else:

            print("Invalid option.")


if __name__ == "__main__":
    main()
