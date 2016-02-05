#### 一个基于flask的二维码生成器

执行以下命令
```
pip install -r req.txt
gunicorn -k gevent -w 1 -b 127.0.0.1:5003 views:app
```

然后打开浏览器访问`localhost:5003`
