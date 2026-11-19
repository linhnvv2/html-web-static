# Trang kế hoạch kiếm tiền công khai: quangvulinh.com/plan
# Sinh ra plan.html trong repo html-web-static (nguồn duy nhất). Không có đường dẫn máy, id thẻ kanban, tài khoản hay số liệu riêng.
from html import escape as E
from datetime import date

import os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "plan.html")  # sửa LANES/PLATFORMS/TODO rồi chạy: python tools/plan_page.py
UPDATED = date.today().strftime("%d/%m/%Y")

C = {"green": "#34d399", "violet": "#a78bfa", "teal": "#2dd4bf", "sky": "#38bdf8", "orange": "#fb923c",
     "amber": "#fbbf24", "rose": "#fb7185", "slate": "#94a3b8", "pink": "#f472b6", "lime": "#a3e635"}
FILL = {"green": "rgba(6,78,59,0.4)", "violet": "rgba(76,29,149,0.4)", "teal": "rgba(17,94,89,0.4)",
        "sky": "rgba(12,74,110,0.4)", "orange": "rgba(251,146,60,0.25)", "amber": "rgba(120,53,15,0.3)",
        "rose": "rgba(136,19,55,0.4)", "slate": "rgba(30,41,59,0.5)", "pink": "rgba(131,24,67,0.4)",
        "lime": "rgba(54,83,20,0.4)"}

# ---------------------------------------------------------------- 10 hướng
LANES = [
    dict(c="green", t=("PHIM CỔ TÍCH", "+ HOẠT HÌNH"), sub=("YouTube AdSense (YPP)", "kênh vL Kể Chuyện"),
         steps=[("Kịch bản", "đội phim + duyệt"), ("Vẽ ảnh", "Klein 3D + Qwen 2511"), ("Chuyển động", "Wan 2.2 · LTX-2.5"),
                ("Lồng tiếng + dựng", "VieNeu + FFmpeg"), ("Đăng", "CN + T4 19:00")],
         st=[("ĐANG CHẠY · ra tập đều", "green"), ("Wan Apache · LTX free <10tr USD", "green")]),
    dict(c="violet", t=("NHẠC AI", "(vL Ballad)"), sub=("YouTube + YT Music/Spotify", "kênh vL Ballad"),
         steps=[("Sáng tác", "HeartMuLa"), ("Sản xuất", "ACE-Step 1.5"), ("Đăng", "kênh vL Ballad")],
         st=[("GIẤY PHÉP OK · cần đăng đều để vào YPP", "amber"), ("ACE-Step MIT ✓ · HeartMuLa Apache ✓", "green")]),
    dict(c="teal", t=("BÁN GIỌNG ĐỌC", "(tts.quangvulinh.com)"), sub=("2.000đ / 1.000 ký tự", "gói 20k–200k"),
         steps=[("Thư viện giọng", "49–56 giọng hợp pháp"), ("Đọc", "VieNeu v3"), ("Web bán", "nghe thử · tải MP3"),
                ("Thanh toán", "VietQR chuyển khoản")],
         st=[("WEB CHẠY · chưa mở thanh toán", "amber"), ("Apache / CC0 ✓", "green")]),
    dict(c="sky", t=("FREELANCE", "WEB / APP / AI"), sub=("Fiverr · Upwork · Freelancer", "+ khách quen"), new=True,
         steps=[("Portfolio", "quangvulinh.com · 5 dự án"), ("Hồ sơ sàn", "Fiverr 2 gig + Upwork"),
                ("Nhận việc", "báo giá trọn gói"), ("Nhận tiền", "Payoneer / PayPal")],
         st=[("ĐÃ CÓ DỰ ÁN THẬT", "green"), ("Gig Fiverr chưa đăng", "amber")]),
    dict(c="pink", t=("VIDEO AI", "CHO SHOP VN"), sub=("300k–3tr / video", "nhóm FB · Zalo · shop quen"), new=True,
         steps=[("3 video mẫu", "cà phê · thời trang · spa"), ("Trang bảng giá", "+ form brief"),
                ("Chốt khách", "gói 10 video"), ("Giao + thu tiền", "chuyển khoản")],
         st=[("XẾP HẠNG #1 (ra tiền nhanh)", "amber"), ("Chưa làm mẫu", "slate")]),
    dict(c="lime", t=("SẢN PHẨM SỐ", "(Gumroad)"), sub=("Template · workflow · prompt", "trả VND về ngân hàng"), new=True,
         steps=[("Đóng gói", "template Expo · ComfyUI"), ("Đăng bán", "Gumroad / Lemon Squeezy"),
                ("Kéo khách", "Reddit · nhóm FB")],
         st=[("DỰ BỊ", "slate"), ("Chỉ bán phần Apache ✓", "green")]),
    dict(c="orange", t=("NGƯỜI ẢO", "BÁN HÀNG"), sub=("Video bán hàng / live", "video trước, live sau"),
         steps=[("Ảnh + video", "Qwen 2511 + Wan"), ("Lồng tiếng", "VieNeu"), ("Video 9:16 (A)", "bán hàng"),
                ("Live mặt nạ (B)", "MuseTalk + OBS")],
         st=[("BLOCKED (âm thanh ảo)", "rose"), ("Chỉ model thương mại ✓", "green")]),
    dict(c="amber", t=("TỔNG ĐÀI AI", "(onmi)"), sub=("Bán gói / dịch vụ CSKH", "onmi.quangvulinh.com"),
         steps=[("Thẻ nhân vật", "kịch bản CSKH"), ("Nghe", "Zipformer STT"), ("Trả lời", "LLM"),
                ("Nói", "VieNeu · WebRTC")],
         st=[("WEB CHẠY · còn việc chặn", "rose"), ("603 test đạt · cần QA cuối", "amber")]),
    dict(c="rose", t=("ANDROID APPS", "(Play Store)"), sub=("AdMob · bản Pro · affiliate", "Bé học chữ miễn phí"),
         steps=[("Build", "15+ app đã có APK"), ("Closed test", "14 ngày · 12+ người"), ("Play Console", "$25 + CCCD")],
         st=[("CHỜ GOM 14–15 GMAIL TEST", "amber"), ("Tốc Độ VN: dùng riêng", "slate")]),
    dict(c="slate", t=("LIVE TRANSLATE", "(ý tưởng)"), sub=("Web phiên dịch", "nói 2 chiều + đọc to"),
         steps=[("Nghe", "Whisper / Zipformer"), ("Dịch", "LLM local"), ("Đọc to", "VieNeu + TTS EN"),
                ("Web PWA", "điện thoại + PC")],
         st=[("Ý TƯỞNG · đã lên kế hoạch", "slate"), ("Làm sau phim", "slate")]),
]

