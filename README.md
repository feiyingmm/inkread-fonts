# inkread-fonts

[墨阅 (inkread)](https://github.com/feiyingmm/inkread) 的**可下载字体扩展**托管仓库。

中文字体动辄 10MB 上下，全塞进安装包不现实，所以墨阅只内置霞鹜文楷保底，其余放在这里按需下载。
应用读取根目录的 [`fonts.json`](fonts.json) 得到清单，用户在「设置 → 阅读 → 正文字体」里点一下即可下载启用。

**本仓库不含任何原创字体作品**，只是把上游作者发布的开源字体转成 woff2 后重新分发；
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

均为 Regular 单字重，源文件转 woff2（体积约为原始 TTF/OTF 的 1/3）。

### 为什么没收录某些常见字体

- **霞鹜新晰黑 LXGW Neo XiHei** —— 衍生自 IPAex Gothic，用的是 **IPA Font License 1.0 而非 OFL**。
  作者明确提示「涉及字体文件再分发的嵌入式应用需满足 IPA 许可的限制条件，请自行评估合规成本」，
  故本仓库不收。
- **汇文明朝体 / 京华老宋体** —— 授权条款未能核实到权威原文，按「拿不准就不上架」处理。

## 取用地址

应用侧写死了 `v1` 这个 tag，主源走 jsDelivr、超时自动切 GitHub raw：

```
https://cdn.jsdelivr.net/gh/feiyingmm/inkread-fonts@v1/fonts.json
https://raw.githubusercontent.com/feiyingmm/inkread-fonts/v1/fonts.json
```

## 约束

- ⚠️ **jsDelivr 单文件上限 20MB**，新增字体转完 woff2 后必须低于此值
- ⚠️ `fonts.json` 里的 `size` 与 `sha256` **必须与实际文件一致** —— 应用下载完会校验，
  不符会直接删除文件并报错（半截字体装上去正文会变成一片豆腐块，比下载失败更难查）
- `family` 是 `@font-face` 里声明的**别名**，不必等于字体内部的家族名

## 更新字体清单

`_src/`（不入库）放源字体与两个脚本：

```bash
python _src/build.py      # 源字体 -> woff2，并打印字体内部的 family 与授权声明
python _src/manifest.py   # 重算 size / sha256，生成 fonts.json
```

改完之后**建议打新 tag 并同步改应用里的 `SOURCES`**（`src-tauri/src/fonts.rs`），
而不是 force push 覆盖 `v1` —— jsDelivr 按 tag 缓存，覆盖后最长要等 7 天才生效。
