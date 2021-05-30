# django-official-tutorial01
## 概要
[参照公式ドキュメント](https://docs.djangoproject.com/ja/3.2/intro/tutorial01/)
* Python 3.9.2
* Django 3.2.2

***
**投票アプリケーション**
以下の２つの部分から構成される。
1. ユーザが投票したり結果を表示したりできる公開用サイト
2. 投票項目の追加、変更、削除を行うための管理 (admin) サイト
3. Viewの構成
    質問 "インデックス" ページ -- 最新の質問をいくつか表示
    質問 "詳細" ページ -- 結果を表示せず、質問テキストと投票フォームを表示
    質問 "結果" ページ -- 特定の質問の結果を表示
    投票ページ -- 特定の質問の選択を投票として受付

**ディレクトリ構成**
* プロジェクト名 - mysite
* アプリ名 - polls
    * モデル
        1. Question
        2. Choice


mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py



## 手順
1. プロジェクトの作成
    `django-admin startproject プロジェクト名 .`
    ` . `で現在のディレクトリ内にプロジェクトを作成する
2. アプリの作成
    `django-admin startapp アプリ名`
    アプリのディレクトリ内に「urls.py」を作成する

[その２](https://docs.djangoproject.com/ja/3.2/intro/tutorial02/)

3. settings.pyへの記述
    * INSTALLED_APPSアプリの追加 `アプリ名.apps.アプリ名Config`
    * TEMPLATES `'DIRS': [ BASE_DIR ],` ルート直下に「templates」フォルダの作成
    * 言語、タイムゾーン、データベースの設定
    * **カスタムユーザーモデルを使用する場合はこの時点で別途追記**

4. migrateの実行
    * `python ./manage.py makemigrations (アプリ名)`
        モデルの変更がある場合に行う、アプリ名の記述がないと全てのアプリが確認される
    * `python ./manage.py migrate`
        `python manage.py sqlmigrate アプリ名 0001`
        実行したSQL文が確認できる

5. Modelの作成
    * `アプリ名/models.py`にモデルを追加→マイグレーション
    * 管理画面からモデルを操作するには、`アプリ名/admin.py`に追記

6. Viewの作成
    `function based view` ...関数を用いたView
    `class based View`...予め一定の機能が実装されているclass View

## その他
* シェルを起動する
    `python manage.py shell`

* Viewの基本的な役割
    `Httpレスポンスを返すか例外を返すか`
    レコードを取り出したり、PDF,ZIPを生成したり自由。
    Djangoにとって重要なのはHttpResponceか例外か



## 注意点
`urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]`
**urlのパスの後ろの「/」は必ずつける**

* `HttpResponse`...Httpレスポンスを返す
* `render`...テンプレートをロードしてcontextに値を入れて返す
    `return HttpResponse(template.render(context, request))`
    `return render(request, 'polls/index.html', context)`

[**templateで使用するnamespaceについて**](https://docs.djangoproject.com/ja/3.2/intro/tutorial03/)


## 設計思想
`なぜ ObjectDoesNotExist 例外を高水準で自動的にキャッチせず、ヘルパー関数 get_object_or_404() を使うのでしょうか、また、なぜモデル API に ObjectDoesNotExist ではなく、 Http404 を送出させるのでしょうか?
答えは、モデルレイヤとビューレイヤをカップリングしてしまうからです。 Django の最も大きな目標の一つは、ルーズカップリングの維持にあります。いくつかの制御カップリングは、 django.shortcuts モジュールの中にあります。`