LANE_H, TOP = 118, 58
svg = []
add = svg.append
for i, L in enumerate(LANES):
    y = TOP + i * LANE_H
    col, fill = C[L["c"]], FILL[L["c"]]
    add(f'<rect x="8" y="{y}" width="984" height="{LANE_H-10}" rx="10" fill="rgba(15,23,42,0.25)" stroke="{col}" stroke-opacity="0.25"/>')
    add(f'<rect x="15" y="{y+4}" width="175" height="{LANE_H-18}" rx="6" fill="{fill}" stroke="{col}" stroke-width="1.5"/>')
    add(f'<text x="102" y="{y+27}" fill="{col}" font-size="11" font-weight="700" text-anchor="middle">{E(L["t"][0])}</text>')
    add(f'<text x="102" y="{y+41}" fill="{col}" font-size="10" font-weight="700" text-anchor="middle">{E(L["t"][1])}</text>')
    add(f'<text x="102" y="{y+63}" fill="#b6c2cf" font-size="9" text-anchor="middle">{E(L["sub"][0])}</text>')
    add(f'<text x="102" y="{y+78}" fill="#b6c2cf" font-size="9" text-anchor="middle">{E(L["sub"][1])}</text>')
    if L.get("new"):
        add(f'<rect x="85" y="{y+86}" width="34" height="14" rx="7" fill="#22d3ee"/>'
            f'<text x="102" y="{y+96}" fill="#020617" font-size="8" font-weight="700" text-anchor="middle">MỚI</text>')
    n = len(L["steps"]); pitch = 569 / n; w = pitch - 14
    for k, (a, b) in enumerate(L["steps"]):
        x = 205 + k * pitch; cy = y + 30
        add(f'<rect x="{x:.1f}" y="{cy}" width="{w:.1f}" height="48" rx="6" fill="{fill}" stroke="{col}" stroke-width="1.5"/>')
        add(f'<text x="{x+w/2:.1f}" y="{cy+20}" fill="white" font-size="9.5" font-weight="600" text-anchor="middle">{E(a)}</text>')
        add(f'<text x="{x+w/2:.1f}" y="{cy+34}" fill="#b6c2cf" font-size="8" text-anchor="middle">{E(b)}</text>')
        if k < n - 1:
            add(f'<line x1="{x+w:.1f}" y1="{cy+24}" x2="{x+pitch:.1f}" y2="{cy+24}" stroke="{col}" stroke-width="1.5" marker-end="url(#ah)"/>')
    for k, (txt, sc) in enumerate(L["st"]):
        sy = y + 14 + k * 44
        add(f'<rect x="772" y="{sy}" width="213" height="32" rx="5" fill="rgba(15,23,42,0.6)" stroke="{C[sc]}" stroke-width="1.5"/>')
        add(f'<text x="878" y="{sy+20}" fill="{C[sc]}" font-size="8.5" font-weight="600" text-anchor="middle">{E(txt)}</text>')

