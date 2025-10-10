import requests
from tqdm import tqdm
import sys
import getpass
import re

# Danh sách các domain cần thêm vào danh sách đen
DOMAINS = [
    "*.vpp.itunes.apple.com",
    "*.daw.apple.com",
    "*.deviceservices.apple.com",
    "*.profile.ess.apple.com",
    "*.sq-device.apple.com",
    "*.static.ips.apple.com",
    "*.ppq.apple.com",
    "*.tbsc.apple.com",
    "*.acactivationd.apple.com",
    "*.deviceenrollment.apple.com",
    "*.mdmenrollment.apple.com",
    "*.iprofiles.apple.com",
    "*.gsa.apple.com",
    "*.albert.apple.com",
    "*.findmyiphone.icloud.com",
    "*.fmfmobile.icloud.com",
    "*.deviceservices-external.apple.com",
    "*.push.apple.com",
    "*.gs.apple.com",
    "*.configuration.apple.com",
    "*.mesu.apple.com",
    "*.ocsp.apple.com",
    "*.idmsa.apple.com",
    "*.apple.com",
    "*.icloud.com",
    "*.authkit.apple.com",
    "*.appleid.apple.com",
    "*.setup.icloud.com",
    "*.identity.icloud.com",
    "*.identity.apple.com",
    "*.gateway.icloud.com",
    "*.activationlock.apple.com",
    "*.fmf.icloud.com",
    "*.fmip.icloud.com",
    "*.findmy.icloud.com",
    "*.findmy.apple.com",
    "*.fmipmobile.icloud.com"
]

def display_copyright():
    # Sử dụng ANSI escape codes để in đậm và gạch chân
    BOLD_UNDERLINE = "\033[1m\033[4m"
    RESET = "\033[0m"
    print(f"{BOLD_UNDERLINE}Quang Bảo{RESET} - Bản quyền tool tự động thêm domain vào danh sách đen.")

def validate_api_key(api_key):
    # Kiểm tra định dạng API key (ví dụ: phải dài ít nhất 10 ký tự và chỉ chứa chữ, số, dấu gạch ngang, dấu gạch dưới)
    if not re.match(r'^[a-zA-Z0-9\-_]{10,}$', api_key):
        return False, "API key không hợp lệ. Phải chứa ít nhất 10 ký tự (chữ, số, -, _)."
    return True, ""

def add_domain_to_blacklist(api_endpoint, api_key, profile_id, domain):
    url = f"{api_endpoint}/profiles/{profile_id}/blacklist/add"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "domain": domain
    }
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=10)
        if response.status_code == 200:
            return True, response.json().get("message", "Thêm thành công")
        else:
            return False, response.text
    except requests.RequestException as e:
        return False, f"Lỗi kết nối: {str(e)}"

def main():
    display_copyright()
    
    # Nhập API endpoint
    api_endpoint = input("Nhập API endpoint (ví dụ: https://api.example.com): ").strip()
    if not api_endpoint:
        print("API endpoint không được để trống.")
        sys.exit(1)
    
    # Nhập API key (ẩn ký tự khi nhập)
    api_key = getpass.getpass("Nhập API key (ẩn khi nhập): ").strip()
    is_valid, error_message = validate_api_key(api_key)
    if not is_valid:
        print(error_message)
        sys.exit(1)
    
    # Nhập Profile ID
    profile_id = input("Nhập Profile ID: ").strip()
    if not profile_id:
        print("Profile ID không được để trống.")
        sys.exit(1)
    
    print("\nBắt đầu thêm các domain vào danh sách đen...")
    success_count = 0
    failed_domains = []
    
    # Sử dụng tqdm để hiển thị tiến độ
    for domain in tqdm(DOMAINS, desc="Tiến độ", unit="domain"):
        success, message = add_domain_to_blacklist(api_endpoint, api_key, profile_id, domain)
        if success:
            success_count += 1
        else:
            failed_domains.append((domain, message))
    
    print("\nHoàn tất!")
    print(f"Thêm thành công: {success_count}/{len(DOMAINS)} domain.")
    
    if failed_domains:
        print("\nCác domain thất bại:")
        for domain, error in failed_domains:
            print(f"- {domain}: {error}")

if __name__ == "__main__":
    main()