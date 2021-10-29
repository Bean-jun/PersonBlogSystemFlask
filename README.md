# PersonBlogSystem的Flask版本

### 一、对比PersonBlogSystem的区别

   本部分将介绍和之前的PersonBlogSystem的差异性，避免读者查看时产生误会~

1. 用户注册中不再处理腾讯云存储内容，均使用本地存储

   受影响范围：

    - 用户头像上传
    - 博客top_image上传
    - 目前不支持修改功能

2. 博客不再支持语雀同步

3. 更新oauth授权，但是这里的授权没有使用微博的oauth授权，而是采用自定制oauth系统，关于本系统有兴趣的小伙伴请点击查看[这里](https://github.com/Bean-jun/AuthSystem.git)

### 二、 使用方式

1. 请务必配置`conf.settings.py`中的`SUPER_USER`字段哦~
2. 安装依赖 `pip3 install -r requirments.txt`
3. 脚本命令行启动 `python3 manage.py runserver`

### 三、api接口文档

- [点我查看](./docs/APIDocuments.md)