yb = TOP + len(LANES) * LANE_H + 6
add(f'<rect x="15" y="{yb}" width="970" height="60" rx="10" fill="rgba(8,51,68,0.4)" stroke="#22d3ee" stroke-width="1.5"/>')
add(f'<text x="30" y="{yb+23}" fill="#22d3ee" font-size="12" font-weight="700">XƯƠNG SỐNG DÙNG CHUNG</text>')
add(f'<text x="30" y="{yb+43}" fill="#94a3b8" font-size="8.5">1 bộ công cụ gánh nhiều hướng</text>')
for k, t in enumerate(["ComfyUI (Klein · Wan · LTX)", "VieNeu + thư viện giọng", "LLM local", "Web + Cloudflare tunnel"]):
    x = 235 + k * 188
    add(f'<rect x="{x}" y="{yb+12}" width="178" height="36" rx="6" fill="rgba(15,23,42,0.5)" stroke="#22d3ee" stroke-width="1.5"/>')
    add(f'<text x="{x+89}" y="{yb+34}" fill="white" font-size="9" font-weight="600" text-anchor="middle">{E(t)}</text>')
yl = yb + 82
add(f'<text x="30" y="{yl}" fill="white" font-size="10" font-weight="600">CHÚ THÍCH</text>')
for k, (c, t) in enumerate([("green", "Đang chạy / giấy phép OK"), ("amber", "Chờ / cần kiểm"), ("rose", "Blocked"), ("slate", "Ý tưởng / dự bị")]):
    x = 100 + k * 170
    add(f'<rect x="{x}" y="{yl-9}" width="16" height="10" rx="2" fill="{FILL[c]}" stroke="{C[c]}"/>'
        f'<text x="{x+22}" y="{yl}" fill="#94a3b8" font-size="8.5">{E(t)}</text>')
add(f'<rect x="780" y="{yl-10}" width="30" height="12" rx="6" fill="#22d3ee"/><text x="795" y="{yl-1}" fill="#020617" font-size="7.5" font-weight="700" text-anchor="middle">MỚI</text>'
    f'<text x="816" y="{yl}" fill="#94a3b8" font-size="8.5">thêm 18/11</text>')
H = yl + 16
head = f'''<rect x="15" y="8" width="430" height="34" rx="6" fill="rgba(8,51,68,0.4)" stroke="#22d3ee" stroke-width="1.5"/>
<text x="230" y="30" fill="#22d3ee" font-size="10.5" font-weight="600" text-anchor="middle">MỐC: 2 kênh YouTube đạt YPP trước 01/02/2027</text>
<rect x="455" y="8" width="120" height="34" rx="6" fill="rgba(15,23,42,0.5)" stroke="#34d399" stroke-width="1.5"/>
<text x="515" y="30" fill="#34d399" font-size="11" font-weight="600" text-anchor="middle">{len(LANES)} HƯỚNG</text>
<rect x="585" y="8" width="185" height="34" rx="6" fill="rgba(15,23,42,0.5)" stroke="#2dd4bf" stroke-width="1.5"/>
<text x="677" y="30" fill="#2dd4bf" font-size="10" font-weight="600" text-anchor="middle">3 WEB ĐANG CHẠY</text>
<rect x="780" y="8" width="205" height="34" rx="6" fill="rgba(15,23,42,0.5)" stroke="#fb7185" stroke-width="1.5"/>
<text x="882" y="30" fill="#fb7185" font-size="10" font-weight="600" text-anchor="middle">1 GPU · phim ưu tiên</text>'''

