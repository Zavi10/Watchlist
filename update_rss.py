name: Aggiorna RSS Watchlist

on:
  push:
    paths:
      - 'watchlist.txt'

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout del codice
        uses: actions/checkout@v4

      - name: Configura Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Installa dipendenze
        run: pip install feedgen

      - name: Esegui script di generazione RSS
        run: python update_rss.py

      - name: Configura Git per il commit automatico
        run: |
          git config --global user.name "github-actions[bot]"
          git config --global user.email "41898282+github-actions[bot]@users.noreply.github.com"
          git add feed.xml
          git commit -m "Aggiornamento automatico feed RSS [skip ci]" || exit 0
          git push
