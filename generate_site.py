from __future__ import annotations

from datetime import date
from pathlib import Path
import html
import json

BASE_URL = "https://towerrush1w.vercel.app"
AFF_LINK = "https://one-vv793.com/v3/5768/tower-rush?p=0o47"
ROOT = Path(__file__).parent
LANGS = ["ru", "en", "kz", "uz"]

I18N = {
    "ru": {
        "label": "RU",
        "site_name": "Tower Rush Guide",
        "hero_title": "Tower Rush в 1win - обзор игры, стратегии и бонусов",
        "hero_subtitle": "Динамичная crash-игра, где важны timing, дисциплина и грамотный cashout.",
        "meta_base": "Премиальный обзор Tower Rush в 1win: правила, стратегия, управление банкроллом и бонусы.",
        "nav": [("Главная", ""), ("Играть", "play"), ("Демо", "demo"), ("Стратегии", "strategy"), ("Бонусы", "bonus"), ("Блог", "blog/tower-rush-strategy")],
        "cta_play": "Играть в Tower Rush",
        "cta_bonus": "Получить бонус",
        "bonus_title": "Бонусы 1win",
        "bonus_text": "Promo code, free spins, cashback и instant withdraw работают лучше, когда вы играете по заранее заданному плану сессии.",
        "why_title": "Почему Tower Rush в 1win выбирают чаще",
        "why_text": "Игра сочетает простые правила, быстрые раунды и понятный контроль риска. Это делает формат удобным и для новичков, и для игроков с опытом.",
        "table_h1": "Параметр",
        "table_h2": "Детали",
        "table_rows": [("Формат", "Crash / tower game"), ("Темп", "Короткие раунды"), ("Режимы", "Demo и real money"), ("Бонусы", "Casino bonus, cashback, promo code"), ("Платформы", "Desktop и mobile")],
        "guide_title": "Практический гайд",
        "faq_title": "FAQ",
        "faq": [("Как начать играть?", "Перейдите по ссылке, создайте аккаунт в 1win, выберите демо или игру на деньги и задайте лимит сессии."),
                ("Какая стратегия подходит новичку?", "Начните с консервативного сценария: небольшая ставка, ранний cashout, паузы после серии проигрышей."),
                ("Как использовать бонусы безопасно?", "Сначала изучите условия отыгрыша и только потом выбирайте размер ставки. Это снижает риск импульсивной игры.")],
        "footer1": "18+ Играйте ответственно.",
        "footer2": "Партнерский информационный проект.",
    },
    "en": {
        "label": "EN",
        "site_name": "Tower Rush Guide",
        "hero_title": "Tower Rush at 1win - gameplay, strategy, and bonus guide",
        "hero_subtitle": "A fast crash game where timing, bankroll control, and discipline matter.",
        "meta_base": "Professional Tower Rush review with gameplay mechanics, strategy blocks, and risk management tips.",
        "nav": [("Home", ""), ("Play", "play"), ("Demo", "demo"), ("Strategy", "strategy"), ("Bonus", "bonus"), ("Blog", "blog/tower-rush-strategy")],
        "cta_play": "Play Tower Rush",
        "cta_bonus": "Get Bonus",
        "bonus_title": "1win bonus offers",
        "bonus_text": "Promo code, free spins, cashback, and instant withdraw features are more effective when used with a clear session plan.",
        "why_title": "Why players choose Tower Rush at 1win",
        "why_text": "The game combines clear rules, fast rounds, and flexible cashout decisions. It works well for short sessions and structured bankroll play.",
        "table_h1": "Metric",
        "table_h2": "Details",
        "table_rows": [("Format", "Crash / tower game"), ("Round pace", "Fast"), ("Modes", "Demo and real money"), ("Bonuses", "Casino bonus, cashback, promo code"), ("Devices", "Desktop and mobile")],
        "guide_title": "Editorial guide",
        "faq_title": "FAQ",
        "faq": [("How do I start?", "Open 1win from the partner link, register, choose demo or real money mode, and set session limits."),
                ("What is a low-risk approach?", "Use small stakes, earlier cashout targets, and stop rules after losing streaks."),
                ("How should I use bonuses?", "Read wagering terms first and adapt your stake size to protect your bankroll.")],
        "footer1": "18+ Gamble responsibly.",
        "footer2": "Affiliate informational project.",
    },
    "kz": {
        "label": "KZ",
        "site_name": "Tower Rush Guide",
        "hero_title": "Tower Rush 1win - ойын механикасы, стратегия және бонус",
        "hero_subtitle": "Жылдам crash game форматында дұрыс cashout пен bankroll бақылауы маңызды.",
        "meta_base": "Tower Rush бойынша сапалы шолу: ережелер, стратегия, тәуекелді басқару және бонус қолдану.",
        "nav": [("Басты бет", ""), ("Ойнау", "play"), ("Демо", "demo"), ("Стратегия", "strategy"), ("Бонус", "bonus"), ("Блог", "blog/tower-rush-strategy")],
        "cta_play": "Tower Rush ойнау",
        "cta_bonus": "Бонус алу",
        "bonus_title": "1win бонустары",
        "bonus_text": "Promo code, free spins, cashback және instant withdraw мүмкіндігі сессия жоспары бар кезде тиімдірек.",
        "why_title": "Неге ойыншылар Tower Rush таңдайды",
        "why_text": "Ойын қарапайым ережелер мен жоғары темпті біріктіреді. Ойыншы коэффициентті бақылап, тәуекел деңгейін өзі таңдай алады.",
        "table_h1": "Көрсеткіш",
        "table_h2": "Сипаттама",
        "table_rows": [("Формат", "Crash / tower game"), ("Қарқын", "Жылдам раундтар"), ("Режим", "Demo және real money"), ("Бонус", "Casino bonus, cashback, promo code"), ("Құрылғы", "Desktop және mobile")],
        "guide_title": "Пайдалы нұсқаулық",
        "faq_title": "FAQ",
        "faq": [("Ойынды қалай бастаймын?", "Сілтеме арқылы 1win ашып, тіркеліп, demo не real money режимін таңдаңыз."),
                ("Қауіпі төмен стиль қандай?", "Шағын ставка, ерте cashout және ұтылыс сериясынан кейін үзіліс."),
                ("Бонусты қалай дұрыс қолдану керек?", "Алдымен шарттарын оқып, содан кейін ставка мөлшерін таңдаңыз.")],
        "footer1": "18+ Жауапкершілікпен ойнаңыз.",
        "footer2": "Серіктестік ақпараттық жоба.",
    },
    "uz": {
        "label": "UZ",
        "site_name": "Tower Rush Guide",
        "hero_title": "Tower Rush 1win - o'yin sharhi, strategiya va bonuslar",
        "hero_subtitle": "Tez crash game formatida to'g'ri cashout va bankroll nazorati asosiy omil hisoblanadi.",
        "meta_base": "Tower Rush bo'yicha professional qo'llanma: qoidalar, strategiya, risk nazorati va bonuslardan foydalanish.",
        "nav": [("Bosh sahifa", ""), ("O'ynash", "play"), ("Demo", "demo"), ("Strategiya", "strategy"), ("Bonus", "bonus"), ("Blog", "blog/tower-rush-strategy")],
        "cta_play": "Tower Rush o'ynash",
        "cta_bonus": "Bonus olish",
        "bonus_title": "1win bonuslari",
        "bonus_text": "Promo code, free spins, cashback va instant withdraw imkoniyati aniq sessiya rejasi bilan yaxshiroq ishlaydi.",
        "why_title": "Nega Tower Rush mashhur",
        "why_text": "O'yin sodda qoidalar, tez raundlar va moslashuvchan cashout qarorlari bilan ajralib turadi. Bu yangi va tajribali o'yinchilar uchun qulay.",
        "table_h1": "Ko'rsatkich",
        "table_h2": "Tafsilot",
        "table_rows": [("Format", "Crash / tower game"), ("Tezlik", "Tez raundlar"), ("Rejim", "Demo va real money"), ("Bonuslar", "Casino bonus, cashback, promo code"), ("Qurilma", "Desktop va mobile")],
        "guide_title": "Amaliy qo'llanma",
        "faq_title": "FAQ",
        "faq": [("Qanday boshlayman?", "Hamkor havolasi orqali 1win ga o'ting, ro'yxatdan o'ting va mos rejimni tanlang."),
                ("Past xavfli usul qanday?", "Kichik stavka, erta cashout va yutqazish seriyasidan keyin tanaffus."),
                ("Bonusni qanday ishlatish kerak?", "Avval shartlarni o'qing va keyin bankrollga mos stavka tanlang.")],
        "footer1": "18+ Mas'uliyat bilan o'ynang.",
        "footer2": "Hamkorlik axborot loyihasi.",
    },
}


