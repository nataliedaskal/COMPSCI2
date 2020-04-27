import requests
import matplotlib.pyplot as plt


url = "https://www.gutenberg.org/files/1342/1342-0.txt"
pride_prejudice = requests.get(url).text

print(pride_prejudice[:1000])

wordlist = pride_prejudice.split()
wordlist = [x.upper().strip('?.:;!\\<>{}\n\t') for x in wordlist]

print(wordlist[:1000])