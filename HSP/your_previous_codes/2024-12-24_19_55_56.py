import instaloader

# Create an instance of Instaloader
L = instaloader.Instaloader()

# Log in with your Instagram credentials
username = "HimanshuDW31"
password = ""

try:
    L.login(username, password)
    print("Logged in successfully!")
except Exception as e:
    print(f"Login failed: {e}")

# Example: Fetch your profile data
profile = instaloader.Profile.from_username(L.context, username)
print(f"Your profile name: {profile.full_name}")
print(f"Number of followers: {profile.followers}")
print(f"Number of followees: {profile.followees}")