MAIN_PAGES = [
    "",
    "demo",
    "play",
    "strategy",
    "how-to-play",
    "how-to-win",
    "download",
    "reviews",
    "faq",
    "bonus",
    "promo-code",
    "1win",
    "analytics",
    "play-real-money",
    "play-free",
    "play-online",
    "play-no-registration",
    "play-mobile",
    "play-android",
    "play-ios",
    "demo-free",
    "demo-no-registration",
    "demo-mobile",
    "strategy-safe",
    "strategy-aggressive",
    "strategy-low-risk",
    "strategy-high-risk",
]

BLOG_PAGES = [
    "tower-rush-strategy",
    "tower-rush-demo",
    "tower-rush-real-money",
    "how-to-win-tower-rush",
    "tower-rush-bonus",
    "tower-rush-1win-review",
    "best-casino-games",
    "crash-games",
    "tower-rush-mobile",
    "tower-rush-kazakhstan",
    "tower-rush-uzbekistan",
    "tower-rush-app",
    "tower-rush-withdrawal",
    "tower-rush-promo-code",
    "tower-rush-risk-management",
    "tower-rush-beginner-guide",
    "tower-rush-pro-strategy",
    "tower-rush-vs-aviator",
    "tower-rush-betting-system",
    "tower-rush-live-sessions",
    "tower-rush-odds-and-rtp",
]