# ---------------------------------------------------------------- nền tảng để đăng
# (tên, loại, dùng để, phí / nhận tiền, trạng thái, màu)
PLATFORMS = [
    ("YouTube (YPP)", "Kênh video", "Phim cổ tích, hoạt hình, nhạc", "Chia sẻ doanh thu quảng cáo; cần đủ giờ xem + sub", "Đang đăng", "green"),
    ("tts.quangvulinh.com", "Web của mình", "Bán ký tự đọc giọng Việt", "VietQR thẳng về ngân hàng, không mất phí sàn", "Chạy · chờ mở thanh toán", "amber"),
    ("Nhóm Facebook / Zalo", "Bán trực tiếp", "Video AI cho shop, chatbot, web", "Chuyển khoản trực tiếp, 0% phí sàn", "Chưa đăng bài chào", "amber"),
    ("Fiverr", "Sàn freelance (gig)", "Gig 1: AI automation / AI agent · Gig 2: YouTube automation", "Phí 20%; rút về Payoneer/PayPal; giữ tiền 14 ngày", "Có tài khoản · đang tạo hồ sơ", "amber"),
    ("Upwork", "Sàn freelance (chào giá)", "Dựng workflow ComfyUI, pipeline AI, web/app", "15–45 USD/giờ; dự án 800–2.500 USD", "Có tài khoản · đang tạo hồ sơ", "amber"),
    ("Freelancer.com", "Sàn freelance (chào giá)", "Dự án pipeline video AI", "Đông người chào giá (vd 98 người/1 việc)", "Có tài khoản · đã chọn 13 kỹ năng", "amber"),
    ("Gumroad / Lemon Squeezy", "Bán sản phẩm số", "Template app Expo, workflow ComfyUI, gói prompt", "Gumroad 10% + 0,5 USD, trả VND về ngân hàng (≥100 USD)", "Dự bị", "slate"),
    ("Google Play", "Chợ ứng dụng", "15+ app Android, Bé học chữ", "Phí 25 USD một lần; Google khấu trừ 5% thuế", "Chờ closed test", "amber"),
    ("Shopee Affiliate", "Hoa hồng", "Gắn link vào app người lớn + kênh", "Mẹ & Bé ~9,4% khách mới, tối đa 70k/đơn", "Chưa đăng ký", "slate"),
    ("Magnific (Freepik) · Zedge · Amazon KDP", "Kho nội dung", "Ảnh/vector AI, hình nền, nhạc chuông, sách tô màu", "Thu nhập thấp, chậm; chỉ dùng model Apache", "Để sau", "slate"),
]
DROPPED = [
    ("Adobe Stock", "13/20 ảnh hỏng + model phi thương mại"),
    ("Etsy", "không hỗ trợ người bán ở Việt Nam"),
    ("Envato", "ngừng nhận tác giả mới từ 25/09/2026, không nhận AI"),
    ("TikTok Creator Rewards", "không có ở Việt Nam → TikTok chỉ để kéo khách"),
    ("Facebook Content Monetization", "Việt Nam không có trong danh sách chính thức"),
]

