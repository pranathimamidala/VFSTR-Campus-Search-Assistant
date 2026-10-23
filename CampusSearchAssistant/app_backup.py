# Campus Search Assistant
# Version 1: Basic Keyword Search

campus_data = [
    {
        "topic": "Library",
        "information": "Students can borrow books from the campus library."
    },
    {
        "topic": "Examinations",
        "information": "Examination schedules and instructions are provided by the examination section."
    },
    {
        "topic": "Hostel",
        "information": "Hostel information includes accommodation and student facilities."
    },
    {
        "topic": "Sports",
        "information": "Students can access campus sports and recreational facilities."
    },
    {
        "topic": "Computer Science Department",
        "information": "The department provides information about computer science courses and laboratories."
    }
]


def search_campus(query):
    query_words = query.lower().split()
    results = []

    for item in campus_data:
        searchable_text = (
            item["topic"] + " " + item["information"]
        ).lower()

        matching_words = sum(
            1 for word in query_words
            if word in searchable_text
        )

        if matching_words > 0:
            results.append((matching_words, item))

    results.sort(key=lambda result: result[0], reverse=True)
    return results


print("=== Campus Search Assistant ===")

user_query = input("Enter your campus-related query: ").strip()

if user_query:
    results = search_campus(user_query)

    if results:
        print("\nRelevant Information:\n")

        for score, item in results:
            print("Topic:", item["topic"])
            print("Information:", item["information"])
            print("Matching words:", score)
            print("-" * 40)
    else:
        print("No matching information found.")
else:
    print("Please enter a search query.")