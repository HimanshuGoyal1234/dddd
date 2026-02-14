import pygetwindow as gw
windows = gw.getAllTitles()
open_windows = [window for window in windows if window.strip()]
print(f"Number of open windows: {len(open_windows)}")
print("Open windows:")
for i, window in enumerate(open_windows, start=1):
    print(f"{i}. {window}")
