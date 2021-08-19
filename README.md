# PersonBlog的Flask版本

### 一、对比PersonBlogSystem的区别

   本部分将介绍和之前的PersonBlogSystem的差异性，避免读者查看时产生误会~

1. 用户注册中不再处理腾讯云存储内容，均使用本地存储

   受影响范围：

    - 用户头像上传
    - 博客top_image上传

2. 博客不再支持语雀同步
