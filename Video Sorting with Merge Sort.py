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

# Task 1: Implement the merge sort algorithm in Python to sort videos by their titles..

def mergeSortVideos(video_list):
    if len(video_list) > 1:
        mid = len(video_list) // 2
        left = video_list[:mid]
        right = video_list[mid:]

        mergeSortVideos(left)
        mergeSortVideos(right)

        left_index = right_index = main_index = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                video_list[main_index] = left[left_index]
                left_index += 1
            else:
                video_list[main_index] = right[right_index]
                right_index += 1

            main_index += 1

        while left_index < len(left):
            video_list[main_index] = left[left_index]
            left_index += 1
            main_index += 1
            
        while right_index < len(right):
            video_list[main_index] = right[right_index]
            right_index += 1
            main_index += 1            

# Task 2: Develop another REST API endpoint using Flask that allows users to fetch a list of videos sorting alphabetically by their titles using the merge sort developed in Task 1.

@app.route("/video_sort", methods=["GET"])
def sortVideos():
    mergeSortVideos(video_titles)
    return video_titles

# Task 3: Test the video sorting functionality using Postman or a similar tool. Send requests to the API endpoint created in Task 2 and verify its correctness and efficiency. Ensure that the API returns the expected results.

if __name__ == '__main__':
    app.run(debug=True)