# Next.js × Django Rest Framework ログイン

## 仮装環境の建て方
```
python -m venv venv
```

## 仮装環境の入り方
```
venv/Scripts/Activate.ps1
```

## 仮装環境の抜け方
```
deactivate
```

## ライブラリの導入
```
pip3 install -r requirements.txt
```

## Djangoプロジェクトの作成
```
django-admin startproject mysite
```

## アプリケーションの作成
```
python manage.py startapp <アプリ名>
```


## マイグレーション
```
python manage.py makemigrations
python manage.py migrate
```

## サーバの起動
```
python manage.py runserver
```

## スーパーユーザの作成
```
python manage.py createsuperuser
```