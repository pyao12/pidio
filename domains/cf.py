import requests

def add_record(subdomain_name, record_type, record_value, zone_id, api_key):
    url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "type": record_type,
        "name": f"{subdomain_name}",
        "content": record_value
    }
    try:
        response = requests.post(url, headers=headers, json=data, timeout=10)
        response_data = response.json()
        if not response_data.get("success"):
            errors = response_data.get("errors", [])
            error_messages = [error.get("message", "Unknown error") for error in errors]
            return {"success": False, "error": ", ".join(error_messages)}
        record = response_data.get("result", {})
        return {"success": True, "id": record.get("id"), "data": record}
    except requests.exceptions.RequestException as e:
        return {"success": False, "error": str(e)}

def edit_record(record_id, subdomain_name, record_type, record_value, zone_id, api_key):
    url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records/{record_id}"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "type": record_type,
        "name": f"{subdomain_name}",
        "content": record_value
    }
    try:
        response = requests.patch(url, headers=headers, json=data, timeout=10)
        response_data = response.json()
        if not response_data.get("success"):
            errors = response_data.get("errors", [])
            error_messages = [error.get("message", "Unknown error") for error in errors]
            return {"success": False, "error": ", ".join(error_messages)}
        record = response_data.get("result", {})
        return {"success": True, "id": record.get("id"), "data": record}
    except requests.exceptions.RequestException as e:
        return {"success": False, "error": str(e)}

def delete_record(record_id, zone_id, api_key):
    url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records/{record_id}"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    try:
        response = requests.delete(url, headers=headers, timeout=10)
        response_data = response.json()
        if not response_data.get("success"):
            errors = response_data.get("errors", [])
            error_messages = [error.get("message", "Unknown error") for error in errors]
            return {"success": False, "error": ", ".join(error_messages)}
        return {"success": True}
    except requests.exceptions.RequestException as e:
        return {"success": False, "error": str(e)}
