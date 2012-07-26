1.安装paramiko
  参见文档：http://wiki.cloud.centrin.com.cn/wiki/index.php/Paramiko%E7%9A%84%E5%AE%89%E8%A3%85

2.生成数据库表
  创建mysql数据库
  修改配置文件vrmp/settings.py，DATABASES中的参数，根据创建的mysql数据库填写
  执行命令python manage.py syncdb，生成数据库表
  在执行命令的过程中，会要求生成一个超级用户的用户名和密码，请牢记用户名和密码，将作为登录admin的账号

3.启动服务
  执行命令python manage.py runserver ***.***.***.***:8000

4.访问地址
  http://***.***.***.***:8000/admin/
  登录信息为之前生成的超级用户的用户名和密码

备注：
  ***.***.***.***为当前主机的ip
  上文提到的文件相对路径以及执行命令的目录均为vrmpadmin目录