def localized_slug(lang: str, slug: str) -> str:
    return f"{lang}" if slug == "" else f"{lang}/{slug}"


def path_to_url(path: str) -> str:
    return f"{BASE_URL}/{path}/"


def link_block(lang: str, current: str) -> str:
    core = ["", "play", "demo", "strategy", "bonus", "faq", "reviews"]
    blog_samples = ["blog/tower-rush-strategy", "blog/tower-rush-demo", "blog/tower-rush-mobile"]
    links = []
    for slug in core + blog_samples:
        if slug == current:
            continue
        lslug = localized_slug(lang, slug)
        href = f"/{lslug}/"
        text = "Home" if slug == "" else slug.replace("-", " ").title()
        links.append(f'<a href="{href}">{text}</a>')
    return '<div class="internal-links">' + " ".join(links) + "</div>"


def make_json_ld(lang: str, title: str, url: str) -> str:
    faq = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": I18N[lang]["faq"][0][0],
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": I18N[lang]["faq"][0][1],
                },
            },
            {
                "@type": "Question",
                "name": I18N[lang]["faq"][1][0],
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": I18N[lang]["faq"][1][1],
                },
            },
            {
                "@type": "Question",
                "name": I18N[lang]["faq"][2][0],
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": I18N[lang]["faq"][2][1],
                },
            },
        ],
    }
    review = {
        "@context": "https://schema.org",
        "@type": "Review",
        "itemReviewed": {"@type": "Game", "name": "Tower Rush"},
        "reviewRating": {"@type": "Rating", "ratingValue": "4.9", "bestRating": "5"},
        "author": {"@type": "Organization", "name": "TowerRush1W Editorial Team"},
        "reviewBody": I18N[lang]["meta_base"],
    }
    breadcrumb = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE_URL},
            {"@type": "ListItem", "position": 2, "name": title, "item": url},
        ],
    }
    return (
        '<script type="application/ld+json">'
        + json.dumps(faq, ensure_ascii=False)
        + "</script>"
        + '<script type="application/ld+json">'
        + json.dumps(review, ensure_ascii=False)
        + "</script>"
        + '<script type="application/ld+json">'
        + json.dumps(breadcrumb, ensure_ascii=False)
        + "</script>"
    )


def page_category(slug: str) -> str:
    if slug in {"", "play", "play-online", "play-mobile", "play-real-money"}:
        return "play"
    if slug.startswith("demo"):
        return "demo"
    if "strategy" in slug or slug in {"how-to-win", "how-to-play"}:
        return "strategy"
    if slug in {"bonus", "promo-code", "1win"}:
        return "bonus"
    if slug.startswith("blog/"):
        return "blog"
    return "review"


