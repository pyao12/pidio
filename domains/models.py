from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BaseDomain(models.Model):
    class Meta:
        verbose_name = "基础域名"
        verbose_name_plural = "基础域名"

    domain_name = models.CharField(max_length=255, unique=True, verbose_name="域名")
    cloudflare_zone_id = models.CharField(max_length=64, verbose_name="Cloudflare Zone ID")
    cloudflare_api_token = models.CharField(max_length=64, verbose_name="Cloudflare API Token")

    def __str__(self):
        return self.domain_name

class SubDomain(models.Model):
    class Meta:
        verbose_name = "子域名"
        verbose_name_plural = "子域名"

    subdomain_name = models.CharField(max_length=255, unique=True, verbose_name="子域名")
    base_domain = models.ForeignKey(BaseDomain, on_delete=models.CASCADE, verbose_name="基础域名")
    record_type = models.CharField(max_length=10, 
        choices=[("A", "A记录"), ("AAAA", "AAAA记录"), ("CNAME", "CNAME记录")], verbose_name="记录类型")
    record_value = models.CharField(max_length=255, verbose_name="记录值")
    record_id = models.CharField(max_length=64, verbose_name="Cloudflare Record ID")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="所有者")

    def __str__(self):
        return f"{self.subdomain_name}.{self.base_domain}"
