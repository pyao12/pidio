from django.shortcuts import render, redirect, get_object_or_404
from .models import SubDomain
from .forms import SubDomainForm, SubDomainEditForm
from .cf import add_record, edit_record, delete_record
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    subdomains = SubDomain.objects.filter(owner=request.user).order_by("base_domain", "subdomain_name")
    return render(request, "index.html", {"subdomains": subdomains})

@login_required
def create_subdomain(request):
    if request.method == "POST":
        form = SubDomainForm(request.POST)
        if form.is_valid():
            subdomain = form.save(commit=False)
            subdomain.owner = request.user
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

@login_required
def edit_subdomain(request, pk):
    subdomain = get_object_or_404(SubDomain, pk=pk, owner=request.user)
    if subdomain.owner != request.user:
        return redirect("index")
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

@login_required
def delete_subdomain(request, pk):
    subdomain = get_object_or_404(SubDomain, pk=pk, owner=request.user)
    if subdomain.owner != request.user:
        return redirect("index")
    if request.method == "POST":
        subdomain.delete()
        result = delete_record(subdomain.record_id, subdomain.base_domain.cloudflare_zone_id, 
        subdomain.base_domain.cloudflare_api_token)
        if result["success"]:
            return redirect("index")
        else:
            form.add_error(None, "删除子域名失败，请检查域名是否已存在或其他错误")
    return render(request, "delete_subdomain.html", {"subdomain": subdomain})