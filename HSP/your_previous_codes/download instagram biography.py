import instaloader
username = input("")
loader = instaloader.Instaloader()
profile = instaloader.Profile.from_username(loader.context, username)
pr = profile.biography
print(pr)
