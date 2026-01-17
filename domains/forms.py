from django import forms
from .models import SubDomain
import re

class SubDomainForm(forms.ModelForm):
    class Meta:
        model = SubDomain
        fields = ["subdomain_name", "base_domain", "record_type", "record_value"]
    
    def clean_record_value(self):
        record_type = self.cleaned_data.get("record_type")
        record_value = self.cleaned_data.get("record_value")
        
        if record_type == "A":
            ipv4_pattern = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
            if not re.match(ipv4_pattern, record_value):
                raise forms.ValidationError("请输入有效的IPv4地址")
        elif record_type == "AAAA":
            ipv6_pattern = r"^([0-9a-fA-F]{1,4}:){7}([0-9a-fA-F]{1,4})$"
            if not re.match(ipv6_pattern, record_value):
                raise forms.ValidationError("请输入有效的IPv6地址")
        elif record_type == "CNAME":
            cname_pattern = r"^[a-zA-Z0-9][a-zA-Z0-9-]{0,61}[a-zA-Z0-9]\.[a-zA-Z]{2,}$"
            if not re.match(cname_pattern, record_value):
                raise forms.ValidationError("请输入有效的域名")
        
        return record_value

class SubDomainEditForm(forms.ModelForm):
    class Meta:
        model = SubDomain
        fields = ["record_type", "record_value"]
    
    def clean_record_value(self):
        record_type = self.cleaned_data.get("record_type")
        record_value = self.cleaned_data.get("record_value")
        
        if record_type == "A":
            ipv4_pattern = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
            if not re.match(ipv4_pattern, record_value):
                raise forms.ValidationError("请输入有效的IPv4地址")
        elif record_type == "AAAA":
            ipv6_pattern = r"^([0-9a-fA-F]{1,4}:){7}([0-9a-fA-F]{1,4})$"
            if not re.match(ipv6_pattern, record_value):
                raise forms.ValidationError("请输入有效的IPv6地址")
        elif record_type == "CNAME":
            cname_pattern = r"^[a-zA-Z0-9][a-zA-Z0-9-]{0,61}[a-zA-Z0-9]\.[a-zA-Z]{2,}$"
            if not re.match(cname_pattern, record_value):
                raise forms.ValidationError("请输入有效的域名")
        
        return record_value
