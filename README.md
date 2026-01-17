# Pidio

一个简单易用的二级域名分发系统，基于Django。

## 安装

您可以通过Docker运行：

```bash
docker run -p 8000:8000 \
    -e SECRET_KEY="insecure_key" \
    -v $(pwd)/pidio:/app/data \
    ghcr.io/pyao12/pidio:latest
```

强烈建议您在生产环境中使用随机的`SECRET_KEY`，具体参考[环境变量](#环境变量)。

默认使用的是SQLite数据库，数据库文件在宿主机当前目录下的`db.sqlite3`。

如果国内拉取镜像较慢，您可以从`ghcr.nju.edu.cn/pyao12/pidio:latest`拉取镜像。

### 环境变量

需要设置以下docker环境：

- `SECRET_KEY`：Django 项目的密钥，用于加密会话数据等。默认是 `insecure_key`，这并不安全。

建议长度大于64字符，同时要包含字母、数字和特殊字符。

### 挂载卷

为了持久化数据，建议挂载一个卷到容器的`/app/data`目录。