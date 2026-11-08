import os
from feedgen.feed import FeedGenerator

WATCHLIST_FILE = "watchlist.txt"
RSS_OUTPUT = "feed.xml"

def generate_rss():
    fg = FeedGenerator()
    fg.id('http://192.168.1.200/watchlist-rss') # O il tuo dominio/IP locale o DuckDNS
    fg.title('Syncplay Movie Watchlist')
    fg.link(href='http://192.168.1.200', rel='alternate')
    fg.description('Feed RSS automatico per i film da scaricare insieme')
    fg.language('it')

    if not os.path.exists(WATCHLIST_FILE):
        print(f"File {WATCHLIST_FILE} non trovato.")
        return

    with open(WATCHLIST_FILE, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for line in lines:
        if '|' not in line or line.startswith('#'):
            continue
        
        title, magnet = line.strip().split('|', 1)
        title = title.strip()
        magnet = magnet.strip()

        fe = fg.add_item()
        fe.id(magnet)
        fe.title(title)
        fe.link(href=magnet)
        fe.description(f"Download automatico per: {title}")

    fg.rss_file(RSS_OUTPUT, pretty=True)
    print(f"Feed RSS aggiornato con successo: {RSS_OUTPUT}")

if __name__ == '__main__':
    generate_rss()
