const { DateTime } = require("luxon");
const fs = require("fs");
const path = require("path");
const crypto = require("crypto");
const { isPublished, isSlugPublished } = require("./lib/publishing");
const { resolveCategory, pickRelated } = require("./lib/categories");

module.exports = function (eleventyConfig) {
  eleventyConfig.addPassthroughCopy("src/assets");
  eleventyConfig.addGlobalData("currentYear", () => new Date().getFullYear());

  // 記事ごとの OG 画像(scripts/generate_og_images.py が og-images/<slug>.png に生成)。
  // ・公開済みの記事の画像だけを /assets/og/ にコピーする。予約公開待ちの記事の
  //   画像(タイトル入り)が記事より先に公開されないようにするため。
  // ・画像が無い記事(生成に失敗した場合など)は ogImage が空を返し、テンプレートは
  //   og:image も画像タグも出さない。画像が無くてもビルドは止まらない。
  // ・URL の ?v= は画像の中身のハッシュ。タイトルを直したとき SNS 側の古い画像の
  //   キャッシュを避けるため。
  const ogImages = {};
  const ogDir = path.join(__dirname, "og-images");
  if (fs.existsSync(ogDir)) {
    for (const file of fs.readdirSync(ogDir)) {
      if (!file.endsWith(".png")) continue;
      const slug = file.slice(0, -4);
      if (!isSlugPublished(slug)) continue;
      const hash = crypto
        .createHash("md5")
        .update(fs.readFileSync(path.join(ogDir, file)))
        .digest("hex")
        .slice(0, 8);
      ogImages[slug] = `/assets/og/${file}?v=${hash}`;
      eleventyConfig.addPassthroughCopy({ [`og-images/${file}`]: `assets/og/${file}` });
    }
  }
  eleventyConfig.addFilter("ogImage", (slug) => ogImages[slug] || "");

  // 予約公開の記事へのリンクを、リンク先が公開されたビルドから表示する(JP と同じ)。
  //   {% whenPublished "slug" %}...[記事]({{ '/posts/slug/' | url }})...{% endwhenPublished %}
  // リンク先が未公開の間は中身を丸ごと出さない(404 のリンクを作らない)。
  eleventyConfig.addPairedShortcode("whenPublished", (content, slug) =>
    isSlugPublished(slug) ? content : ""
  );

  eleventyConfig.addCollection("posts", function (collectionApi) {
    const now = new Date();
    // 判定は lib/publishing.js に集約している。
    // src/posts/posts.11tydata.js のページ生成可否と必ず同じ結果になるようにするため、
    // ここに条件を直接書き足さないこと。
    return collectionApi
      .getFilteredByGlob("src/posts/*.md")
      .filter((item) => isPublished(item.data, now))
      .sort((a, b) => b.date - a.date);
  });

  // テーマ(カテゴリ)別のまとめページ用。/category/<slug>/ を1テーマ1ページで作る。
  // 材料は公開判定済みの記事だけ(未公開記事は一覧にもリンクにも出さない)。
  // 公開済みの記事が1本も無いテーマは、ページを作らない。
  eleventyConfig.addCollection("categoryHubs", function (collectionApi) {
    const now = new Date();
    // 編集中に categories.json を書き換えても反映されるよう、毎回読み直す
    delete require.cache[require.resolve("./src/_data/categories.json")];
    const categoriesData = require("./src/_data/categories.json");
    const posts = collectionApi
      .getFilteredByGlob("src/posts/*.md")
      .filter((item) => isPublished(item.data, now))
      .sort((a, b) => b.date - a.date);
    const unassigned = posts.filter(
      (item) => !resolveCategory(categoriesData, item.fileSlug, item.data.category)
    );
    if (unassigned.length) {
      console.warn(
        "[categories] テーマ未登録の公開記事があります(src/_data/categories.json の posts に追加してください): " +
          unassigned.map((i) => i.fileSlug).join(", ")
      );
    }
    return categoriesData.categories
      .map((c) => ({
        ...c,
        posts: posts.filter(
          (item) =>
            (resolveCategory(categoriesData, item.fileSlug, item.data.category) || {}).slug === c.slug
        ),
      }))
      .filter((c) => c.posts.length > 0);
  });

  // 関連記事: 同じテーマの公開済み記事を最大6本。同テーマが4本未満なら新しい記事で4本まで補う。
  eleventyConfig.addFilter("relatedPosts", (posts, currentUrl, categorySlug) =>
    pickRelated(posts, currentUrl, categorySlug, 6, 4)
  );

  eleventyConfig.addFilter("readableDate", (dateObj) => {
    return DateTime.fromJSDate(dateObj, { zone: "utc" }).toFormat("LLLL d, yyyy");
  });

  // "YYYY-MM-DD" の文字列を "September 22, 2026" にする(記事ページの公開日・更新日用)
  eleventyConfig.addFilter("longDateStr", (s) => {
    const dt = DateTime.fromISO(String(s || ""), { zone: "utc" });
    return dt.isValid ? dt.setLocale("en").toFormat("LLLL d, yyyy") : "";
  });

  eleventyConfig.addFilter("htmlDateString", (dateObj) => {
    return DateTime.fromJSDate(dateObj, { zone: "utc" }).toFormat("yyyy-LL-dd");
  });

  eleventyConfig.addFilter("readingTime", (content) => {
    const text = String(content || "").replace(/<[^>]*>/g, " ");
    const words = text.split(/\s+/).filter(Boolean).length;
    const minutes = Math.max(1, Math.round(words / 200));
    return `${minutes} min read`;
  });

  return {
    pathPrefix: "/",
    dir: {
      input: "src",
      output: "_site",
      includes: "_includes",
    },
  };
};
