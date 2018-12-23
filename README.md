# twitter-analysis

## ライブラリインストール

```
pip install requests requests-oauthlib
pip install janome
pip install wordcloud
pip install emoji --upgrade
```

## config.py.example の修正

ファイルをコピーをして、ファイル名を config.py にする
twitter api のトークンを設定する

## 使い方

1. params の screen_name にアカウント名を入れる（getTimelines2.py）
2. `python getTimeLines2.py`を実行し、ツイートを取得(output/tweet_data に出力される)
3. `python wordcloud.py` を実行し、Word Cloud の画像を出力する(wordcloud_sample.png)
   ※除外したい単語は counter 関数の中に記載する

## 参考 URL

[Python で Twitter API を利用していろいろ遊んでみる](https://qiita.com/bakira/items/00743d10ec42993f85eb)
[【Python でテキストマイニング】Twitter データを WordCloud で可視化してみる](http://www.randpy.tokyo/entry/python_wordcloud)
[python で絵文字を駆逐する](https://qiita.com/yoshimo123/items/85331d881aed9ad41020)
