---
marp: true
theme: default
paginate: true
header: 'Marpサンプルプレゼンテーション'
footer: '作成日: 2026-02-11'
---

<!-- _class: lead -->
# Marpへようこそ

Markdownでプレゼンテーションを作成

**VSCode + Marp で簡単スライド作成**

---

## Marpとは？

- **Markdown**ベースのプレゼンテーションツール
- VSCodeで**リアルタイムプレビュー**
- PDF、PPTX、HTMLに**エクスポート可能**
- **Gitでバージョン管理**できる
- コードスニペットや数式に対応

---

## スライドの作り方

各スライドは `---` で区切ります

```markdown
---
## スライドタイトル

内容をここに記述

---
```

シンプルで直感的！

---

## テキストの装飾

**太字** と *斜体* と ~~取り消し線~~

> 引用文も使えます

- 箇条書き
  - ネストも可能
    - さらにネスト

1. 番号付きリスト
2. 自動で番号が振られます

---

## コードハイライト

JavaScriptのサンプル:

```javascript
function greet(name) {
  console.log(`Hello, ${name}!`);
  return `Welcome to Marp!`;
}

greet('世界');
```

シンタックスハイライトも完璧！

---

## 画像の挿入

Markdown形式で画像を挿入:

```markdown
![画像の説明](image.png)
```

サイズ調整も可能:

```markdown
![w:500](image.png)  <!-- 幅500px -->
![h:300](image.png)  <!-- 高さ300px -->
```

---

## 2カラムレイアウト

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">

<div>

### 左カラム

- ポイント1
- ポイント2
- ポイント3

</div>

<div>

### 右カラム

- 特徴A
- 特徴B
- 特徴C

</div>

</div>

---

## 数式のサポート

インライン数式: $E = mc^2$

ブロック数式:

$$
\int_{a}^{b} f(x) dx = F(b) - F(a)
$$

数式もきれいに表示できます！

---

## テーブル

| 機能 | 説明 | 対応 |
|------|------|------|
| Markdown | 記法が簡単 | ✅ |
| プレビュー | リアルタイム | ✅ |
| エクスポート | PDF/PPTX | ✅ |
| テーマ | カスタマイズ可 | ✅ |

---

## カスタムスタイル

<!-- _class: lead -->
<!-- _backgroundColor: #1e3a8a -->
<!-- _color: white -->

# 背景色や文字色も変更可能

このスライドは青背景に白文字

---

## エクスポート方法

1. **コマンドパレット** を開く (`Ctrl+Shift+P`)
2. 「**Marp: Export Slide Deck**」を選択
3. エクスポート形式を選択:
   - PDF
   - PowerPoint (PPTX)
   - HTML
   - 画像 (PNG/JPEG)

---

<!-- _class: lead -->

# まとめ

- ✅ Markdownで簡単にスライド作成
- ✅ VSCodeで快適な編集環境
- ✅ 多様なエクスポート形式
- ✅ バージョン管理も容易

**さっそく試してみましょう！**

---

<!-- _class: lead -->
<!-- _paginate: false -->

# ありがとうございました

**Happy Presenting with Marp!** 🎉