def editorial_sections(lang: str, slug: str) -> str:
    category = page_category(slug)
    intro_map = {
        "ru": {
            "play": "Tower Rush в 1win — это динамичная crash-игра, где игроку нужно вовремя остановить рост множителя до обрушения башни.",
            "demo": "Демо-режим помогает понять ритм раундов и протестировать стратегию без давления реальных ставок.",
            "strategy": "Рабочая стратегия строится на трех опорах: размер ставки, точка cashout и лимит потерь на сессию.",
            "bonus": "Бонусы дают дополнительный ресурс, но эффективны только при дисциплине и понимании условий отыгрыша.",
            "blog": "Материал собран в формате gambling media: наблюдения, реальные сценарии и аккуратная аналитика без шума.",
            "review": "Этот раздел оформлен как практичный casino review с акцентом на пользу для игрока.",
        },
        "en": {
            "play": "Tower Rush at 1win is a fast crash game where players must cash out before the tower collapses.",
            "demo": "Demo mode is a safe way to test timing, round speed, and entry/exit discipline.",
            "strategy": "A solid strategy links stake size, cashout target, and a strict stop-loss limit.",
            "bonus": "Bonuses are useful when you align them with realistic stakes and session planning.",
            "blog": "This article follows a media-style approach with practical notes and realistic gameplay scenarios.",
            "review": "This section is written as a concise casino review focused on decision quality.",
        },
        "kz": {
            "play": "Tower Rush — мұнара құлағанға дейін ұтысты алып үлгеру керек болатын жылдам crash ойыны.",
            "demo": "Demo режимі раунд ырғағын түсінуге және стратегияны қауіпсіз тексеруге көмектеседі.",
            "strategy": "Тиімді стратегия ставка көлемін, cashout нүктесін және стоп-лимитті бірге қарастырады.",
            "bonus": "Бонус пайдалы, егер оны тәуекелді бақылаумен және нақты жоспармен қолдансаңыз.",
            "blog": "Бұл бөлім gambling media стилінде: практикалық мысал, нақты кеңес және артық уәде жоқ.",
            "review": "Бөлім casino review форматында, негізгі мақсат — ойыншыға пайдалы ақпарат беру.",
        },
        "uz": {
            "play": "Tower Rush — minora qulashidan oldin cashout qilish kerak bo'lgan tezkor crash o'yin.",
            "demo": "Demo rejimi orqali raund tezligi va chiqish vaqtini xavfsiz sinab ko'rish mumkin.",
            "strategy": "Yaxshi strategiya stavka hajmi, cashout nuqtasi va stop-limitni bir tizimga bog'laydi.",
            "bonus": "Bonuslar tartibli bankroll boshqaruvi bilan birga ishlatilganda yaxshiroq natija beradi.",
            "blog": "Bu maqola gambling media uslubida yozilgan: amaliy maslahat va real holatlar.",
            "review": "Bo'lim casino review formatida, asosiy urg'u — foydali va aniq ma'lumot.",
        },
    }
    intro = intro_map[lang][category]
    scenarios = {
        "ru": """
<h2>Реальные сценарии игры</h2>
<ul>
  <li><strong>Консервативный подход:</strong> короткие серии по 10-15 раундов, ранний cashout, сохранение темпа без просадки банка.</li>
  <li><strong>Сбалансированная сессия:</strong> чередование низких и средних ставок, фиксация прибыли после заметного апсвинга.</li>
  <li><strong>Агрессивный режим:</strong> подходит только при заранее установленном лимите потерь и стоп-правиле по времени.</li>
</ul>
""",
        "en": """
<h2>Real gameplay scenarios</h2>
<ul>
  <li><strong>Conservative:</strong> short sets, early cashout, controlled pace.</li>
  <li><strong>Balanced:</strong> low and mid stakes mixed with profit locking.</li>
  <li><strong>Aggressive:</strong> only with strict stop-loss and time cap.</li>
</ul>
""",
        "kz": """
<h2>Нақты ойын сценарийлері</h2>
<ul>
  <li><strong>Консервативті:</strong> қысқа серия, ерте cashout, банкроллды қорғау.</li>
  <li><strong>Теңгерімді:</strong> төмен және орта ставка, пайданың бір бөлігін бекіту.</li>
  <li><strong>Агрессивті:</strong> тек қатаң стоп-лимитпен қолдану керек.</li>
</ul>
""",
        "uz": """
<h2>Amaliy o'yin ssenariylari</h2>
<ul>
  <li><strong>Konservativ:</strong> qisqa sessiya, erta cashout, barqaror temp.</li>
  <li><strong>Balansli:</strong> past va o'rta stavkalarni aralashtirish.</li>
  <li><strong>Agressiv:</strong> faqat stop-limit va vaqt cheklovi bilan.</li>
</ul>
""",
    }[lang]
    bankroll = {
        "ru": """
<h2>Bankroll management</h2>
<p>Рабочее правило для большинства игроков: риск на один раунд до 1-3% от игрового банка. Если сессия уходит в минус, пауза и пересмотр стратегии обычно эффективнее, чем попытка отыграться в ускоренном темпе.</p>
<p>Перед стартом задайте три параметра: размер сессии, лимит потерь и целевой профит. Такая структура делает игру более предсказуемой и снижает эмоциональные решения.</p>
""",
        "en": """
<h2>Bankroll management</h2>
<p>A practical rule is 1-3% risk per round. If results turn negative, pause and review instead of chasing losses.</p>
<p>Set session budget, stop-loss, and target profit before you start.</p>
""",
        "kz": """
<h2>Bankroll management</h2>
<p>Көп ойыншы үшін тиімді шек: бір раундқа 1-3% тәуекел. Теріс серия кезінде үзіліс жасау маңызды.</p>
<p>Сессия бюджеті, stop-loss және мақсатты пайда алдын ала белгіленгені дұрыс.</p>
""",
        "uz": """
<h2>Bankroll management</h2>
<p>Ko'pchilik uchun qulay qoida: har raundda 1-3% risk. Minus seriyada tanaffus qilish foydaliroq.</p>
<p>Sessiya byudjeti, stop-loss va maqsadli foyda oldindan belgilansin.</p>
""",
    }[lang]
    risks = {
        "ru": """
<h2>Риски и ответственная игра</h2>
<p>Crash-формат психологически провоцирует на импульсивные решения, особенно после серии удачных раундов. Лучший способ снизить риск - заранее закрепленный план и запрет на увеличение ставки после проигрыша.</p>
""",
        "en": """
<h2>Risk and responsible play</h2>
<p>Crash games can trigger emotional decisions after winning streaks. A fixed plan and strict limits help reduce that pressure.</p>
""",
        "kz": """
<h2>Тәуекел және жауапты ойын</h2>
<p>Crash форматында эмоцияға еріп шешім қабылдау оңай. Қатаң жоспар мен лимит бұл тәуекелді азайтады.</p>
""",
        "uz": """
<h2>Risk va mas'uliyatli o'yin</h2>
<p>Crash o'yinlarda hissiy qarorlar tez paydo bo'ladi. Qat'iy reja va limitlar xavfni kamaytiradi.</p>
""",
    }[lang]
    slug_title = slug.replace("blog/", "").replace("-", " ").strip().title()
    context_note = (
        f"<p>Раздел <strong>{html.escape(slug_title or 'Home')}</strong> фокусируется на практических решениях: "
        "как выбирать размер ставки, когда делать паузу и как оценивать результат по итогам серии, а не одного раунда.</p>"
    ) if lang == "ru" else ""
    return f"<p>{intro}</p>{context_note}{scenarios}{bankroll}{risks}"


