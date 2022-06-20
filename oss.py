# -*- coding: utf-8 -*-
import os

import oss2

class Oss():
    def __init__(self):
        self.access_key_id = ''
        self.access_key_secret = ''
        self.bucket_name = ''
        self.endpoint = 'oss-cn-beijing-internal.aliyuncs.com' # 最好内网地址
        self.access_key_id2 = ''
        self.access_key_secret2 = ''
        self.bucket_name2 = ''
        self.endpoint2 = 'oss-cn-beijing-internal.aliyuncs.com' # 最好内网地址

    def getInfo(self):
        bucket = oss2.Bucket(oss2.Auth(self.access_key_id, self.access_key_secret), self.endpoint, self.bucket_name)
        bucket2 = oss2.Bucket(oss2.Auth(self.access_key_id2, self.access_key_secret2), self.endpoint2, self.bucket_name2)
        i = 0
        list = []
        for obj in oss2.ObjectIteratorV2(bucket):
            i = i+1
            # 判断目录是否存在
            # 判断文件是否存在
            print('开始：'+obj.key)
            if bucket2.object_exists(obj.key) == False:
                path = './file/'+obj.key
                if '/' in obj.key:
                    file_dir = os.path.dirname(path)
                    if os.path.exists(file_dir) == False:
                        os.makedirs(file_dir)
                if os.path.isdir(path) == False:
                    try:
                        bucket.get_object_to_file(obj.key, path)
                        bucket2.put_object_from_file(obj.key, path)
                        print('下载上传搞定：' + obj.key)
                        os.remove(path)
                    except:
                        print('失败一个' + obj.key)
                        list.append(obj.key)
                # if not os.path.exists(path):
                print('完成：' + obj.key)
            else:
                print('已存在：' + obj.key)
            print(i)
            print(list)
        print(list)


if __name__ == '__main__':
    Oss().getInfo()

