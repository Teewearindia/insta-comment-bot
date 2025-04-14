import requests

ACCESS_TOKEN = "PASTE_YOUR_LONG_LIVED_TOKEN"
IG_USER_ID = "17841472887866949"
MEDIA_ID = "PASTE_YOUR_REEL_ID"
TRIGGER_WORD = "buy"

def get_comments():
    url = f"https://graph.facebook.com/v19.0/{MEDIA_ID}/comments"
    params = {
        "access_token": ACCESS_TOKEN
    }
    res = requests.get(url, params=params).json()
    return res.get("data", [])

def reply_to_comment(comment_id, message):
    url = f"https://graph.facebook.com/v19.0/{comment_id}/replies"
    data = {
        "message": message,
        "access_token": ACCESS_TOKEN
    }
    res = requests.post(url, data=data).json()
    return res

comments = get_comments()
for comment in comments:
    text = comment.get("text", "").lower()
    comment_id = comment.get("id")

    if TRIGGER_WORD in text:
        print(f"Trigger found in comment: {text}")
        response = reply_to_comment(comment_id, "Hey! Check your DMs for the product link 🔗")
        print(response)
