# inkread-fonts

[墨阅 (inkread)](https://github.com/feiyingmm/inkread) 的**可下载字体扩展**托管仓库。

中文字体动辄 10MB 上下，全塞进安装包不现实，所以墨阅只内置霞鹜文楷保底，其余放在这里按需下载。
应用读取根目录的 [`fonts.json`](fonts.json) 得到清单，用户在「设置 → 阅读」的正文或代码字体入口按需下载启用。
本次字体目录发布为 `v2`；现有 `v1` 下载目录保持原样。

**本仓库不含任何原创字体作品**，采用上游官方 WOFF2，或将官方 TTF/OTF 无损压缩为 WOFF2 后重新分发；
每款字体的授权原文见 [`licenses/`](licenses/)，版权归各自作者所有。

## 字体清单

全部为 **SIL Open Font License 1.1**，允许自由使用、修改与再分发（含商业用途）。

| 字体 | family | 大小 | 分类 | 上游 |
|------|--------|------|------|------|
| 思源宋体 | `Noto Serif SC` | 8.0 MB | 宋体 | [notofonts/noto-cjk](https://github.com/notofonts/noto-cjk) |
| 思源黑体 | `Noto Sans SC` | 5.8 MB | 黑体 | [notofonts/noto-cjk](https://github.com/notofonts/noto-cjk) |
| 更纱黑体 | `Sarasa Gothic SC` | 8.0 MB | 黑体 | [be5invis/Sarasa-Gothic](https://github.com/be5invis/Sarasa-Gothic) |
| 朱雀仿宋 | `Zhuque Fangsong` | 4.6 MB | 仿宋 | [TrionesType/zhuque](https://github.com/TrionesType/zhuque) |
| 霞鹜文楷 GB | `LXGW WenKai GB` | 7.6 MB | 楷体 | [lxgw/LxgwWenKaiGB](https://github.com/lxgw/LxgwWenKaiGB) |
| IBM Plex Sans SC | `IBM Plex Sans SC` | 3.64 MiB | 黑体 | [IBM/plex](https://github.com/IBM/plex) |
| 悠哉 | `Yozai` | 7.84 MiB | 手写/楷体 | [lxgw/yozai-font](https://github.com/lxgw/yozai-font) |
| Literata | `Literata` | 95.2 KiB | 西文衬线 | [googlefonts/literata](https://github.com/googlefonts/literata) |
| JetBrains Mono | `JetBrains Mono` | 90.2 KiB | 西文等宽 | [JetBrains/JetBrainsMono](https://github.com/JetBrains/JetBrainsMono) |

均为 **Regular 单字重**，没有独立 Bold/Italic 文件；粗体和斜体由应用/浏览器合成。
新增 IBM Plex Sans SC 适合中文技术文档；悠哉为手写风格，上游自 0.860 起采用 AI 补全部分汉字，部分字形仍可能沿用日本写法。
Literata 面向西文长文，中文需现有字体回退；JetBrains Mono 面向代码与配置，中文需等宽字体回退，不能视为完整中文字库。
实际字节数和 SHA256 以 [`fonts.json`](fonts.json) 为准。

### 为什么没收录某些常见字体

- **霞鹜新晰黑 LXGW Neo XiHei** —— 衍生自 IPAex Gothic，用的是 **IPA Font License 1.0 而非 OFL**。
  作者明确提示「涉及字体文件再分发的嵌入式应用需满足 IPA 许可的限制条件，请自行评估合规成本」，
  故本仓库不收。
- **汇文明朝体 / 京华老宋体** —— 授权条款未能核实到权威原文，按「拿不准就不上架」处理。

## 取用地址

本次字体目录读取 `v2` tag，旧客户端固定的 `v1` 保持可用；主源走 jsDelivr、超时自动切 GitHub raw：

```text
https://cdn.jsdelivr.net/gh/feiyingmm/inkread-fonts@v2/fonts.json
https://raw.githubusercontent.com/feiyingmm/inkread-fonts/v2/fonts.json
```

## 约束

- ⚠️ **jsDelivr 单文件上限 20MB**，新增字体转完 woff2 后必须低于此值
- ⚠️ `fonts.json` 里的 `size` 与 `sha256` **必须与实际文件一致** —— 应用下载完会校验，
  不符会直接删除文件并报错（半截字体装上去正文会变成一片豆腐块，比下载失败更难查）
- `family` 是 `@font-face` 里声明的**别名**，不必等于字体内部的家族名

## 更新字体清单

`_src/build.py` 与 `_src/manifest.py` 已入库；源字体及解包产物不入库。
源文件按下表放入 `_src/`，许可全文原样保存在 `licenses/`。官方 WOFF2 只复制，不重新编码；悠哉仅作 WOFF2 无损压缩，不裁剪字符或修改名称、字形与授权。

| 字体 | 固定上游修订 | 官方源文件 → `_src/` 文件名 | 本地许可（取自同一修订） |
|---|---|---|---|
| IBM Plex Sans SC | `71f558992315a12ca1f06a2215d57962a1992162` | [官方 WOFF2](https://raw.githubusercontent.com/IBM/plex/71f558992315a12ca1f06a2215d57962a1992162/packages/plex-sans-sc/fonts/complete/woff2/hinted/IBMPlexSansSC-Regular.woff2) → `IBMPlexSansSC-Regular.woff2` | [ibm-plex-sans-sc.txt](licenses/ibm-plex-sans-sc.txt)，上游 `packages/plex-sans-sc/LICENSE.txt` |
| 悠哉 | `v0.868` / `90a91ca019faad7b7dae885a4f70a44359021333` | [官方发布附件](https://github.com/lxgw/yozai-font/releases/download/v0.868/Yozai-Regular.ttf) → `Yozai-Regular.ttf` | [yozai.txt](licenses/yozai.txt)，上游 `OFL.txt` |
| Literata | `0c2761b727a1b3a7cffd313c37f0f5163dfc7a63` | [官方 WOFF2](https://raw.githubusercontent.com/googlefonts/literata/0c2761b727a1b3a7cffd313c37f0f5163dfc7a63/fonts/webfonts/Literata-Regular.woff2) → `Literata-Regular.woff2` | [literata.txt](licenses/literata.txt)，上游 `OFL.txt` |
| JetBrains Mono | `19371302b95d218af43299bce79ddbddd0bc364d` | [官方 WOFF2](https://raw.githubusercontent.com/JetBrains/JetBrainsMono/19371302b95d218af43299bce79ddbddd0bc364d/fonts/webfonts/JetBrainsMono-Regular.woff2) → `JetBrainsMono-Regular.woff2` | [jetbrains-mono.txt](licenses/jetbrains-mono.txt)，上游 `OFL.txt` |

悠哉原始 TTF 为 15,605,374 字节，SHA256 为 `25071998a0fe6a72f54c235e714986d259633e5ff670b1a2b5e264387f3316ac`，已与官方发布页校对。
转换使用 fontTools 4.64.0、Brotli 1.2.0；禁用表预处理并保留时间戳，压缩后核对字体表、名称、字符映射及字形数据。
悠哉各表原始字节保持一致，唯 `head` 表按 [WOFF2 规范](https://www.w3.org/TR/WOFF2/) 设置无损压缩标志 bit 11 并重算校验值，名称、字形与授权表不变。
仅作无损 WOFF2 封装时保留名称，遵循 [OFL FAQ 2.2/2.2.1](https://openfontlicense.org/ofl-faq/)；后续若修改字形、子集或元数据，须重新核对保留名称条件。

在仓库根目录运行（Python 需已有 fontTools 和 Brotli）。旧五款源文件不在当前检出时，构建脚本会提示缺源并跳过，保留已有 WOFF2：

```powershell
# 官方 WOFF2 原样复制；TTF/OTF 压缩为 WOFF2，并打印内部家族名和授权声明。
python _src/build.py
# 重算全部已登记字体的真实字节数与 SHA256，更新 fonts.json。
python _src/manifest.py
```

## 发布边界

字体资源通过仓库内文件及 `v2` tag 分发，不覆盖 `v1`；不另上传字体 Release 附件。
本次经用户授权，将完整任务分支合入主线并发布 `v2` tag；应用双源使用 `v2`，须核实 CDN/raw 清单与资产哈希。字体资源和应用安装包分别发布。
清单的 `version: 1` 是现有格式版本，不等于资源发布 tag。
jsDelivr 按 tag 缓存，禁止 force push 覆盖已发布 tag。
