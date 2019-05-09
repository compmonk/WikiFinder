from datetime import datetime

from core.WikiFinder import WikiFinder

if __name__ == '__main__':
    wiki = WikiFinder()
    while True:
        query = input("Enter your query: ")
        if query.lower() == "exit":
            break
        start = datetime.now()
        pages = wiki.search(query)
        seconds = (datetime.now() - start).microseconds / 1e6
        if pages:
            print("\nFound {0} results in {1} seconds\n{2}\n".format(len(pages),
                                                                     seconds,
                                                                     "*" * 50))
            for page in pages:
                print(page)
                print()
        else:
            print("No results found\n")
        print("*" * 50)
