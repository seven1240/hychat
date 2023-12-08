# 一个简单的聊天程序

使用腾讯混元大模型。

如果你不能访问腾讯混元大模型，可以使用 `mock_server.py` 模拟。

## 准备


```bash
pip install --upgrade tencentcloud-sdk-python
```

## 使用方法

```bash
export TENCENTCLOUD_SECRET_ID=你的腾讯云 SecretID
export TENCENTCLOUD_SECRET_KEY=你的腾讯云 SecretKey
```

```bash
python chat_std.py
```

## 使用 Mock Server：

```bash
python mock_server.py
```

修改 `chat_std.py`中被注释的相关行，打开另一个终端，

```bash
python chat_std.py
```

## 联系我

https://www.dujinfang.com
