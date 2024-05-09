URLs=["www.google.com&quot", "www.gmail.com&quot", "www.github.com&quot", "www.reddit.com&quot", "www.yahoo.com&quot"]
site=[]
for i in URLs:
    site.append(i[4:-9])
print(f"URLs: {URLs}")
print(f"Domínios: {site}")