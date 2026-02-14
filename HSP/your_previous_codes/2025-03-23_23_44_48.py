from tqdm import tqdm
import requests
while True:
    url = input("")
    r = requests.get(url, stream=True)

    totalExpectedBytes = int(r.headers['Content-Length'])
    bytesReceived = 0

    progress_bar = tqdm(total=totalExpectedBytes, unit='B', unit_scale=True)

    with open("red2q.mp4", "wb") as f:
        for chunk in r.iter_content(chunk_size=128):
            if chunk:
                f.write(chunk)
                progress_bar.update(len(chunk))

    progress_bar.close()