def mobile_lang_options(current: str, slug: str) -> str:
    langs = [("ru", "RU"), ("en", "EN"), ("kz", "KZ"), ("uz", "UZ")]
    out = []
    for code, label in langs:
        selected = ' selected="selected"' if code == current else ""
        target = localized_slug(code, slug)
        out.append(f'<option value="/{target}/"{selected}>{label}</option>')
    return "".join(out)


def page_html(lang: str, slug: str, title_suffix: str) -> str:
    cfg = I18N[lang]
    lslug = localized_slug(lang, slug)
    title = f"{title_suffix} | {cfg['site_name']}"
    desc = f"{cfg['meta_base']} Section: {slug or 'home'}."
    url = path_to_url(lslug)
    canonical = url
    hero_title = cfg["hero_title"] if not slug else f"{title_suffix}: Tower Rush guide"
    hero_subtitle = cfg["hero_subtitle"]
    keywords = "tower rush, multiplier, cashout, strategy, casino bonus, real money, online casino, crash game, tower game"
    cta_buttons = """
<div class="cta-grid">
  <a class="cta-btn" href="{aff}" target="_blank" rel="nofollow sponsored noopener">{play}</a>
  <a class="cta-btn secondary" href="{aff}" target="_blank" rel="nofollow sponsored noopener">{bonus}</a>
</div>
""".format(aff=AFF_LINK, play=cfg["cta_play"], bonus=cfg["cta_bonus"])
    table_rows = "".join([f"<tr><td>{a}</td><td>{b}</td></tr>" for a, b in cfg["table_rows"]])
    table = f"""
<table class="seo-table">
  <tr><th>{cfg['table_h1']}</th><th>{cfg['table_h2']}</th></tr>
  {table_rows}
</table>
"""
    faq_block = f"""
<section class="glass card">
  <h2>{cfg['faq_title']}</h2>
  <details><summary>{cfg['faq'][0][0]}</summary><p>{cfg['faq'][0][1]}</p></details>
  <details><summary>{cfg['faq'][1][0]}</summary><p>{cfg['faq'][1][1]}</p></details>
  <details><summary>{cfg['faq'][2][0]}</summary><p>{cfg['faq'][2][1]}</p></details>
</section>
"""
    hreflang = "\n".join(
        [
            f'<link rel="alternate" hreflang="{("kk" if c=="kz" else c)}" href="{path_to_url(localized_slug(c, slug))}" />'
            for c in LANGS
        ]
    ) + f'\n<link rel="alternate" hreflang="x-default" href="{path_to_url(localized_slug("ru", slug))}" />'
    nav_links = "".join([f'<a href="/{localized_slug(lang, s)}/">{t}</a>' for t, s in cfg["nav"]])
    desktop_lang_links = " | ".join([f'<a href="/{localized_slug(c, slug)}/">{I18N[c]["label"]}</a>' for c in LANGS])
    return f"""<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{html.escape(title)}</title>
  <meta name="description" content="{html.escape(desc)}" />
  <meta name="keywords" content="{html.escape(keywords)}" />
  <link rel="canonical" href="{canonical}" />
  <meta property="og:title" content="{html.escape(title)}" />
  <meta property="og:description" content="{html.escape(desc)}" />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="{url}" />
  <meta property="og:site_name" content="TowerRush1W" />
  {hreflang}
  <link rel="stylesheet" href="/css/styles.css" />
  {make_json_ld(lang, title, url)}
</head>
<body>
  <div class="money-rain" aria-hidden="true"></div>
  <div class="floating-chips" aria-hidden="true"></div>
  <div class="gradient-overlay" aria-hidden="true"></div>
  <header class="site-header glass">
    <div class="brand">TowerRush1W</div>
    <button class="menu-toggle" aria-label="Open menu" aria-expanded="false">☰</button>
    <nav class="top-nav" id="main-nav">{nav_links}</nav>
    <div class="lang-switch desktop">
      {desktop_lang_links}
    </div>
    <select class="lang-switch mobile" onchange="if(this.value) window.location.href=this.value;">
      {mobile_lang_options(lang, slug)}
    </select>
  </header>
  <main>
    <section class="hero glass">
      <h1>{html.escape(hero_title)}</h1>
      <p>{html.escape(hero_subtitle)}</p>
      {cta_buttons}
    </section>
    <section class="glass card">
      <h2>{cfg['why_title']}</h2>
      <p>{cfg['why_text']}</p>
      {table}
    </section>
    <section class="glass card">
      <h2>{cfg['bonus_title']}</h2>
      <p>{cfg['bonus_text']}</p>
      {cta_buttons}
    </section>
    <section class="glass card">
      <h2>{html.escape(title_suffix)}: {cfg['guide_title']}</h2>
      {editorial_sections(lang, slug or "home")}
    </section>
    {faq_block}
    <section class="glass card">
      <h2>Internal links</h2>
      {link_block(lang, slug)}
    </section>
  </main>
  <footer class="site-footer">
    <p>{cfg['footer1']} {cfg['footer2']}</p>
    <p><a href="/{localized_slug(lang,'terms')}/">Terms</a> | <a href="/{localized_slug(lang,'privacy')}/">Privacy</a> | <a href="/{localized_slug(lang,'1win')}/">1win partner disclaimer</a></p>
  </footer>
  <div class="mobile-cta-bar">
    <a href="{AFF_LINK}" class="cta-btn" target="_blank" rel="nofollow sponsored noopener">{cfg['cta_play']}</a>
    <a href="{AFF_LINK}" class="cta-btn secondary" target="_blank" rel="nofollow sponsored noopener">{cfg['cta_bonus']}</a>
  </div>
  <script src="/js/animation.js"></script>
</body>
</html>
"""