# ---------------------------------------------------------------- việc cần làm (ai làm)
TODO = [
    ("Bán giọng đọc", "Điền tài khoản ngân hàng để mở VietQR", "Anh", True),
    ("Bán giọng đọc", "Khởi động lại web, kiểm mã QR + 1 đơn thử", "Em", False),
    ("Freelance", "Gửi tên đúng CCCD + ảnh thật để hoàn tất hồ sơ; sau này mở Payoneer + xác minh CCCD", "Anh", True),
    ("Freelance", "Viết nội dung 2 gig (tiêu đề, mô tả, giá, tag, FAQ) bằng tiếng Anh", "Em", False),
    ("Freelance", "Hồ sơ Upwork dựa trên portfolio 5 dự án", "Em", False),
    ("Video cho shop", "Làm 3 video mẫu 9:16 (cà phê, thời trang, spa) bằng model thương mại", "Em", False),
    ("Video cho shop", "Trang bảng giá + form brief; bài chào cho nhóm FB/Zalo", "Em", False),
    ("Video cho shop", "Đăng bài chào + nhắn shop quen, chốt khách đầu", "Anh", True),
    ("YouTube", "Giữ lịch CN + T4 19:00; theo dõi giờ xem để vào YPP", "Em", False),
    ("Nhạc AI", "Tự sửa lời + giữ file dự án làm bằng chứng sáng tác; tick khai báo AI khi đăng", "Em", False),
    ("Android", "Gom 14–15 Gmail người test, đăng ký Play Console (25 USD)", "Anh", True),
    ("Tổng đài onmi", "Gỡ các việc đang chặn, QA cuối trước khi chào bán", "Em", False),
    ("Người ảo", "Cài driver âm thanh ảo (cần anh bấm quyền admin)", "Anh", True),
    ("Live Translate", "Làm sau khi xong đợt phim", "Em", False),
]

DOT = {"green": "#34d399", "amber": "#fbbf24", "rose": "#fb7185", "slate": "#94a3b8"}

def lane_card(L):
    col = C[L["c"]]
    new = '<span class="new">MỚI</span>' if L.get("new") else ""
    pills = "".join(f'<span class="pill" style="--c:{C[c]}">{E(t)}</span>' for t, c in L["st"])
    steps = "".join(f'<li><b>{E(a)}</b><span>{E(b)}</span></li>' for a, b in L["steps"])
    return (f'<details class="lane" style="--c:{col};--f:{FILL[L["c"]]}"><summary>'
            f'<span class="lt">{E(L["t"][0])} {E(L["t"][1])}{new}</span>'
            f'<span class="ls">{E(L["sub"][0])} · {E(L["sub"][1])}</span>'
            f'<span class="lp">{pills}</span></summary><ol class="steps">{steps}</ol></details>')
lanes_m = "\n".join(lane_card(L) for L in LANES)
plat_rows = "\n".join(
    f'<tr><td class="pn"><b>{E(n)}</b><span class="k">{E(k)}</span></td><td data-l="Dùng để">{E(u)}</td><td data-l="Phí · nhận tiền">{E(f)}</td>'
    f'<td class="ps"><span class="pill" style="--c:{DOT[c]}">{E(s)}</span></td></tr>' for n, k, u, f, s, c in PLATFORMS)
drop_li = "".join(f"<li><b>{E(n)}</b>: {E(w)}</li>" for n, w in DROPPED)
todo_li = "\n".join(
    f'<li class="{"me" if who == "Anh" else ""}"><span class="tag">{E(g)}</span><span class="txt">{E(t)}</span>'
    f'<span class="who {"a" if who == "Anh" else "e"}">{E(who)}</span></li>' for g, t, who, _ in TODO)
n_anh = sum(1 for t in TODO if t[2] == "Anh")

