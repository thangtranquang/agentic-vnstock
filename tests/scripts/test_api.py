import urllib.request
import json
import urllib.parse
import time

# 1. Đọc cái file workflow API anh vừa tải (giả sử tên là workflow_api.json)
with open("workflow_api.json", "r", encoding="utf-8") as f:
    prompt_text = f.read()

prompt = json.loads(prompt_text)

# 2. Đóng gói gửi lên Server ComfyUI
p = {"prompt": prompt}
data = json.dumps(p).encode('utf-8')
req = urllib.request.Request("http://127.0.0.1:8188/prompt", data=data)

# 3. Chờ nhận ID của hàng đợi (Prompt ID)
try:
    response = urllib.request.urlopen(req)
    result = json.loads(response.read())
    prompt_id = result['prompt_id']
    print(f"✅ Đã gửi lệnh thành công! ID hàng đợi: {prompt_id}")
    print("⏳ Đang chờ Card RTX 5880 xử lý (khoảng 10-30s)...")
except Exception as e:
    print("❌ Lỗi gọi API:", e)
    exit()

# 4. Viết vòng lặp hỏi thăm xem Server làm xong chưa
while True:
    try:
        req_history = urllib.request.Request(f"http://127.0.0.1:8188/history/{prompt_id}")
        resp_history = urllib.request.urlopen(req_history)
        history = json.loads(resp_history.read())
        
        if prompt_id in history:
            print("🎉 XỬ LÝ XONG! Video đã được lưu trong thư mục ComfyUI/output/")
            break
        else:
            time.sleep(2) # Đợi 2 giây rồi hỏi lại
    except:
        pass
