""" 定义BaseDomain和SubDomain域名模型 """

from django.db import models

# Create your models here.
class BaseDomain(models.Model):
    """基础域名，这里是所有子域名的一级域名，只有staff能够管理"""

    class Meta:
        verbose_name = "基础域名"
        verbose_name_plural = "基础域名"

    domain_name = models.CharField(
        max_length=255, unique=True, verbose_name="域名"
        )
    cloudflare_zone_id = models.CharField(
        max_length=64, verbose_name="Cloudflare Zone ID"
        )
    cloudflare_api_token = models.CharField(
        max_length=64, verbose_name="Cloudflare API Token"
        )

    def __str__(self):
        return self.domain_name

class SubDomain(models.Model):
    """子域名，每个子域名都有一个对应的基础域名，用户可以直接管理（后续实现）"""

    class Meta:
        verbose_name = "子域名"
        verbose_name_plural = "子域名"

    subdomain_name = models.CharField(
        max_length=255, unique=True, verbose_name="子域名"
        )
    base_domain = models.ForeignKey(
        BaseDomain, on_delete=models.CASCADE, verbose_name="基础域名")
    record_type = models.CharField(
        max_length=10, 
        choices=[("A", "A记录"), ("AAAA", "AAAA记录"), ("CNAME", "CNAME记录")], 
        verbose_name="记录类型"
        )
    record_value = models.CharField(
        max_length=255, verbose_name="记录值"
        )

    def __str__(self):
        return f"{self.subdomain_name}.{self.base_domain}"