def write_page(slug: str, html_content: str) -> None:
    if slug == "":
        path = ROOT / "index.html"
    else:
        path = ROOT / slug / "index.html"
        path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html_content, encoding="utf-8")


def generate_css() -> None:
    css = """
:root {
  --bg: #0c1118;
  --bg2: #141b26;
  --txt: #e8edf7;
  --muted: #a5b1c6;
  --accent: #8b6af7;
  --gold: #d7b06a;
  --cta: #53c692;
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  margin: 0;
  font-family: Inter, Segoe UI, Arial, sans-serif;
  color: var(--txt);
  background: linear-gradient(150deg, var(--bg), var(--bg2));
  min-height: 100vh;
  overflow-x: hidden;
}
.money-rain::before, .money-rain::after {
  content: "$ $ $ $ $ $ $ $ $ $";
  position: fixed;
  left: 0;
  top: -10vh;
  width: 100%;
  color: rgba(215,176,106,.14);
  font-size: clamp(14px, 1.5vw, 24px);
  letter-spacing: 1.2rem;
  animation: rain 16s linear infinite;
  pointer-events: none;
  z-index: 0;
}
.money-rain::after { animation-duration: 20s; animation-delay: -4s; color: rgba(139,106,247,.1); }
@keyframes rain { to { transform: translateY(120vh); } }
.floating-chips::before,
.floating-chips::after {
  content: "◎ ◎ ◎ ◎";
  position: fixed;
  right: 3vw;
  color: rgba(215,176,106,.15);
  font-size: clamp(24px, 3vw, 50px);
  animation: chips 12s ease-in-out infinite;
  z-index: 0;
}
.floating-chips::after { right: auto; left: 3vw; animation-delay: -6s; }
@keyframes chips {
  0%,100% { transform: translateY(0); }
  50% { transform: translateY(-22px); }
}
.gradient-overlay {
  position: fixed;
  inset: 0;
  background: radial-gradient(circle at 70% 0%, rgba(139,106,247,.08), transparent 42%);
  pointer-events: none;
  z-index: 0;
}
.glass {
  background: rgba(20, 27, 38, 0.72);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255,255,255,.08);
  box-shadow: 0 10px 24px rgba(0,0,0,.26);
}
.site-header {
  position: sticky;
  top: 0;
  z-index: 20;
  margin: 12px auto;
  width: min(1150px, calc(100% - 24px));
  border-radius: 16px;
  padding: 10px 14px;
  display: flex;
  justify-content: space-between;
  gap: 12px;
  align-items: center;
}
.brand { font-weight: 800; letter-spacing: .5px; }
.menu-toggle {
  display: none;
  border: 1px solid rgba(255,255,255,.2);
  background: transparent;
  color: var(--txt);
  border-radius: 8px;
  padding: 6px 9px;
}
.top-nav { display:flex; flex-wrap:wrap; gap: 10px; }
.top-nav a { color: var(--muted); text-decoration: none; }
.top-nav a:hover { color: var(--gold); }
main { width: min(1150px, calc(100% - 20px)); margin: 12px auto 120px; position: relative; z-index: 1; }
.hero,.card { border-radius: 18px; padding: clamp(16px, 3vw, 34px); margin-bottom: 18px; }
h1 { margin: 0 0 12px; font-size: clamp(1.9rem, 5vw, 3.3rem); line-height: 1.2; }
h2 { margin-top: 0; color: var(--gold); }
p, li, td { line-height: 1.85; color: #e4e9f4; }
.cta-grid {
  margin-top: 18px;
  display: grid;
  grid-template-columns: repeat(2,minmax(180px,1fr));
  gap: 12px;
}
.cta-btn {
  text-align: center;
  text-decoration: none;
  color: #fff;
  font-weight: 800;
  border-radius: 12px;
  padding: 14px 12px;
  background: linear-gradient(120deg, #4967a9, #5d4db8);
  border: 1px solid rgba(255,255,255,.15);
  transition: transform .2s ease, filter .2s ease;
}
.cta-btn:hover { transform: translateY(-2px); filter: brightness(1.06); }
.cta-btn.secondary { background: linear-gradient(120deg, #355e52, #3a7c62); }
.seo-table { width: 100%; border-collapse: collapse; }
.seo-table th, .seo-table td { border: 1px solid rgba(255,255,255,.15); padding: 10px; text-align: left; }
.internal-links { display: flex; flex-wrap: wrap; gap: 10px; }
.internal-links a {
  color: #b4d8c8;
  text-decoration: none;
  border: 1px solid rgba(180,216,200,.35);
  padding: 8px 10px;
  border-radius: 10px;
}
.lang-switch.desktop { margin-left: auto; color: var(--muted); }
.lang-switch.desktop a { color: var(--txt); text-decoration: none; }
.lang-switch.mobile { display: none; }
.site-footer {
  border-top: 1px solid rgba(255,255,255,.1);
  padding: 22px 12px 86px;
  text-align: center;
  color: var(--muted);
}
.site-footer a { color: var(--gold); }
.mobile-cta-bar { display: none; }
@media (max-width: 900px) {
  .menu-toggle { display: block; }
  .top-nav { display: none; width: 100%; flex-direction: column; margin-top: 8px; }
  .top-nav.open { display: flex; }
  .site-header { flex-wrap: wrap; padding: 8px 10px; gap: 8px; }
  .lang-switch.desktop { display: none; }
  .lang-switch.mobile {
    display: block;
    margin-left: auto;
    background: #182132;
    color: var(--txt);
    border: 1px solid rgba(255,255,255,.15);
    border-radius: 8px;
    padding: 6px;
  }
  .hero,.card { padding: 14px; margin-bottom: 12px; }
  .cta-grid { grid-template-columns: 1fr; }
  .cta-btn { width: 100%; padding: 15px 12px; }
  .mobile-cta-bar {
    display: grid;
    grid-template-columns: 1fr;
    gap: 8px;
    position: fixed;
    left: 10px;
    right: 10px;
    bottom: 8px;
    z-index: 60;
  }
}
"""
    (ROOT / "css").mkdir(exist_ok=True)
    (ROOT / "css" / "styles.css").write_text(css.strip() + "\n", encoding="utf-8")


