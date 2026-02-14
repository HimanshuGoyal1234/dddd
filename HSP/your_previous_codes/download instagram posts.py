import instaloader
username = input("")
loader = instaloader.Instaloader()
profile = instaloader.Profile.from_username(loader.context, username)
for post in profile.get_posts():
    loader.download_post(post, target=profile.username)