html = f'''<!DOCTYPE html>
<html lang="vi"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex, nofollow">
<title>Plan — kế hoạch kiếm tiền · quangvulinh.com</title>
<link rel="icon" href="assets/img/favicon.png">
<style>
* {{ margin:0; padding:0; box-sizing:border-box; }}
body {{ font-family: 'JetBrains Mono', Consolas, ui-monospace, monospace; background:#020617; padding:1.5rem; color:#e2e8f0; }}
.container {{ max-width:1400px; margin:0 auto; }}
.header-row {{ display:flex; align-items:center; gap:.8rem; margin-bottom:.4rem; flex-wrap:wrap; }}
.pulse-dot {{ width:12px; height:12px; background:#22d3ee; border-radius:50%; box-shadow:0 0 12px #22d3ee; }}
h1 {{ font-size:1.5rem; font-weight:700; color:white; }}
h2 {{ font-size:1.05rem; color:white; margin:2rem 0 .8rem; display:flex; align-items:center; gap:.5rem; }}
h2::before {{ content:""; width:4px; height:1.1em; background:#22d3ee; border-radius:2px; }}
.subtitle {{ color:#94a3b8; font-size:.82rem; }}
.nav {{ display:flex; gap:.5rem; flex-wrap:wrap; margin:.9rem 0 1.2rem; }}
.nav a {{ color:#22d3ee; text-decoration:none; font-size:.78rem; border:1px solid #164e63; padding:.3rem .7rem; border-radius:99px; }}
.nav a:hover {{ background:#083344; }}
.panel {{ background:rgba(15,23,42,.5); border-radius:1rem; border:1px solid #1e293b; padding:1rem; overflow-x:auto; }}
svg {{ width:100%; min-width:900px; display:block; }}
table {{ width:100%; border-collapse:collapse; font-size:.78rem; min-width:760px; }}
th {{ text-align:left; color:#94a3b8; font-weight:600; padding:.55rem .6rem; border-bottom:1px solid #1e293b; }}
td {{ padding:.6rem; border-bottom:1px solid #111a2e; vertical-align:top; color:#cbd5e1; line-height:1.45; }}
td b {{ color:white; display:block; }} td .k {{ color:#94a3b8; font-size:.72rem; }}
.pill {{ display:inline-block; white-space:nowrap; font-size:.7rem; padding:.15rem .55rem; border-radius:99px; color:var(--c); border:1px solid var(--c); }}
.todo {{ list-style:none; display:grid; grid-template-columns:repeat(auto-fill,minmax(520px,1fr)); gap:.5rem; }}
.todo li {{ display:flex; align-items:center; gap:.6rem; background:rgba(15,23,42,.5); border:1px solid #1e293b; border-radius:.6rem; padding:.55rem .7rem; font-size:.78rem; }}
.todo li.me {{ border-color:#7c2d12; }}
.todo .tag {{ flex:none; width:7.5rem; color:#a5b4c3; font-size:.72rem; }}
.todo .txt {{ flex:1; color:#e2e8f0; line-height:1.4; }}
.who {{ flex:none; font-size:.68rem; font-weight:700; padding:.12rem .5rem; border-radius:99px; }}
.who.a {{ background:#fb923c; color:#1c0a00; }} .who.e {{ background:#164e63; color:#a5f3fc; }}
.cards {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(280px,1fr)); gap:1rem; }}
.card {{ background:rgba(15,23,42,.5); border-radius:.75rem; border:1px solid #1e293b; padding:1rem; }}
.card h3 {{ font-size:.85rem; margin-bottom:.6rem; color:white; }}
.card ul {{ list-style:none; color:#94a3b8; font-size:.75rem; }} .card li {{ margin-bottom:.45rem; line-height:1.4; }}
.card li b {{ color:#e2e8f0; }}
.footer {{ text-align:center; margin-top:2rem; color:#8696a8; font-size:.75rem; }}
.footer a {{ color:#64748b; }}
.lanes {{ display:none; }}
.who-legend {{ margin:-.3rem 0 .7rem; }}
.top {{ position:fixed; right:1rem; bottom:1rem; width:2.6rem; height:2.6rem; border-radius:50%; background:#0e7490; color:white; display:none; align-items:center; justify-content:center; text-decoration:none; font-size:1.1rem; box-shadow:0 4px 14px rgba(0,0,0,.5); }}
@media (max-width:760px) {{
  body {{ padding:0 .75rem 4rem; font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif; font-size:15px; }}
  h1 {{ font-size:1.3rem; }} .header-row {{ padding-top:1rem; }}
  h2 {{ font-size:1.1rem; margin:1.6rem 0 .7rem; scroll-margin-top:3.6rem; }}
  .subtitle {{ font-size:.85rem; }}
  .nav {{ position:sticky; top:0; z-index:5; margin:.8rem -.75rem 0; padding:.55rem .75rem; background:rgba(2,6,23,.94); backdrop-filter:blur(6px);
         flex-wrap:nowrap; overflow-x:auto; scrollbar-width:none; border-bottom:1px solid #1e293b; }}
  .nav::-webkit-scrollbar {{ display:none; }}
  .nav a {{ flex:none; font-size:.85rem; padding:.4rem .8rem; }}
  .top {{ display:flex; width:2.2rem; height:2.2rem; right:.6rem; bottom:.8rem; font-size:.95rem; opacity:.75; }}
  .container {{ padding-bottom:3rem; }}
  .nav {{ -webkit-mask-image:linear-gradient(90deg,#000 85%,transparent); mask-image:linear-gradient(90deg,#000 85%,transparent); }}
  /* sơ đồ → thẻ dọc */
  #tranh + .panel {{ display:none; }}
  .lanes {{ display:grid; gap:.6rem; }}
  .lane {{ border:1px solid var(--c); border-left-width:4px; border-radius:.7rem; background:rgba(15,23,42,.6); }}
  .lane summary {{ list-style:none; cursor:pointer; padding:.7rem .75rem; display:grid; gap:.35rem; }}
  .lane summary::-webkit-details-marker {{ display:none; }}
  .lane summary::after {{ content:"Xem các bước ▾"; font-size:.8rem; color:#7dd3fc; padding-top:.15rem; }}
  .lane[open] summary::after {{ content:"Thu gọn ▴"; }}
  .lt {{ color:var(--c); font-weight:700; font-size:1rem; display:flex; align-items:center; gap:.5rem; flex-wrap:wrap; }}
  .new {{ background:#22d3ee; color:#020617; font-size:.65rem; padding:.05rem .45rem; border-radius:99px; }}
  .ls {{ color:#b6c2cf; font-size:.85rem; }}
  .lp {{ display:flex; flex-wrap:wrap; gap:.35rem; }}
  .lp .pill, td .pill {{ white-space:normal; font-size:.75rem; padding:.2rem .6rem; }}
  .steps {{ list-style:none; counter-reset:s; margin:0 .6rem .7rem; border-top:1px dashed #1e293b; padding-top:.6rem; display:grid; gap:.4rem; }}
  .steps li {{ counter-increment:s; display:grid; grid-template-columns:1.6rem 1fr; column-gap:.4rem; background:var(--f); border-radius:.5rem; padding:.45rem .6rem; }}
  .steps li::before {{ content:counter(s); grid-row:span 2; width:1.4rem; height:1.4rem; border-radius:50%; border:1px solid var(--c); color:var(--c); font-size:.75rem; display:flex; align-items:center; justify-content:center; }}
  .steps b {{ color:white; font-size:.9rem; }} .steps span {{ color:#b6c2cf; font-size:.8rem; }}
  /* việc cần làm */
  .todo {{ grid-template-columns:1fr; }}
  .todo li {{ flex-wrap:wrap; font-size:.9rem; padding:.65rem .75rem; row-gap:.3rem; }}
  .todo .tag {{ width:auto; font-size:.78rem; color:#cbd5e1; font-weight:600; }}
  .who.e {{ background:#0e7490; color:#ecfeff; }} .todo .who {{ margin-left:auto; font-size:.72rem; }}
  .todo .txt {{ flex-basis:100%; order:2; }}
  /* bảng → thẻ */
  #nentang + .panel {{ padding:0; background:none; border:0; overflow:visible; }}
  table, tbody, tr, td {{ display:block; min-width:0; width:100%; }}
  thead {{ display:none; }}
  tr {{ background:rgba(15,23,42,.6); border:1px solid #1e293b; border-radius:.7rem; padding:.7rem .8rem; margin-bottom:.6rem; }}
  td {{ border:0; padding:.2rem 0; font-size:.88rem; }}
  td.pn {{ display:flex; align-items:baseline; justify-content:space-between; gap:.5rem; flex-wrap:wrap; padding-bottom:.35rem; }}
  td.pn b {{ display:inline; font-size:.98rem; }}
  td[data-l]::before {{ content:attr(data-l); display:block; color:#7dd3fc; font-size:.72rem; margin-bottom:.05rem; }}
  td.ps {{ padding-top:.45rem; }}
  .card ul {{ font-size:.88rem; color:#b6c2cf; }} .card h3 {{ font-size:.98rem; }}
  .footer {{ font-size:.78rem; }}
}}
</style></head><body><div class="container">
<div class="header-row"><div class="pulse-dot"></div><h1 id="dau">Plan — kế hoạch kiếm tiền</h1></div>
<p class="subtitle">{len(LANES)} hướng · {len(PLATFORMS)} nền tảng · {len(TODO)} việc cần làm • cập nhật {UPDATED}</p>
<nav class="nav"><a href="#tranh">Bức tranh</a><a href="#viec">Việc cần làm</a><a href="#nentang">Nền tảng để đăng</a><a href="#links">Link freelance</a><a href="#ghichu">Rào cản &amp; đã loại</a><a href="/">← quangvulinh.com</a></nav>

<h2 id="tranh">Bức tranh {len(LANES)} hướng</h2>
<div class="panel"><svg viewBox="0 0 1000 {H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Sơ đồ {len(LANES)} hướng kiếm tiền">
<defs><marker id="ah" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto"><polygon points="0 0, 8 3, 0 6" fill="#64748b"/></marker></defs>
{head}
{chr(10).join(svg)}
</svg></div>
<div class="lanes">
{lanes_m}
</div>

<h2 id="viec">Việc cần làm tiếp</h2>
<p class="subtitle who-legend"><span class="who a">Anh</span> = chính chủ làm ({n_anh} việc: tài khoản, CCCD, ngân hàng, quyền admin) · <span class="who e">Em</span> = agent làm được</p>
<ul class="todo">
{todo_li}
</ul>

<h2 id="nentang">Nền tảng để đăng / bán</h2>
<div class="panel"><table>
<thead><tr><th>Nền tảng</th><th>Dùng để</th><th>Phí · nhận tiền</th><th>Trạng thái</th></tr></thead>
<tbody>
{plat_rows}
</tbody></table></div>

<h2 id="links">Link theo dõi freelance</h2>
<div class="cards">
<div class="card"><h3>Mở nhanh</h3><ul>
<li>• <a href="https://www.fiverr.com/users/me/seller_dashboard" target="_blank" rel="noopener" style="color:#7dd3fc">Fiverr — Seller dashboard</a></li>
<li>• <a href="https://www.upwork.com/nx/find-work/" target="_blank" rel="noopener" style="color:#7dd3fc">Upwork — Find work</a></li>
<li>• <a href="https://www.freelancer.com/dashboard" target="_blank" rel="noopener" style="color:#7dd3fc">Freelancer — Dashboard</a></li>
<li>• Agent tự kiểm tin nhắn / đơn / duyệt hồ sơ lúc 9:00 và 20:00 mỗi ngày, báo qua Telegram</li></ul></div>
</div>

<h2 id="ghichu">Rào cản &amp; đã loại</h2>
<div class="cards">
<div class="card"><h3>Ra tiền gần nhất</h3><ul>
<li>• <b>Bán giọng đọc</b>: web đã chạy, chỉ thiếu tài khoản ngân hàng để mở VietQR</li>
<li>• <b>Video AI cho shop VN</b>: giá thị trường 300k–3tr/video, có tiền trong 1–3 tuần</li>
<li>• <b>Freelance</b>: đã có dự án thật (web du lịch + CMS, biên bản họp AI) làm portfolio</li></ul></div>
<div class="card"><h3>Rào cản chung</h3><ul>
<li>• <b>Giấy phép</b>: không dùng viXTTS, Qwen-Image 2.1, MiniMax H3, HunyuanVideo cho việc kiếm tiền</li>
<li>• <b>TikTok Shop</b> cấm giọng AI trong live (06/2026)</li>
<li>• <b>1 GPU</b>: phim, nhạc, tổng đài, live translate không chạy song song</li>
<li>• Ngưỡng YPP dự kiến tăng từ 01/02/2027</li>
<li>• Nhạc AI: model cho dùng thương mại, nhưng nhạc AI thuần có thể không được bảo hộ bản quyền → không đăng ký Content ID</li></ul></div>
<div class="card"><h3>Đã loại</h3><ul>{drop_li}</ul></div>
</div>

<p class="footer">quangvulinh.com/plan • kế hoạch cá nhân, cập nhật {UPDATED} • số liệu phí/giá tra từ trang chính thức của từng nền tảng 10/2026</p>
</div><a class="top" href="#dau" aria-label="Lên đầu trang">↑</a></body></html>'''
open(OUT, "w", encoding="utf-8", newline="\n").write(html)
print(OUT, H, len(html))
