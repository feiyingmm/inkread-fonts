"""生成 fonts.json:size 与 sha256 必须与实际文件一致,应用下完会校验。

family 是 @font-face 里声明的**别名**,不必等于字体内部的家族名 —— 所以这里统一用
干净的名字(朱雀仿宋内部叫 "Zhuque Fangsong (technical preview)",别名取 "Zhuque Fangsong")。
"""
import hashlib
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

FONTS = [
    dict(id="noto-serif-sc", name="思源宋体", family="Noto Serif SC", category="serif",
         license="SIL OFL 1.1", source="https://github.com/notofonts/noto-cjk",
         desc="端庄的开源宋体,长文阅读最有书卷气"),
    dict(id="noto-sans-sc", name="思源黑体", family="Noto Sans SC", category="sans",
         license="SIL OFL 1.1", source="https://github.com/notofonts/noto-cjk",
         desc="覆盖最全的开源黑体,屏幕阅读最稳"),
    dict(id="sarasa-gothic-sc", name="更纱黑体", family="Sarasa Gothic SC", category="sans",
         license="SIL OFL 1.1", source="https://github.com/be5invis/Sarasa-Gothic",
         desc="等宽友好的黑体,中英混排与代码块都齐整"),
    dict(id="zhuque-fangsong", name="朱雀仿宋", family="Zhuque Fangsong", category="kai",
         license="SIL OFL 1.1", source="https://github.com/TrionesType/zhuque",
         desc="开源仿宋,笔记与古籍类内容的趣味选择"),
    dict(id="lxgw-wenkai-gb", name="霞鹜文楷 GB", family="LXGW WenKai GB", category="kai",
         license="SIL OFL 1.1", source="https://github.com/lxgw/LxgwWenKaiGB",
         desc="内置文楷的扩展字集版,生僻字更全"),
]

out = []
for f in FONTS:
    path = os.path.join(ROOT, f"{f['id']}.woff2")
    data = open(path, "rb").read()
    out.append({
        "id": f["id"], "name": f["name"], "family": f["family"],
        "file": f"{f['id']}.woff2", "size": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
        "license": f["license"], "source": f["source"],
        "category": f["category"], "desc": f["desc"],
    })

manifest = {"version": 1, "fonts": out}
with open(os.path.join(ROOT, "fonts.json"), "w", encoding="utf-8", newline="\n") as fp:
    json.dump(manifest, fp, ensure_ascii=False, indent=2)
    fp.write("\n")

total = sum(x["size"] for x in out)
for x in out:
    print(f"{x['id']:<18} {x['size']:>9,}  {x['sha256'][:16]}…  {x['family']}")
print(f"{'合计':<18} {total:>9,} ({total/1048576:.1f} MB)")
