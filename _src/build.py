"""把源字体转成 woff2,并从字体内部 name 表读出权威的家族名与许可证声明。

官方 WOFF2 原样复制；TTF/OTF 仅压缩，不改字形、名称或授权。
清单 family 可作为 @font-face 别名，内部家族名在这里打印供核对。
"""
import os
import sys
import shutil
from fontTools.ttLib import woff2
from fontTools.ttLib import TTFont

# (输出 id, 展示名, 源文件, 分类, 描述, 来源)
JOBS = [
    ("noto-serif-sc", "思源宋体", "NotoSerifSC-Regular.otf", "serif",
     "端庄的开源宋体,长文阅读最有书卷气", "https://github.com/notofonts/noto-cjk"),
    ("noto-sans-sc", "思源黑体", "NotoSansSC-Regular.otf", "sans",
     "覆盖最全的开源黑体,屏幕阅读最稳", "https://github.com/notofonts/noto-cjk"),
    ("sarasa-gothic-sc", "更纱黑体", "sarasa/SarasaGothicSC-Regular.ttf", "sans",
     "等宽友好的黑体,中英混排和代码块都齐整", "https://github.com/be5invis/Sarasa-Gothic"),
    ("zhuque-fangsong", "朱雀仿宋", "zhuque/ZhuqueFangsong-Regular.ttf", "kai",
     "开源仿宋,笔记与古籍类内容的趣味选择", "https://github.com/TrionesType/zhuque"),
    ("lxgw-wenkai-gb", "霞鹜文楷 GB", "LXGWWenKaiGB-Regular.ttf", "kai",
     "内置文楷的扩展字集版,生僻字更全", "https://github.com/lxgw/LxgwWenKaiGB"),
    ("ibm-plex-sans-sc", "IBM Plex Sans SC", "IBMPlexSansSC-Regular.woff2", "sans",
     "有辨识度的中文黑体，适合技术文档；仅常规字重", "https://github.com/IBM/plex"),
    ("yozai", "悠哉", "Yozai-Regular.ttf", "kai",
     "轻松的手写风格，部分汉字由 AI 补齐；仅常规字重", "https://github.com/lxgw/yozai-font"),
    ("literata", "Literata", "Literata-Regular.woff2", "serif",
     "适合西文长篇阅读的衬线字体，中文使用回退字体；仅常规字重", "https://github.com/googlefonts/literata"),
    ("jetbrains-mono", "JetBrains Mono", "JetBrainsMono-Regular.woff2", "mono",
     "代码用西文等宽字体，中文需等宽回退；仅常规字重", "https://github.com/JetBrains/JetBrainsMono"),
]


def name_of(font, *ids):
    """按优先级取 name 表里第一个非空记录"""
    for nid in ids:
        for rec in font["name"].names:
            if rec.nameID == nid:
                try:
                    v = rec.toUnicode().strip()
                except Exception:
                    continue
                if v:
                    return v
    return ""


out_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rows = []
for fid, label, src, category, desc, source in JOBS:
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), src)
    if not os.path.exists(src):
        print(f"!! 缺源文件 {src}", file=sys.stderr)
        continue
    font = TTFont(src, lazy=False)
    # 16 = Typographic Family(优先),1 = Family
    family = name_of(font, 16, 1)
    lic = name_of(font, 13)
    lic_url = name_of(font, 14)
    dst = os.path.join(out_dir, f"{fid}.woff2")
    if src.lower().endswith(".woff2"):
        shutil.copyfile(src, dst)
    else:
        # 禁用表预处理并保留时间戳，仅作 WOFF2 无损压缩，避免改动保留名称字体。
        woff2.compress(src, dst, transform_tables=set())
    font.close()
    rows.append(
        dict(id=fid, name=label, family=family, file=f"{fid}.woff2",
             size=os.path.getsize(dst), src_size=os.path.getsize(src),
             category=category, desc=desc, source=source,
             license_raw=lic[:160], license_url=lic_url)
    )

for r in rows:
    print(f"[{r['id']}]")
    print(f"  family      = {r['family']}")
    print(f"  {r['src_size']:>10,} -> {r['size']:>10,}  ({r['size']/1048576:.1f} MB)")
    print(f"  license     = {r['license_raw']}")
    print(f"  license_url = {r['license_url']}")
    print()
