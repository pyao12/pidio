from django.shortcuts import render, redirect
from .models import SubDomain
from .forms import SubDomainForm, SubDomainEditForm
from .cf import add_record, edit_record, delete_record

def index(request):
    subdomains = SubDomain.objects.all()
    return render(request, "index.html", {"subdomains": subdomains})

def create_subdomain(request):
    if request.method == "POST":
        form = SubDomainForm(request.POST)
        if form.is_valid():
            subdomain = form.save(commit=False)
            result = add_record(subdomain.subdomain_name, subdomain.record_type, subdomain.record_value, 
            subdomain.base_domain.cloudflare_zone_id, subdomain.base_domain.cloudflare_api_token)
            if result["success"]:
                subdomain.record_id = result["id"]
                subdomain.save()
                return redirect("index")
            else:
                form.add_error(None, "添加子域名失败，请检查域名是否已存在或其他错误")
    else:
        form = SubDomainForm()
    return render(request, "create_subdomain.html", {"form": form})

def edit_subdomain(request, pk):
    subdomain = SubDomain.objects.get(pk=pk)
    if request.method == "POST":
        form = SubDomainEditForm(request.POST, instance=subdomain)
        if form.is_valid():
            subdomain = form.save(commit=False)
            result = edit_record(subdomain.record_id, subdomain.subdomain_name, subdomain.record_type, 
            subdomain.record_value, subdomain.base_domain.cloudflare_zone_id, subdomain.base_domain.cloudflare_api_token)
            if result["success"]:
                subdomain.save()
                return redirect("index")
            else:
                form.add_error(None, "编辑子域名失败，请检查域名是否已存在或其他错误")
    else:
        form = SubDomainEditForm(instance=subdomain)
    return render(request, "edit_subdomain.html", {"form": form, "subdomain": subdomain})

def delete_subdomain(request, pk):
    subdomain = SubDomain.objects.get(pk=pk)
    if request.method == "POST":
        subdomain.delete()
        result = delete_record(subdomain.record_id, subdomain.base_domain.cloudflare_zone_id, 
        subdomain.base_domain.cloudflare_api_token)
        if result["success"]:
            return redirect("index")
        else:
            form.add_error(None, "删除子域名失败，请检查域名是否已存在或其他错误")
    return render(request, "delete_subdomain.html", {"subdomain": subdomain})