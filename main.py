import os
import requests

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
IG_USER_ID = os.getenv("IG_USER_ID")
MEDIA_ID = os.getenv("MEDIA_ID")
TRIGGER_WORD = "buy"

def get_comments():
    url = f"https://graph.facebook.com/v19.0/{MEDIA_ID}/comments"
    params = { "access_token": ACCESS_TOKEN }
    return requests.get(url, params=params).json().get("data", [])

def reply_to_comment(comment_id, message):
    url = f"https://graph.facebook.com/v19.0/{comment_id}/replies"
    data = { "message": message, "access_token": ACCESS_TOKEN }
    return requests.post(url, data=data).json()

comments = get_comments()
for comment in comments:
    text = comment.get("text", "").lower()
    comment_id = comment.get("id")
    if TRIGGER_WORD in text:
        print(f"Trigger found: {text}")
        print(reply_to_comment(comment_id, "Hey! Check your DMs for the product link 🔗"))
