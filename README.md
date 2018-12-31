# twitter-analysis

## はじめに

ツイートを取得して、形態素解析をし、wordcloud で画像を出力します。

![wordcloud](./wordcloud_sample1.png)

## ライブラリインストール

```
pip install requests-oauthlib
pip install janome
pip install wordcloud
pip install emoji --upgrade
```

## config.py.example の修正

ファイルをコピーをして、ファイル名を config.py にする
twitter api のトークンを設定する

## 使い方

### get_user_timelines.py

ユーザのタイムラインツイートを取得
prams の screen_name にツイッターアカウント名を入れる

### get_search_tweets.py

検索キーワードのツイートを取得
params を適宜変更する

### post_tweet.py

ツイートをする

## 参考 URL

[Python で Twitter API を利用していろいろ遊んでみる](https://qiita.com/bakira/items/00743d10ec42993f85eb)

[【Python でテキストマイニング】Twitter データを WordCloud で可視化してみる](http://www.randpy.tokyo/entry/python_wordcloud)

[python で絵文字を駆逐する](https://qiita.com/yoshimo123/items/85331d881aed9ad41020)

[Twitter 開発者 ドキュメント日本語訳](http://westplain.sakuraweb.com/translate/twitter/Documentation/REST-APIs/Public-API/GET-search-tweets.cgi#)

[Twitter の検索 API によるつぶやきの精度を上げるための小技 4 選](https://e-yota.com/webservice/post-2427/)

[Python, Janome で日本語の形態素解析、分かち書き（単語分割）](https://note.nkmk.me/python-janome-tutorial/)

[テキストマイニング：WordCloud で文系女子と理系女子のツイートを可視化してみた](https://www.pc-koubou.jp/magazine/2646)

[python3 による日付の扱い方メモ](http://blog.gepuro.net/posts/how_to_handle_dates_with_python_3/)

[TwitterAPI で期間指定して Tweet を取得する方法](https://qiita.com/areph/items/0745cb744a12810334c6)

[公式 WordCloud](http://amueller.github.io/word_cloud/generated/wordcloud.WordCloud.html)
