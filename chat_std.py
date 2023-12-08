# -*- coding: utf-8 -*-
import json
import os

from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.hunyuan.v20230901 import hunyuan_client, models
from tencentcloud.common.profile.client_profile import ClientProfile

try:
    # 实例化一个认证对象，入参需要传入腾讯云账户 secretId，secretKey
    cred = credential.Credential(
        os.environ.get("TENCENTCLOUD_SECRET_ID"),
        os.environ.get("TENCENTCLOUD_SECRET_KEY"))

    client_profile = ClientProfile()
    # client_profile.httpProfile.endpoint = "localhost:8080"
    # client_profile.httpProfile.protocol = "http"
    # client_profile.httpProfile.scheme = "http"

    client = hunyuan_client.HunyuanClient(cred, "ap-guangzhou", client_profile)
    client.set_stream_logger(level="DEBUG")

    req = models.ChatStdRequest()
    msg = models.Message()
    msg.Role = "user"
    msg.Content = "你好，可以讲个笑话吗"

    msg2 = models.Message()
    msg2.Role = "assistant"
    msg2.Content = '''当然可以！这是一个爆笑笑话：

老师让小明造一句有“哥哥”二字的话。小明：“哥哥昨天晚上又玩游戏了。”

老师：“那你知道哥哥昨天玩什么游戏？”

小明：“不知道，我只知道哥哥又输了。”

这个笑话的笑点在于，它使用了双关语和幽默元素。第一个双关语是“哥哥”，既表示兄弟之间的称呼，也可以表示游戏角色的名称。第二个双关语是“又输了”，既表示游戏输了，也可以表示哥哥输了。这种双关语和幽默元素的结合，使得这个笑话非常搞笑。
'''

    msg3 = models.Message()
    msg3.Role = "user"
    msg3.Content = "不好笑，再讲一个"

    req.Messages = [msg]
    # req.Messages = [msg, msg2, msg3]

    resp = client.ChatStd(req)

    full_content = ""
    for event in resp:
        print(event)
        data = json.loads(event['data'])
        for choice in data['Choices']:
            full_content += choice['Delta']['Content']

    print(full_content)

except TencentCloudSDKException as err:
    print(err)
