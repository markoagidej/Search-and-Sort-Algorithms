from flask import Flask

app = Flask(__name__)

video_titles = [
    "The Art of Coding",
    "Exploring the Cosmos",
    "Cooking Masterclass: Italian Cuisine",
    "History Uncovered: Ancient Civilizations",
    "Fitness Fundamentals: Strength Training",
    "Digital Photography Essentials",
    "Financial Planning for Beginners",
    "Nature's Wonders: National Geographic",
    "Artificial Intelligence Revolution",
    "Travel Diaries: Discovering Europe"
]

# Task 1: Implement the binary search algorithm for searching videos by title.

def binarySearchVideos(video_list, search):
    video_sorted = sorted(video_list)
    low = 0
    high = len(video_list) - 1
    while low <= high :
        mid = (low + high) // 2
        if video_sorted[mid].lower()[:len(search)] == search:
            return video_sorted[mid]
        elif video_sorted[mid].lower()[:len(search)] < search:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Task 2: Develop a REST API endpoint using Flask that allows users to search for videos by their titles using the binary search developed in Task 1. This API should accept a search query as input and return the matching videos, if any.

@app.route("/video_search/<string:searchTerm>", methods=["GET"])
def getMatchingVideoTitle(searchTerm):
    return binarySearchVideos(video_titles, searchTerm.lower())

# Task 3: Test the video search functionality using Postman or a similar tool. Send requests to the API endpoint created in Task 2 with different search queries to verify its correctness and efficiency. Ensure that the API returns the expected results for both existing and non-existing videos.

if __name__ == '__main__':
    app.run(debug=True)