def generate_js() -> None:
    js = """
const toggle = document.querySelector(".menu-toggle");
const nav = document.querySelector(".top-nav");
if (toggle && nav) {
  toggle.addEventListener("click", () => {
    const expanded = toggle.getAttribute("aria-expanded") === "true";
    toggle.setAttribute("aria-expanded", expanded ? "false" : "true");
    nav.classList.toggle("open");
  });
}
"""
    (ROOT / "js").mkdir(exist_ok=True)
    (ROOT / "js" / "animation.js").write_text(js.strip() + "\n", encoding="utf-8")


def generate_misc_pages() -> None:
    for lang in LANGS:
        write_page(localized_slug(lang, "terms"), page_html(lang, "terms", "Terms and Conditions"))
        write_page(localized_slug(lang, "privacy"), page_html(lang, "privacy", "Privacy Policy"))


def generate_all() -> None:
    generate_css()
    generate_js()
    for lang in LANGS:
        for slug in MAIN_PAGES:
            title_suffix = I18N[lang]["site_name"] if slug == "" else slug.replace("-", " ").title()
            write_page(localized_slug(lang, slug), page_html(lang, slug, title_suffix))
        for blog in BLOG_PAGES:
            bslug = f"blog/{blog}"
            write_page(localized_slug(lang, bslug), page_html(lang, bslug, f"Blog {blog.replace('-', ' ').title()}"))

    generate_misc_pages()
    write_sitemap()
    write_robots()


def write_sitemap() -> None:
    urls = []
    for lang in LANGS:
        for slug in MAIN_PAGES:
            urls.append(path_to_url(localized_slug(lang, slug)))
        for slug in BLOG_PAGES:
            urls.append(path_to_url(localized_slug(lang, f"blog/{slug}")))
        urls.append(path_to_url(localized_slug(lang, "terms")))
        urls.append(path_to_url(localized_slug(lang, "privacy")))
    today = date.today().isoformat()
    rows = [
        f"<url><loc>{u}</loc><lastmod>{today}</lastmod><changefreq>weekly</changefreq><priority>0.8</priority></url>"
        for u in urls
    ]
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(rows)
        + "\n</urlset>\n"
    )
    (ROOT / "sitemap.xml").write_text(xml, encoding="utf-8")


def write_robots() -> None:
    txt = f"""User-agent: *
Allow: /

Sitemap: {BASE_URL}/sitemap.xml
Host: towerrush1w.vercel.app
"""
    (ROOT / "robots.txt").write_text(txt, encoding="utf-8")


if __name__ == "__main__":
    generate_all()
