from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from flask import Flask, render_template, request
# Sample campus information dataset
campus_data = [
    {
        "topic": "Green Campus",
        "information": (
            "VFSTR has approximately 50 percent of its campus "
            "covered with greenery, a herbal garden, lotus pond, "
            "greenhouse and hydroponics."
        ),
        "source": "https://vignan.ac.in/generalfacilities.php"
    },
    {
        "topic": "Administrative Block",
        "information": (
            "The VFSTR administrative block houses the Vice "
            "Chancellor Office, Examination Cell, Registrar Office, "
            "Training and Placement Cell, Student Affairs Office "
            "and Finance Section."
        ),
        "source": "https://vignan.ac.in/generalfacilities.php"
    },
    {
        "topic": "Hostel",
        "information": (
            "The VFSTR facilities page describes AC Deluxe, "
            "AC and Non AC hostel rooms with internet and Wi-Fi."
        ),
        "source": "https://vignan.ac.in/generalfacilities.php"
    },
    {
        "topic": "Cafeteria",
        "information": (
            "The VFSTR general facilities page describes a campus "
            "cafeteria with seating for 400 people and additional "
            "food kiosks near academic blocks."
        ),
        "source": "https://vignan.ac.in/generalfacilities.php"
    },
    {
        "topic": "Medical Facility",
        "information": (
            "VFSTR has a campus health centre that provides primary "
            "and secondary healthcare for students and staff."
        ),
        "source": "https://vignan.ac.in/generalfacilities.php"
    },
    {
        "topic": "Transport",
        "information": (
            "VFSTR provides bus transport for students and staff "
            "to surrounding towns and villages."
        ),
        "source": "https://vignan.ac.in/generalfacilities.php"
    },
        {
        "topic": "Library",
        "information": (
            "VFSTR has the NTR Memorial Library with books, "
            "reference materials, journals, e-books and "
            "digital learning resources."
        ),
        "source": "https://www.vignan.ac.in/vuresults11/"
    },
    {
        "topic": "Campus Safety",
        "information": (
            "VFSTR campus safety facilities include security "
            "personnel, CCTV surveillance, fire alarms and "
            "firefighting equipment."
        ),
        "source": "https://vignan.ac.in/generalfacilities.php"
    },
    {
        "topic": "Banking",
        "information": (
            "VFSTR's published facilities information mentions "
            "a UCO Bank branch and ATMs on campus."
        ),
        "source": "https://www.vignan.ac.in/vuresults11/"
    },
    {
        "topic": "Internet and Network",
        "information": (
            "VFSTR's published facilities information describes "
            "campus Wi-Fi and computer network facilities."
        ),
        "source": "https://vignan.ac.in/generalfacilities.php"
    },
    {
        "topic": "Sports",
        "information": (
            "VFSTR sports facilities include playgrounds for "
            "cricket, football, tennis, basketball, badminton "
            "and volleyball, along with a gymnasium and "
            "athletics track."
        ),
        "source": "https://vignan.ac.in/inadcampuslife.php"
    }
]

# Convert documents into TF-IDF vectors
documents = [
    item["topic"] + " " + item["information"]
    for item in campus_data
]
vectorizer = TfidfVectorizer()
document_vectors = vectorizer.fit_transform(documents)


def search_campus(query):
    query = query.lower().strip()

    if not query:
        return []

    # Keywords that identify supported campus topics
    topic_keywords = {
        "Medical Facility": [
            "medical", "doctor", "health", "hospital",
            "healthcare", "first aid", "sick", "ill",
            "medicine", "clinic", "nurse", "fever",
            "unwell", "health centre", "health center"
        ],
        "Library": [
            "library", "book", "books", "borrow",
            "reading", "read", "journal", "ebook"
        ],
        "Banking": [
            "bank", "banking", "atm", "cash", "money",
            "withdraw", "withdrawal", "deposit", "uco"
        ],
        "Hostel": [
            "hostel", "room", "accommodation", "boarding",
            "stay", "staying", "live", "living", "residence",
            "sleep", "lodging"
        ],
        "Transport": [
            "bus", "transport", "travel", "transportation",
            "route", "commute", "pickup", "drop"
        ],
        "Cafeteria": [
            "cafeteria", "food", "eat", "eating", "canteen",
            "lunch", "breakfast", "dinner", "snacks",
            "meal", "hungry", "hunger", "refreshments"
        ],
        "Sports": [
            "sports", "sport", "play", "playing", "game",
            "games", "cricket", "football", "basketball",
            "badminton", "volleyball", "tennis", "gym",
            "playground", "athletics", "fitness", "exercise"
        ],
        "Green Campus": [
            "greenery", "garden", "green", "environment",
            "plants", "trees", "nature", "pond", "greenhouse"
        ],
        "Campus Safety": [
            "security", "safety", "safe", "cctv",
            "camera", "fire", "protection", "guard"
        ],
        "Internet and Network": [
            "internet", "wifi", "wi-fi", "network",
            "online", "connection", "connectivity", "wireless"
        ],
        "Administrative Block": [
    "administration", "administrative", "registrar",
    "examination cell", "finance section",
    "office location", "documents", "certificate",
    "student affairs", "vice chancellor"
]
    }

    # Find topics with matching keywords
    matched_topics = []

    for topic, keywords in topic_keywords.items():
        for keyword in keywords:
            if keyword in query:
                matched_topics.append(topic)
                break

    # Reject questions with no known topic keywords
    if not matched_topics:
        return []

    # Calculate TF-IDF similarity
    query_vector = vectorizer.transform([query])

    scores = cosine_similarity(
        query_vector, document_vectors
    ).flatten()

    # Give priority to topics identified by keywords
    for index, item in enumerate(campus_data):
        if item["topic"] in matched_topics:
            scores[index] += 0.50

    # Only consider the topics matched by the question
    eligible_indices = [
        index for index, item in enumerate(campus_data)
        if item["topic"] in matched_topics
    ]

    # Select the best result among eligible topics
    best_index = max(eligible_indices, key=lambda i: scores[i])
    best_score = float(scores[best_index])

    # Reject weak matches
    if best_score < 0.35:
        return []

    return [(best_score, campus_data[best_index])]


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    results = []
    searched = False

    if request.method == "POST":
        query = request.form.get("query", "").strip()
        searched = True

        if query:
            results = search_campus(query)

    return render_template(
        "index.html",
        results=results,
        searched=searched
    )


if __name__ == "__main__":
    app.run(debug=True)

