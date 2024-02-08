import google.oauth2.credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from firebase_admin import auth

# Function to get YouTube service object
def get_youtube_service(credentials):
    service = build('youtube', 'v3', credentials=credentials)
    return service

# Function to upload video to YouTube
def upload_video(youtube_service, video_path, video_title, video_description):
    request = youtube_service.videos().insert(
        part='snippet,status',
        body={
            'snippet': {
                'title': video_title,
                'description': video_description
            },
            'status': {
                'privacyStatus': 'public'  # Change privacy status as needed
            }
        },
        media_body=video_path
    )
    response = request.execute()
    print('Video uploaded:', response)

# Function to sign in with Google using Firebase Authentication
def sign_in_with_google(id_token):
    try:
        decoded_token = auth.verify_id_token(id_token)
        user_uid = decoded_token['uid']
        user = auth.get_user(user_uid)
        return user
    except auth.InvalidIdTokenError:
        print("Invalid ID token.")
        return None
    except auth.ExpiredIdTokenError:
        print("Expired ID token.")
        return None
    except auth.RevokedIdTokenError:
        print("Revoked ID token.")
        return None

# Example usage
def main():
    # Sign in with Google and get the user
    user = sign_in_with_google(id_token)
    
    # Obtain OAuth 2.0 access token from the user's credentials
    access_token = user['providerData'][0]['accessToken']
    
    # Use the access token to create YouTube service object
    youtube_service = get_youtube_service(access_token)
    
    # Upload video to YouTube
    video_path = 'path_to_video_file.mp4'
    video_title = 'My Video Title'
    video_description = 'Description of my video'
    upload_video(youtube_service, video_path, video_title, video_description)

if __name__ == "__main__":
    main()
