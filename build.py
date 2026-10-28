#!/usr/bin/env python3
"""Генератор статического сайта: python build.py -> HTML в корне репозитория (для GitHub Pages)."""
import pathlib

ROOT = pathlib.Path(__file__).parent

# ---- Настройки: всё, что может измениться, — здесь ----
NAME = "Попов Матвей Юрьевич"
NAME_EN = "Matvey Popov"
INN = "231521307407"
UPDATED_RU = "27 октября 2026 года"
UPDATED_EN = "October 27, 2026"
MIN_AMOUNT = 100        # меньше этого — не принимаем
ACCESS_AMOUNT = 500     # разовый платёж от этой суммы — услуга «Ранний доступ»
ACCESS_STARS = 250      # то же в Telegram Stars (оплата в боте, для тех, у кого нет российской карты)
STAR_RUB = ACCESS_AMOUNT // ACCESS_STARS  # сколько рублей засчитывается за 1 Star (платежи суммируются)
MAX_AMOUNT = 100000
CONTACT_EMAIL = "arapplicationssupport@gmail.com"
PHONE = "+7 995 169-18-97"
POSTAL_ADDRESS = "353924, Краснодарский край, г. Новороссийск, ул. Южная, д. 21, кв. 110"  # просит платёжный сервис
POSTAL_ADDRESS_EN = "21 Yuzhnaya St., apt. 110, Novorossiysk, Krasnodar Krai, 353924, Russia"
# На время модерации платёжным сервисом личные данные скрыты (ФИО, ИНН, телефон, почтовый адрес). Вернуть: True.
# Что именно скрыто — local-docs/removed-for-moderation.md
SHOW_PERSONAL = False
PERSON_RU = NAME if SHOW_PERSONAL else "Автор проектов"
PERSON_GEN_RU = NAME if SHOW_PERSONAL else "их автора"          # «проектов ...»
PERSON_EN = NAME_EN if SHOW_PERSONAL else "The projects' author"
PERSON_GEN_EN = NAME_EN if SHOW_PERSONAL else "their author"    # "the projects of ..."
INN_RU = f", ИНН {INN}" if SHOW_PERSONAL else ""
INN_EN = f", taxpayer ID {INN}" if SHOW_PERSONAL else ""
TAG_MAX = 16            # длина тега в чате обсуждения (ограничение Telegram)
# Форма оплаты на сайте шлёт сумму на сервер бота, он создаёт платёж в платёжном сервисе. Пусто — формы нет, только бот.
PAY_FORM_URL = ""       # "https://arapplications.ru/pay" — включить, когда платёжный сервис подключён
SITE_URL = "https://allvoid.github.io/support"
BOT = "@ArapplicationsBot"
BOT_URL = "https://t.me/ArapplicationsBot"
TG_URL = "https://t.me/arsound_git"
ARSOUND_URL = "https://github.com/Allvoid/arsound"
STEAM_URL = "https://steamcommunity.com/id/ardeveloper/myworkshopfiles/"
GITHUB_URL = "https://github.com/Allvoid"

MODS = [
    ("No Metabolism Limit", "https://github.com/Allvoid/NoMetabolismLimit-Rimworld"),
    ("Void Touched – No Scarification Debuff", "https://github.com/Allvoid/VoidTouchedNoScarDebuff"),
    ("DoubleAmputateLegs", "https://github.com/Allvoid/DoubleAmputateLegs"),
    ("Hemogen Generator Gene", "https://github.com/Allvoid/HemogenGeneratorGene"),
    ("No Food Void Touch", "https://github.com/Allvoid/NoFoodVoidTouch"),
    ("Item Reroll", "https://github.com/Allvoid/ItemReroll-Rimworld"),
]

CSS = """
:root{color-scheme:light;--bg:#eaf0f7;--bar:rgba(246,249,253,.85);--panel:#f8fafd;--ink:#2a3547;--head:#0e1a2e;--dim:#62708a;--line:#d3dce9;--accent:#2563c4;--accent-ink:#1d55ac;--on-accent:#fff;--wave-on:#4a9ae8;--wave-off:#c6d2e3;--glow:rgba(74,154,232,.18)}
:root[data-theme=dark]{color-scheme:dark;--bg:#0b111b;--bar:rgba(11,17,27,.85);--panel:#121a28;--ink:#cbd6e6;--head:#edf3fb;--dim:#8191a8;--line:#202c3f;--accent:#6cb2f5;--accent-ink:#8cc4f8;--on-accent:#07121f;--wave-on:#6cb2f5;--wave-off:#26344b;--glow:rgba(108,178,245,.13)}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){color-scheme:dark;--bg:#0b111b;--bar:rgba(11,17,27,.85);--panel:#121a28;--ink:#cbd6e6;--head:#edf3fb;--dim:#8191a8;--line:#202c3f;--accent:#6cb2f5;--accent-ink:#8cc4f8;--on-accent:#07121f;--wave-on:#6cb2f5;--wave-off:#26344b;--glow:rgba(108,178,245,.13)}}
*{box-sizing:border-box}
body{margin:0;background:radial-gradient(900px 420px at 85% -10%,var(--glow),transparent 70%) no-repeat,var(--bg);color:var(--ink);font:16px/1.65 "Segoe UI",Inter,system-ui,-apple-system,Roboto,sans-serif;padding:0 16px}
html.theming,html.theming *,html.theming *::before,html.theming *::after{transition:background-color .45s ease,color .45s ease,border-color .45s ease,fill .45s ease,box-shadow .45s ease,opacity .35s ease,transform .55s cubic-bezier(.5,0,.2,1)!important}
a{color:var(--accent-ink)}
.bar{background:var(--bar);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);border-bottom:1px solid var(--line);margin:0 -16px;padding:0 16px;position:sticky;top:0;z-index:5}
header,main,footer{max-width:860px;margin:0 auto}
header{display:flex;flex-wrap:wrap;gap:4px 22px;align-items:center;min-height:56px}
header .brand{display:flex;align-items:center;gap:10px;font-weight:700;color:var(--head);text-decoration:none;margin-right:auto;padding:8px 0}
header .brand svg{flex:none}
header a{text-decoration:none;color:var(--dim);font-size:.95rem;padding:6px 0;border-bottom:2px solid transparent}
header a:hover{color:var(--head)}
header a.cur{color:var(--head);border-bottom-color:var(--accent)}
header a.brand{border:0}
#theme{position:relative;width:38px;height:38px;padding:0;background:none;border:1px solid var(--line);color:var(--dim);border-radius:50%;cursor:pointer;overflow:hidden}
#theme:hover{color:var(--head);border-color:var(--dim)}
#theme:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
#theme svg{position:absolute;inset:0;margin:auto;width:20px;height:20px;transition:transform .55s cubic-bezier(.5,0,.2,1),opacity .35s ease}
#theme .moon{opacity:0;transform:rotate(-90deg) scale(.4)}
:root[data-theme=dark] #theme .sun{opacity:0;transform:rotate(90deg) scale(.4)}
:root[data-theme=dark] #theme .moon{opacity:1;transform:none}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]) #theme .sun{opacity:0;transform:rotate(90deg) scale(.4)}:root:not([data-theme=light]) #theme .moon{opacity:1;transform:none}}
main{padding:28px 0 40px}
.wave{display:block;width:100%;height:56px;margin:0 0 22px}
.wave .on{fill:var(--wave-on)}
.wave .off{fill:var(--wave-off)}
.wave rect{transform-box:fill-box;transform-origin:center;animation:pulse 2.8s ease-in-out infinite;animation-delay:calc(var(--i)*40ms)}
@keyframes pulse{0%,100%{transform:scaleY(1)}50%{transform:scaleY(.82)}}
@media (prefers-reduced-motion:reduce){.wave rect{animation:none}html.theming,html.theming *{transition:none!important}#theme svg{transition:none}}
h1{font-size:2rem;line-height:1.2;margin:0 0 8px;color:var(--head);letter-spacing:-.01em}
h2{font-size:1.2rem;margin:2.2rem 0 .5rem;color:var(--head)}
.lead{color:var(--dim);margin:0 0 1.5rem}
.card{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:18px 22px;margin:14px 0}
.card h3{margin:.1rem 0 .3rem;color:var(--head)}
.muted{color:var(--dim);font-size:.92rem}
.btn{display:inline-block;background:var(--accent);color:var(--on-accent);text-decoration:none;padding:11px 26px;border-radius:999px;font-weight:700}
.btn:hover{filter:brightness(1.08)}
ul{padding-left:1.3rem}
footer{border-top:1px solid var(--line);padding:18px 0 40px;color:var(--dim);font-size:.9rem}
.tiers{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:14px;margin:14px 0}
.tiers .card{margin:0}
.tier.hl{border-color:var(--accent);box-shadow:0 0 0 1px var(--accent) inset}
.price{font-size:1.35rem;font-weight:700;color:var(--head);margin:.1rem 0 .6rem}
.pay{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin:.6rem 0}
.pay input[type=number]{width:9.5rem;font:inherit;padding:9px 12px;border:1px solid var(--line);border-radius:10px;background:var(--bg);color:var(--head)}
.pay .chip{font:inherit;padding:8px 14px;border:1px solid var(--line);border-radius:999px;background:none;color:var(--ink);cursor:pointer}
.pay .chip:hover{border-color:var(--accent)}
.pay label{flex-basis:100%;font-size:.92rem;color:var(--dim)}
.pay button.btn{border:0;cursor:pointer;font:inherit;font-weight:700}
.btn.alt{background:none;color:var(--accent-ink);box-shadow:0 0 0 1px var(--accent) inset}
#hint{font-size:.92rem;color:var(--dim);flex-basis:100%;margin:0}
@media (max-width:520px){h1{font-size:1.6rem}header{gap:2px 16px}}
"""

# Волна-украшение: детерминированные столбики, первая треть — оранжевая, как проигранная часть трека
def wave_svg():
    import math
    bars = []
    for i in range(96):
        h = 6 + int(34 * abs(math.sin(i * 0.37) * math.cos(i * 0.11)) + 8 * abs(math.sin(i * 1.7)))
        cls = "on" if i < 32 else "off"
        bars.append(f'<rect class="{cls}" style="--i:{i}" x="{i * 8}" y="{28 - h // 2}" width="5" height="{h}" rx="2.5"/>')
    return f'<svg class="wave" viewBox="0 0 768 56" preserveAspectRatio="none" aria-hidden="true">{"".join(bars)}</svg>'


LOGO = ('<svg width="30" height="20" viewBox="0 0 30 20" aria-hidden="true"><g style="fill:var(--wave-on)">'
        '<rect x="0" y="9" width="3" height="8" rx="1.5"/><rect x="5" y="5" width="3" height="12" rx="1.5"/>'
        '<rect x="10" y="1" width="3" height="16" rx="1.5"/><rect x="15" y="6" width="3" height="11" rx="1.5"/>'
        '<rect x="20" y="3" width="3" height="14" rx="1.5"/><rect x="25" y="8" width="3" height="9" rx="1.5"/></g></svg>')

THEME_JS = """(function(){var r=document.documentElement,b=document.getElementById('theme');
function cur(){var t=r.getAttribute('data-theme');return t||(matchMedia('(prefers-color-scheme:dark)').matches?'dark':'light')}
function label(){var l=cur()==='dark'?b.dataset.l:b.dataset.d;b.setAttribute('aria-label',l);b.title=l}
label();try{matchMedia('(prefers-color-scheme:dark)').addEventListener('change',label)}catch(e){}
var tm;b.addEventListener('click',function(){var n=cur()==='dark'?'light':'dark';r.classList.add('theming');clearTimeout(tm);
r.setAttribute('data-theme',n);try{localStorage.setItem('theme',n)}catch(e){}label();tm=setTimeout(function(){r.classList.remove('theming')},600)})})();"""

SUN = ('<svg class="sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true">'
       '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>')
MOON = ('<svg class="moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
        '<path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>')

THEME_INIT = """try{var t=localStorage.getItem('theme');if(t==='dark'||t==='light')document.documentElement.setAttribute('data-theme',t)}catch(e){}"""


def tel():
    return "+" + "".join(c for c in PHONE if c.isdigit())


def contact_ru():
    show = SHOW_PERSONAL
    address = f"<li>Почтовый адрес: {POSTAL_ADDRESS}</li>" if POSTAL_ADDRESS and show else ""
    who = f'<li>Исполнитель: {NAME}, плательщик налога на профессиональный доход (самозанятый)</li>' if show else ""
    inn = f'<li>ИНН: {INN}</li>' if show else ""
    phone = f'<li>Телефон: <a href="tel:{tel()}">{PHONE}</a></li>' if show else ""
    return (f'<ul>{who}'
            f'{inn}'
            f'{phone}'
            f'<li>E-mail для обращений и возвратов: <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a></li>'
            f'{address}'
            f'<li>Ошибки, предложения, вопросы по оплате: Telegram-бот <a href="{BOT_URL}">{BOT}</a></li>'
            f'<li>Новости проекта: <a href="{TG_URL}">Telegram-канал t.me/arsound_git</a></li></ul>')


def contact_en():
    show = SHOW_PERSONAL
    address = f"<li>Postal address: {POSTAL_ADDRESS_EN or POSTAL_ADDRESS}</li>" if POSTAL_ADDRESS and show else ""
    who = f'<li>Provider: {NAME_EN}, self-employed (Russian "Tax on Professional Income" regime)</li>' if show else ""
    inn = f'<li>Taxpayer ID (INN): {INN}</li>' if show else ""
    phone = f'<li>Phone: <a href="tel:{tel()}">{PHONE}</a></li>' if show else ""
    return (f'<ul>{who}'
            f'{inn}'
            f'{phone}'
            f'<li>E-mail for requests and refunds: <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a></li>'
            f'{address}'
            f'<li>Bugs, ideas, payment questions: Telegram bot <a href="{BOT_URL}">{BOT}</a></li>'
            f'<li>Project news: <a href="{TG_URL}">Telegram channel t.me/arsound_git</a></li></ul>')


PAY_JS = """(function(){var f=document.getElementById('pay');if(!f)return;var a=f.amount,h=document.getElementById('hint');
function upd(){var v=+a.value;h.textContent=v>=+f.dataset.access?f.dataset.yes:f.dataset.no}
f.querySelectorAll('.chip').forEach(function(c){c.addEventListener('click',function(){a.value=c.dataset.v;upd()})});
a.addEventListener('input',upd);upd()})();"""


def pay_form(lang):
    ru = lang == "ru"
    chips = "".join(f'<button type="button" class="chip" data-v="{v}">{v} {"₽" if ru else "RUB"}</button>'
                    for v in (ACCESS_AMOUNT, ACCESS_AMOUNT * 2, ACCESS_AMOUNT * 4))
    yes = (f"Этой суммы хватит на премиум-доступ: после оплаты вы вернётесь в бот {BOT}, он пришлёт ссылку." if ru
           else f"This is enough for premium access: after paying you return to {BOT}, which sends the link.")
    no = (f"Сумма засчитается в оплату премиум-доступа: платежи суммируются, доступ откроется на {ACCESS_AMOUNT} ₽." if ru
          else f"It counts toward premium access: payments add up, access opens at {ACCESS_AMOUNT} RUB.")
    offer = ('Я принимаю условия <a href="offer.html">публичной оферты</a> и <a href="privacy.html">политики '
             'конфиденциальности</a>' if ru else
             'I accept the <a href="offer.html">public offer</a> and the <a href="privacy.html">privacy policy</a>')
    return (f'<form id="pay" class="pay" method="post" action="{PAY_FORM_URL}" data-access="{ACCESS_AMOUNT}" '
            f'data-yes="{yes}" data-no="{no}">{chips}'
            f'<input type="number" name="amount" min="{MIN_AMOUNT}" max="{MAX_AMOUNT}" step="1" '
            f'value="{ACCESS_AMOUNT}" required aria-label="{"Сумма, ₽" if ru else "Amount, RUB"}">'
            f'<button class="btn" type="submit">{"Оплатить" if ru else "Pay"}</button>'
            f'<p id="hint"></p><label><input type="checkbox" required> {offer}</label></form>')


def pay_ru():
    bot = (f'<p><a class="btn{" alt" if PAY_FORM_URL else ""}" href="{BOT_URL}?start=premium">Оплатить в Telegram-боте</a></p>'
           f'<p class="muted">В боте — карта или СБП через платёжный сервис, а без российской карты — Telegram Stars '
           f'(премиум-доступ — {ACCESS_STARS} ⭐). Бот сам открывает доступ сразу после оплаты.</p>')
    if PAY_FORM_URL:
        return (f"<p>Картой или через СБП на этом сайте (через платёжный сервис). Сумма — от {MIN_AMOUNT} "
                f"до {MAX_AMOUNT} ₽ за платёж.</p>{pay_form('ru')}<p>Или в Telegram:</p>{bot}")
    return (f"{bot}<p class=\"muted\">Оплата картой прямо на сайте появится после подключения платёжного сервиса.</p>")


def pay_en():
    bot = (f'<p><a class="btn{" alt" if PAY_FORM_URL else ""}" href="{BOT_URL}?start=premium">Pay in the Telegram bot</a></p>'
           f'<p class="muted">Without a Russian card, pay with Telegram Stars in the bot (premium access is {ACCESS_STARS} ⭐). '
           f'Russian cards and SBP work through the payment service. The bot opens access right after the payment.</p>')
    if PAY_FORM_URL:
        return (f"<p>By card or SBP on this site (through the payment service, Russian cards). From {MIN_AMOUNT} to {MAX_AMOUNT} RUB "
                f"per payment.</p>{pay_form('en')}<p>Or in Telegram:</p>{bot}")
    return f"{bot}<p class=\"muted\">Card payments on the site will appear once the payment service is connected.</p>"


def mods_list():
    return "".join(f'<li><a href="{u}">{n}</a></li>' for n, u in MODS)


# ------------------------------------------------------------------ RU
RU = {}

RU["index"] = ("Премиум-доступ", f"""
<h1>Премиум-доступ «Ранний доступ»</h1>
<p class="lead">Arsound и моды для RimWorld — бесплатные проекты с открытым кодом от независимого разработчика.
Премиум-доступ «Ранний доступ» стоит {ACCESS_AMOUNT} ₽ (или {ACCESS_STARS} ⭐) и даёт закрытый канал с тестовыми
сборками, приоритетное рассмотрение ваших сообщений об ошибках и предложений и свой тег в чате обсуждения. Оплатить
можно сразу или частями: платежи суммируются.</p>

<div class="tiers">
<div class="card tier hl">
<h3>Премиум-доступ «Ранний доступ»</h3>
<p class="price">{ACCESS_AMOUNT} ₽ или {ACCESS_STARS} ⭐</p>
<ul>
<li>🔒 Закрытый Telegram-канал: тестовые сборки раньше основного канала и новости, которых там нет.</li>
<li>⚡ Приоритет: ваши сообщения об ошибках и предложения в боте {BOT} рассматриваются первыми.</li>
<li>🏷 Свой тег в чате обсуждения — подпись рядом с вашим именем.</li>
</ul>
<p class="muted">Одним платежом или частями. Доступ бессрочный.</p>
</div>
<div class="card tier">
<h3>Оплата частями</h3>
<p class="price">платёж от {MIN_AMOUNT} ₽ (звёздами — от 1 ⭐)</p>
<p>Платежи суммируются по вашему аккаунту Telegram: когда наберётся {ACCESS_AMOUNT} ₽, откроется премиум-доступ.
Платёж сверх цены или после открытия доступа — дополнительный платёж: он ничего не меняет в доступе.</p>
</div>
</div>

<h2>Как оплатить</h2>
{pay_ru()}
<p class="muted">Оплачивая, вы принимаете условия <a href="offer.html">публичной оферты</a>. После оплаты приходит чек
самозанятого. Возврат — по разделу 6 оферты.</p>

<h2>Как получить доступ</h2>
<ol>
<li>Оплатите премиум-доступ — {ACCESS_AMOUNT} ₽ (или {ACCESS_STARS} ⭐): одним платежом или несколькими, в боте {BOT} или
на этом сайте. Бот суммирует платежи вашего аккаунта Telegram.</li>
<li>После оплаты на сайте вы вернётесь в бот — так платёж привяжется к вашему аккаунту. Когда сумма наберётся, бот
пришлёт ссылку на закрытый канал.</li>
<li>Нажмите ссылку и отправьте заявку на вступление: бот одобрит её сам, обычно сразу, не позже чем через 24 часа.</li>
</ol>
<p class="muted">Канал и бот работают в Telegram, поэтому для доступа нужен аккаунт Telegram.</p>

<h2>Что покрывает оплата</h2>
<ul>
<li>время на новые версии и исправления ошибок;</li>
<li>тестовые устройства — телефоны разных производителей и версий Android;</li>
<li>сервер и домен для бота, приёма заявок и оплаты;</li>
<li>сервисы для сборки и распространения проектов.</li>
</ul>

<h2>О проектах</h2>
<div class="card">
<h3>Arsound</h3>
<p>Мод для Android-приложения SoundCloud. Неофициальный проект с открытым кодом, не связан с SoundCloud.</p>
<p class="muted"><a href="{ARSOUND_URL}">Исходный код на GitHub</a> · <a href="{TG_URL}">Telegram-канал со сборками</a></p>
</div>

<div class="card">
<h3>Моды для RimWorld</h3>
<p>Бесплатные моды в Steam Workshop и на GitHub:</p>
<ul>{mods_list()}</ul>
<p class="muted"><a href="{STEAM_URL}">Профиль в Steam Workshop</a> · <a href="{GITHUB_URL}">GitHub</a></p>
</div>

<h2>Контакты</h2>
{contact_ru()}
<p class="muted">Чек самозанятого формируется в приложении «Мой налог» и приходит на e-mail или телефон, указанные при
оплате. Данные карты вводятся на стороне платёжного сервиса и разработчику не передаются.</p>
""")

RU["offer"] = ("Публичная оферта", f"""
<h1>Публичная оферта</h1>
<p class="lead">Об услуге «Ранний доступ» (премиум-доступ). Редакция от {UPDATED_RU}.</p>
<p>Проекты бесплатны для всех. Оферта описывает платную услугу «Ранний доступ» (в Боте и на сайте — «Премиум-доступ») и
два вида платежей: оплату этой услуги и дополнительные платежи, которые ничего не открывают.</p>

<h2>1. Термины</h2>
<p>1.1. <b>Исполнитель</b> — {PERSON_RU}, физическое лицо, применяющее специальный налоговый режим «Налог на
профессиональный доход» (самозанятый){INN_RU}.</p>
<p>1.2. <b>Пользователь</b> — дееспособное физическое лицо, которое совершает Платёж.</p>
<p>1.3. <b>Проекты</b> — приложение Arsound и моды для RimWorld с <a href="index.html">главной страницы</a>: свободное
программное обеспечение с открытым кодом, бесплатное для всех.</p>
<p>1.4. <b>Бот</b> — Telegram-бот {BOT} (<a href="{BOT_URL}">{BOT_URL}</a>).</p>
<p>1.5. <b>Закрытый канал</b> — приватный Telegram-канал Исполнителя для пользователей с Ранним доступом.</p>
<p>1.6. <b>Обращение</b> — сообщение об ошибке или предложение, отправленное через Бот.</p>
<p>1.7. <b>Платёж</b> — перечисление денег Исполнителю одной операцией: в рублях через платёжный сервис
(оператор приёма платежей; его название и условия указаны на странице оплаты, далее — Платёжный сервис) или звёздами
Telegram (Telegram Stars) в Боте.</p>

<h2>2. Предмет и акцепт</h2>
<p>2.1. Настоящий документ — публичная оферта (ст. 435 и п. 2 ст. 437 Гражданского кодекса РФ). Совершая Платёж,
Пользователь полностью и безоговорочно принимает её условия (п. 3 ст. 438 ГК РФ).</p>
<p>2.2. <b>Услуга «Ранний доступ» (премиум-доступ).</b> Цена услуги из раздела 3 — {ACCESS_AMOUNT} ₽ (возмездное оказание услуг,
глава 39 ГК РФ). Её можно внести одним Платежом или частями: Платежи Пользователя суммируются по его аккаунту Telegram —
в Боте сразу, на сайте после возврата в Бот по ссылке со страницы оплаты. Платёж звёздами засчитывается из расчёта
1 Star = {STAR_RUB} ₽. Платежи засчитываются в оплату услуги, пока их сумма не достигнет цены; тогда услуга считается
оплаченной.</p>
<p>2.3. <b>Дополнительный платёж.</b> Платежи после оплаты услуги и часть Платежа сверх её цены — дополнительные
платежи. Они вносятся по желанию Пользователя, не предполагают встречного предоставления и ничего не открывают.</p>
<p>2.4. Ни дополнительные платежи, ни услуга не открывают функций в самих Проектах: Проекты одинаково доступны всем
бесплатно.</p>
<p>2.5. Оферта опубликована по адресу <a href="{SITE_URL}/offer.html">{SITE_URL}/offer.html</a>.</p>

<h2>3. Услуга «Ранний доступ»</h2>
<p>3.1. Услуга включает:</p>
<ul>
<li>бессрочный доступ к Закрытому каналу, где Исполнитель по мере готовности публикует тестовые сборки Проектов раньше
основного канала и новости, которых нет в основном канале;</li>
<li>приоритетное рассмотрение Обращений: Обращения Пользователя рассматриваются раньше Обращений пользователей без
Раннего доступа;</li>
<li>возможность получить тег — подпись рядом с именем Пользователя в Telegram-чате обсуждения Проектов (п. 3.7).</li>
</ul>
<p>3.2. Исполнитель не обещает определённого числа, частоты или содержания публикаций, сроков исправления ошибок и
реализации предложений. Тестовые сборки могут работать нестабильно.</p>
<p>3.3. Порядок оказания: когда сумма Платежей достигла цены услуги (п. 2.2), Бот присылает Пользователю ссылку на
Закрытый канал, а заявку на вступление одобряет автоматически. Срок — не позднее 24 часов с этого момента.</p>
<p>3.4. Услуга считается оказанной, когда Пользователь получил доступ к Закрытому каналу (ссылка направлена, заявка
одобрена). Выйти из канала и вернуться можно сколько угодно раз — доступ сохраняется.</p>
<p>3.5. Доступ персональный. Нельзя передавать его другим людям и выкладывать тестовые сборки из Закрытого канала в
открытый доступ. При нарушении Исполнитель вправе прекратить доступ.</p>
<p>3.6. Если Закрытый канал прекращает работу, Исполнитель заранее сообщает об этом в Боте и в основном канале.</p>
<p>3.7. Тег Пользователь предлагает через Бот: до {TAG_MAX} символов, без эмодзи, нецензурных и оскорбительных слов.
Исполнитель вправе отклонить любой предложенный тег без объяснения причин. Отклонение не лишает Пользователя
возможности предложить другой тег. Исполнитель вправе снять установленный тег, если он нарушает эти правила или
правила чата. Тег ставится, пока Пользователь состоит в чате обсуждения.</p>

<h2>4. Оплата</h2>
<p>4.1. Сумма — от {MIN_AMOUNT} до {MAX_AMOUNT} ₽ за одну операцию; звёздами — от 1 Star.</p>
<p>4.2. Рубли принимаются через Платёжный сервис (банковская карта, СБП и другие доступные там способы) на его
странице оплаты; название и условия Платёжного сервиса указаны на этой странице. Данные карты вводятся на стороне
Платёжного сервиса; Исполнитель их не получает.</p>
<p>4.3. Telegram Stars принимаются в Боте по правилам Telegram.</p>
<p>4.4. Платёж считается совершённым, когда платёжный сервис или Telegram подтвердил операцию.</p>
<p>4.5. На платёж в рублях Исполнитель формирует чек по закону о налоге на профессиональный доход и направляет его на
e-mail или телефон, указанные при оплате.</p>

<h2>5. Права и обязанности</h2>
<p>5.1. Исполнитель направляет полученные средства на работу над Проектами и услугой «Ранний доступ» (время разработки,
тестирование и тестовые устройства, серверы и сервисы для сборки и распространения), оказывает услугу по разделу 3 и
обращается с данными Пользователя по <a href="privacy.html">Политике конфиденциальности</a>.</p>
<p>5.2. Отчёт о расходовании средств Исполнитель не предоставляет.</p>
<p>5.3. Пользователь подтверждает, что средства принадлежат ему на законных основаниях. Пользователь младше 18 лет
совершает Платёж с согласия родителей или законных представителей.</p>

<h2>6. Возврат</h2>
<p>6.1. Дополнительные платежи (п. 2.3) не возвращаются, кроме двойного или ошибочного списания из-за технического
сбоя.</p>
<p>6.2. Услуга: Пользователь вправе отказаться от услуги до её оказания и получить возврат Платежей, засчитанных в её
оплату (ст. 32 Закона «О защите прав потребителей»). Если доступ не предоставлен в срок из п. 3.3 по причинам,
зависящим от Исполнителя, эти Платежи по запросу возвращаются полностью. После предоставления доступа услуга считается
оказанной (п. 3.4).</p>
<p>6.3. Двойное или ошибочное списание возвращается в любом случае.</p>
<p>6.4. Как запросить возврат: в Боте (команда /paysupport) или на e-mail из раздела «Контакты». Укажите
дату, сумму и способ оплаты. Не присылайте номер карты и коды из SMS. Срок ответа и возврата — 10 дней. Деньги
возвращаются тем же способом: рубли — через Платёжный сервис на ту же карту или счёт, звёзды — звёздами в Telegram.</p>

<h2>7. Ответственность</h2>
<p>7.1. Проекты, тестовые сборки и материалы Закрытого канала предоставляются «как есть» — см.
<a href="terms.html">Пользовательское соглашение</a>.</p>
<p>7.2. Исполнитель не отвечает за перебои в работе Telegram и платёжных сервисов, которые от него не зависят.</p>

<h2>8. Заключительные положения</h2>
<p>8.1. Применяется право Российской Федерации.</p>
<p>8.2. Споры решаются переговорами, а при недостижении согласия — в порядке, установленном законодательством РФ.</p>
<p>8.3. Исполнитель вправе менять оферту. Действующая редакция всегда доступна по адресу из п. 2.5; изменения не
затрагивают уже совершённых Платежей.</p>

<h2>Контакты</h2>
{contact_ru()}
""")

RU["privacy"] = ("Политика конфиденциальности", f"""
<h1>Политика конфиденциальности</h1>
<p class="lead">Редакция от {UPDATED_RU}</p>

<h2>1. Оператор</h2>
<p>Оператор персональных данных — {PERSON_RU}, самозанятый{INN_RU}. Контакты — в конце страницы.</p>

<h2>2. Сайт</h2>
<p>Сайт статический: у него нет аккаунтов, cookie, счётчиков посещений, рекламы и сторонней аналитики. Он размещён на
GitHub Pages; GitHub, как любой веб-сервер, может фиксировать технические данные запроса (IP-адрес, браузер, время) по
своей политике — у оператора доступа к ним нет.</p>
<p>Форма оплаты передаёт на сервер оператора (arapplications.ru) только выбранную сумму. Сервер ведёт технический
журнал запросов (IP-адрес, время, адрес страницы) для защиты от злоупотреблений и хранит его не дольше 30 дней.</p>

<h2>3. Бот {BOT}</h2>
<p>Когда вы пишете боту, обрабатываются: ID Telegram, имя и username, язык; тексты заявок (ошибки, предложения,
вопросы по оплате) и переписка по ним; сведения о Раннем доступе (есть ли он и с какого дня); теги для чата
обсуждения, которые вы предложили. Файлы, логи, видео и
скриншоты, которые вы прикладываете, остаются на серверах Telegram: бот пересылает их разработчику внутри Telegram и
на свой сервер не скачивает. Данные бота хранятся на сервере оператора, резервные копии — 14 дней.</p>
<p>Telegram обрабатывает ваши данные по собственной политике.</p>

<h2>4. Платежи</h2>
<p>Обрабатываются: сумма, дата, статус и идентификатор платежа, а также связь платежа с ID Telegram — чтобы открыть
Ранний доступ. E-mail или телефон для чека вы указываете на странице оплаты платёжного сервиса (оператора приёма платежей; его
название и условия указаны на этой странице). Номер карты, CVC и имя держателя оператор не получает и не хранит.
Платёжный сервис и Telegram (для оплаты звёздами) обрабатывают данные по своим политикам. Для чека сведения о платеже вносятся в приложение «Мой налог» (ФНС России).</p>

<h2>5. Цели, основания и сроки</h2>
<p>Цели: приём платежей и выдача чеков, оказание услуги «Ранний доступ», рассмотрение заявок и ответы на них,
налоговые обязанности, защита от злоупотреблений. Основания: договор по <a href="offer.html">оферте</a>, заключаемый
по вашей инициативе, обязанности по закону и ваше согласие (п. 1, 2 и 5 ч. 1 ст. 6 Федерального закона № 152-ФЗ
«О персональных данных»). Оплачивая или отправляя заявку в бот, вы соглашаетесь с обработкой данных на условиях этой
Политики.</p>
<p>Данные не продаются и не передаются третьим лицам, кроме платёжного сервиса, Telegram и ФНС — в объёме, нужном для
перечисленных целей. Сведения о платежах хранятся в течение срока налоговой отчётности (не менее 4 лет), заявки и
переписка — пока нужны для решения вопроса; по вашей просьбе их удалят раньше.</p>

<h2>6. Ваши права</h2>
<p>Вы можете узнать, какие данные о вас есть, потребовать исправить или удалить их (если закон не требует их хранить)
и отозвать согласие. Напишите в бот или на e-mail ниже; ответ — в течение 10 рабочих дней. Если считаете, что ваши права
нарушены, можно обратиться в Роскомнадзор.</p>

<h2>7. Сами проекты</h2>
<p>Arsound и моды для RimWorld не отправляют данные оператору. Что приложение отправляет сторонним сервисам (например,
названия треков и исполнителей в Last.fm для рекомендаций), описано в <a href="{ARSOUND_URL}">README проекта</a>; эти
функции настраиваются пользователем.</p>

<h2>8. Изменения</h2>
<p>Актуальная редакция всегда на этой странице и действует с момента публикации.</p>

<h2>Контакты</h2>
{contact_ru()}
""")

RU["terms"] = ("Пользовательское соглашение", f"""
<h1>Пользовательское соглашение</h1>
<p class="lead">Редакция от {UPDATED_RU}</p>

<h2>1. Общие положения</h2>
<p>1.1. Соглашение определяет условия использования сайта, Telegram-бота {BOT} и проектов {PERSON_GEN_RU} (далее — Автор):
приложения Arsound и модов для RimWorld. Пользуясь ими, вы принимаете условия Соглашения.</p>
<p>1.2. Проекты распространяются бесплатно, с открытым исходным кодом, на условиях лицензий, указанных в их
репозиториях. Платежи — оплата услуги «Ранний доступ» (премиум-доступ) и дополнительные платежи — регулируются
<a href="offer.html">публичной офертой</a>.</p>

<h2>2. Неофициальные проекты</h2>
<p>2.1. Arsound — неофициальный проект. Он не связан и не одобрен SoundCloud, ReVanced, Valve, Ludeon Studios и
другими правообладателями. Названия и товарные знаки принадлежат их владельцам.</p>
<p>2.2. Пользователь сам отвечает за соблюдение условий сервисов, с которыми работает Arsound (в частности
пользовательского соглашения SoundCloud и законов об авторском праве), и за то, как использует загруженные материалы.
Автор не предоставляет доступа к платному контенту, не хранит и не раздаёт чужие треки.</p>

<h2>3. Отсутствие гарантий</h2>
<p>3.1. Проекты предоставляются «как есть». Автор не гарантирует бесперебойную работу, совместимость с будущими
версиями SoundCloud, RimWorld и Android и не отвечает за косвенные убытки, потерю данных или блокировку аккаунтов у
сторонних сервисов.</p>
<p>3.2. Установка и использование — на риск пользователя. Рекомендуется делать резервные копии сохранений и данных.</p>
<p>3.3. Тестовые сборки из закрытого канала — предварительные версии: в них чаще встречаются ошибки.</p>

<h2>4. Премиум-доступ «Ранний доступ»</h2>
<p>4.1. Дополнительные платежи (сверх цены услуги) ничего не открывают и не дают преимуществ.</p>
<p>4.2. Услуга «Ранний доступ» (премиум-доступ) даёт доступ к закрытому каналу с тестовыми сборками и новостями, приоритетное
рассмотрение ваших сообщений об ошибках и предложений и тег в чате обсуждения. Функций в самих проектах она не
открывает.</p>
<p>4.3. Условия, суммы и возврат — в <a href="offer.html">оферте</a>.</p>

<h2>5. Бот</h2>
<p>5.1. Через бота принимаются сообщения об ошибках, предложения и вопросы по оплате. Не отправляйте в бот пароли,
номера карт и чужие персональные данные.</p>
<p>5.2. За спам и оскорбления Автор вправе перестать принимать сообщения от пользователя.</p>

<h2>6. Изменения</h2>
<p>Автор может менять Соглашение; актуальная редакция — на этой странице.</p>

<h2>7. Применимое право</h2>
<p>Право Российской Федерации. Споры решаются путём переговоров, а при недостижении согласия — по законодательству РФ.</p>

<h2>Контакты</h2>
{contact_ru()}
""")

# ------------------------------------------------------------------ EN
EN = {}

EN["index"] = ("Premium access", f"""
<h1>Premium access "Early access"</h1>
<p class="lead">Arsound and the RimWorld mods are free, open-source projects by an independent developer. Premium
access "Early access" costs {ACCESS_STARS} ⭐ (or {ACCESS_AMOUNT} RUB) and gives a private channel with test builds,
priority review of your bug reports and ideas, and your own tag in the discussion chat. You can pay at once or in
parts: payments add up.</p>

<div class="tiers">
<div class="card tier hl">
<h3>Premium access "Early access"</h3>
<p class="price">{ACCESS_STARS} ⭐ or {ACCESS_AMOUNT} RUB</p>
<ul>
<li>🔒 A private Telegram channel: test builds before the main channel, and news that is not posted there.</li>
<li>⚡ Priority: your bug reports and ideas in the {BOT} bot are reviewed first.</li>
<li>🏷 Your own tag in the discussion chat — a label next to your name.</li>
</ul>
<p class="muted">In one payment or in parts. Access does not expire.</p>
</div>
<div class="card tier">
<h3>Paying in parts</h3>
<p class="price">a payment from {MIN_AMOUNT} RUB (in Stars — from 1 ⭐)</p>
<p>Payments add up on your Telegram account: once they reach {ACCESS_STARS} ⭐ ({ACCESS_AMOUNT} RUB), premium access
opens. A payment above the price or after access is open is an additional payment: it changes nothing in the
access.</p>
</div>
</div>

<h2>How to pay</h2>
{pay_en()}
<p class="muted">By paying you accept the <a href="offer.html">public offer</a>. Refunds follow section 6 of the
offer.</p>

<h2>How to get access</h2>
<ol>
<li>Pay for premium access — {ACCESS_STARS} ⭐ (or {ACCESS_AMOUNT} RUB): in one payment or several, in the {BOT} bot
or on this site. The bot adds up the payments of your Telegram account.</li>
<li>After paying on the site you return to the bot — that links the payment to your account. Once the total is reached,
the bot sends the private channel link.</li>
<li>Tap the link and send a join request: the bot approves it automatically, usually at once, within 24 hours at
most.</li>
</ol>
<p class="muted">The channel and the bot live in Telegram, so a Telegram account is needed for access.</p>

<h2>What the payment covers</h2>
<ul>
<li>time for new versions and bug fixes;</li>
<li>test devices — phones of different brands and Android versions;</li>
<li>the server and domain for the bot, requests and payments;</li>
<li>services for building and distributing the projects.</li>
</ul>

<h2>About the projects</h2>
<div class="card">
<h3>Arsound</h3>
<p>A mod for the Android SoundCloud app. An unofficial open-source project, not affiliated with SoundCloud.</p>
<p class="muted"><a href="{ARSOUND_URL}">Source code on GitHub</a> · <a href="{TG_URL}">Telegram channel with builds</a></p>
</div>

<div class="card">
<h3>RimWorld mods</h3>
<p>Free mods on Steam Workshop and GitHub:</p>
<ul>{mods_list()}</ul>
<p class="muted"><a href="{STEAM_URL}">Steam Workshop profile</a> · <a href="{GITHUB_URL}">GitHub</a></p>
</div>

<h2>Contacts</h2>
{contact_en()}
<p class="muted">For ruble payments a self-employed receipt is issued in the "My Tax" app and sent to the e-mail or
phone given at checkout. Card details are entered on the payment service side and never reach the developer.</p>
""")

EN["offer"] = ("Public offer", f"""
<h1>Public offer</h1>
<p class="lead">On the "Early access" service (premium access). Version of {UPDATED_EN}. The Russian version prevails
in case of discrepancy.</p>
<p>The projects are free for everyone. This offer covers the paid "Early access" service (called "Premium access" in
the Bot and on the site) and two kinds of payments: payment for that service and additional payments, which unlock
nothing.</p>

<h2>1. Terms</h2>
<p>1.1. <b>Provider</b> — {PERSON_EN}, an individual under the Russian special tax regime "Tax on Professional Income"
(self-employed){INN_EN}.</p>
<p>1.2. <b>User</b> — a legally capable individual who makes a Payment.</p>
<p>1.3. <b>Projects</b> — the Arsound app and the RimWorld mods listed on the <a href="index.html">main page</a>: free,
open-source software.</p>
<p>1.4. <b>Bot</b> — the Telegram bot {BOT} (<a href="{BOT_URL}">{BOT_URL}</a>).</p>
<p>1.5. <b>Private channel</b> — the Provider's private Telegram channel for users with Early access.</p>
<p>1.6. <b>Request</b> — a bug report or an idea sent through the Bot.</p>
<p>1.7. <b>Payment</b> — a single transfer of money to the Provider: in rubles through a payment service
(a payment acceptance operator whose name and terms are shown on the payment page; the "Payment Service") or in
Telegram Stars in the Bot.</p>

<h2>2. Subject and acceptance</h2>
<p>2.1. This is a public offer under Article 435 and Article 437(2) of the Civil Code of the Russian Federation. By
making a Payment, the User fully and unconditionally accepts it (Article 438(3)).</p>
<p>2.2. <b>"Early access" service (premium access).</b> The price of the service in section 3 is {ACCESS_AMOUNT} RUB (paid services,
Chapter 39 of the Civil Code). It may be paid in one Payment or in parts: the User's Payments add up on their Telegram
account — in the Bot at once, on the site after returning to the Bot via the link on the payment page. A Payment in
Stars counts as 1 Star = {STAR_RUB} RUB. Payments count toward the service until their total reaches the price; then
the service is paid.</p>
<p>2.3. <b>Additional payment.</b> Payments made after the service is paid, and the part of a Payment above its price,
are additional payments. They are made at the User's option, imply nothing in return and unlock nothing.</p>
<p>2.4. Neither additional payments nor the service unlock any features in the Projects: the Projects are free for
everyone.</p>
<p>2.5. Published at <a href="{SITE_URL}/en/offer.html">{SITE_URL}/en/offer.html</a>.</p>

<h2>3. The "Early access" service</h2>
<p>3.1. The service includes:</p>
<ul>
<li>non-expiring access to the Private channel, where the Provider posts test builds of the Projects before the main
channel, when they are ready, and news not posted in the main channel;</li>
<li>priority review of Requests: the User's Requests are reviewed before those of users without Early access;</li>
<li>a tag — a label next to the User's name in the Projects' Telegram discussion chat (clause 3.7).</li>
</ul>
<p>3.2. The Provider does not promise any number, frequency or content of posts, or deadlines for fixes and ideas.
Test builds may be unstable.</p>
<p>3.3. Delivery: once the total of Payments reaches the price (clause 2.2), the Bot sends the User the Private channel
link and approves the join request automatically, within 24 hours of that moment.</p>
<p>3.4. The service is rendered when the User gets access to the Private channel (the link is sent, the request is
approved). The User may leave and rejoin any number of times — access is kept.</p>
<p>3.5. Access is personal. Do not share it or publish test builds from the Private channel. On violation the Provider
may end the access.</p>
<p>3.6. If the Private channel closes, the Provider announces it in advance in the Bot and in the main channel.</p>
<p>3.7. The User proposes a tag through the Bot: up to {TAG_MAX} characters, no emoji, no obscene or insulting words.
The Provider may reject any proposed tag without giving reasons. A rejection does not take away the User's right to
propose another tag. The Provider may remove a tag that breaks these rules or the chat rules. A tag is set while the
User is a member of the discussion chat.</p>

<h2>4. Payment</h2>
<p>4.1. From {MIN_AMOUNT} to {MAX_AMOUNT} RUB per operation; in Stars — from 1 Star.</p>
<p>4.2. Rubles are accepted through the Payment Service (bank card, SBP and other methods it offers) on its payment
page; the name and terms of the Payment Service are shown on that page. Card details are entered on the Payment
Service side; the Provider never receives them.</p>
<p>4.3. Telegram Stars are accepted in the Bot under Telegram's rules.</p>
<p>4.4. A Payment is made when the payment service or Telegram confirms it.</p>
<p>4.5. For ruble Payments the Provider issues a receipt under the professional income tax law to the e-mail or phone
given at checkout.</p>

<h2>5. Rights and obligations</h2>
<p>5.1. The Provider spends the funds received on the work on the Projects and the "Early access" service
(development time, testing and test devices, servers and services for building and distributing), renders the service
under section 3 and handles the User's data under the <a href="privacy.html">Privacy policy</a>.</p>
<p>5.2. The Provider gives no report on spending.</p>
<p>5.3. The User confirms the funds are lawfully theirs. A User under 18 pays with the consent of a parent or
guardian.</p>

<h2>6. Refunds</h2>
<p>6.1. Additional payments (clause 2.3) are not refunded, except for a double or erroneous charge caused by a technical
failure.</p>
<p>6.2. Service: the User may cancel before the service is rendered and get back the Payments counted toward it
(Article 32 of the Russian Consumer Protection Law). If access is not given within the time in clause 3.3 for reasons on
the Provider's side, those Payments are refunded in full on request. Once access is given, the service is rendered
(clause 3.4).</p>
<p>6.3. A double or erroneous charge is always refunded.</p>
<p>6.4. To ask for a refund, use /paysupport in the Bot or the e-mail in "Contacts". Give the date, amount
and method. Never send card numbers or SMS codes. Reply and refund within 10 days, by the same method: rubles through
the Payment Service to the same card or account, Stars as Stars in Telegram.</p>

<h2>7. Liability</h2>
<p>7.1. The Projects, test builds and Private channel materials are provided "as is" — see the
<a href="terms.html">Terms of use</a>.</p>
<p>7.2. The Provider is not liable for outages of Telegram or payment services beyond its control.</p>

<h2>8. Final provisions</h2>
<p>8.1. Governed by the law of the Russian Federation.</p>
<p>8.2. Disputes are settled by negotiation; failing that, under Russian legislation.</p>
<p>8.3. The Provider may change this offer. The current version is always at the address in clause 2.5; changes do not
affect Payments already made.</p>

<h2>Contacts</h2>
{contact_en()}
""")

EN["privacy"] = ("Privacy policy", f"""
<h1>Privacy policy</h1>
<p class="lead">Version of {UPDATED_EN}. The Russian version prevails in case of discrepancy.</p>

<h2>1. Operator</h2>
<p>The data operator is {PERSON_EN}, self-employed{INN_EN}. Contacts are at the bottom of the page.</p>

<h2>2. This site</h2>
<p>The site is static: no accounts, cookies, visit counters, ads or third-party analytics. It is hosted on GitHub
Pages; like any web server, GitHub may log technical request data (IP address, browser, time) under its own policy —
the operator has no access to it.</p>
<p>The payment form sends only the chosen amount to the operator's server (arapplications.ru). The server keeps a
technical request log (IP address, time, page address) against abuse for no longer than 30 days.</p>

<h2>3. The {BOT} bot</h2>
<p>When you write to the bot, it processes: your Telegram ID, name and username, language; the texts of your requests
(bugs, ideas, payment questions) and the conversation about them; your Early access status (whether you have it and
since when); the tags you proposed for the discussion chat. Files, logs, videos and screenshots you attach stay on Telegram's servers: the bot forwards them to the
developer inside Telegram and does not download them. Bot data is stored on the operator's server; backups are kept
for 14 days.</p>
<p>Telegram processes your data under its own policy.</p>

<h2>4. Payments</h2>
<p>We process the amount, date, status and ID of a payment and its link to your Telegram ID — to open Early access.
You enter the e-mail or phone for the receipt on the payment page of the payment service (the payment acceptance operator; its name and terms are
shown on that page). We never receive or store your card number, CVC or cardholder name. The payment service and
Telegram (for Stars) process data under their own policies. For
the receipt, payment details are entered into the "My Tax" app of the Russian Federal Tax Service.</p>

<h2>5. Purposes, grounds and retention</h2>
<p>Purposes: accepting payments and issuing receipts, rendering the "Early access" service, handling requests, tax
duties, protection against abuse. Grounds: the contract under the <a href="offer.html">offer</a> concluded at your
initiative, legal duties and your consent (Article 6(1)(1, 2, 5) of Russian Federal Law No. 152-FZ). By paying or
sending a request to the bot you consent to the processing described here.</p>
<p>Data is not sold or passed to third parties, except the payment service, Telegram and the tax service, as needed for
these purposes. Payment records are kept for the tax reporting period (at least 4 years); requests and conversations —
as long as needed to resolve them, or less on your request.</p>

<h2>6. Your rights</h2>
<p>You may ask what data we hold, ask to correct or delete it (unless the law requires keeping it) and withdraw
consent. Write to the bot or the e-mail below; we reply within 10 business days. You may also complain to
Roskomnadzor, the Russian data protection authority.</p>

<h2>7. The projects themselves</h2>
<p>Arsound and the RimWorld mods do not send data to the operator. What the app sends to third-party services (for
example track and artist names to Last.fm for recommendations) is described in the <a href="{ARSOUND_URL}">project
README</a>; these features are user-configurable.</p>

<h2>8. Changes</h2>
<p>The current version is always on this page and takes effect when published.</p>

<h2>Contacts</h2>
{contact_en()}
""")

EN["terms"] = ("Terms of use", f"""
<h1>Terms of use</h1>
<p class="lead">Version of {UPDATED_EN}. The Russian version prevails in case of discrepancy.</p>

<h2>1. General</h2>
<p>1.1. These terms govern the use of this site, the Telegram bot {BOT} and the projects of {PERSON_GEN_EN} (the Author):
the Arsound app and the RimWorld mods. By using them you accept these terms.</p>
<p>1.2. The projects are free and open-source under the licenses in their repositories. Payments — for the "Early access"
service (premium access) and additional payments — are governed by the <a href="offer.html">public offer</a>.</p>

<h2>2. Unofficial projects</h2>
<p>2.1. Arsound is unofficial. It is not affiliated with or endorsed by SoundCloud, ReVanced, Valve, Ludeon Studios or
other rights holders. Names and trademarks belong to their owners.</p>
<p>2.2. Users are responsible for complying with the terms of services Arsound works with (notably SoundCloud's terms
and copyright law) and for how they use downloaded material. The Author does not provide access to paid content and
does not store or distribute third-party tracks.</p>

<h2>3. No warranty</h2>
<p>3.1. The projects are provided "as is". The Author does not guarantee uninterrupted operation or compatibility with
future versions of SoundCloud, RimWorld or Android, and is not liable for indirect losses, data loss or account
restrictions at third-party services.</p>
<p>3.2. Installation and use are at your own risk. Back up saves and data.</p>
<p>3.3. Test builds from the private channel are previews and contain more bugs.</p>

<h2>4. Premium access "Early access"</h2>
<p>4.1. Additional payments (above the price of the service) unlock nothing and give no advantages.</p>
<p>4.2. The "Early access" service (premium access) gives access to the private channel with test builds and news, priority review of
your bug reports and ideas, and a tag in the discussion chat. It unlocks no features in the projects.</p>
<p>4.3. Terms, amounts and refunds are in the <a href="offer.html">offer</a>.</p>

<h2>5. The bot</h2>
<p>5.1. The bot accepts bug reports, ideas and payment questions. Do not send passwords, card numbers or other people's
personal data.</p>
<p>5.2. The Author may stop accepting messages from a user for spam or abuse.</p>

<h2>6. Changes</h2>
<p>The Author may change these terms; the current version is on this page.</p>

<h2>7. Governing law</h2>
<p>Law of the Russian Federation. Disputes are settled by negotiation; failing that, under Russian legislation.</p>

<h2>Contacts</h2>
{contact_en()}
""")

def legal_html(name):
    """Russian privacy policy and user agreement: the payment service's templates from legal/, only date and name filled in."""
    import html as _html
    out, items = [], []

    def flush():
        if items:
            out.append("<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>")
            items.clear()

    first_text = True
    for raw in (ROOT / "legal" / name).read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line:
            continue
        text = _html.escape(line.lstrip("#- ").strip() if line[0] in "#-" else line, quote=False)
        if line.startswith("## "):
            flush()
            out.append(f"<h2>{text}</h2>")
        elif line.startswith("# "):
            flush()
            out.append(f"<h1>{text}</h1>")
        elif line.startswith("- "):
            items.append(text)
        else:
            flush()
            out.append(f'<p class="lead">{text}</p>' if first_text else f"<p>{text}</p>")
            first_text = False
    flush()
    return chr(10).join(out)


RU["privacy"] = ("Политика конфиденциальности", legal_html("privacy-policy.md"))
RU["terms"] = ("Пользовательское соглашение", legal_html("user-agreement.md"))

RU["support"] = ("Поддержка", f"""
<h1>Поддержка</h1>
<p class="lead">Вопросы по оплате и доступу, ошибки и предложения.</p>

<h2>Telegram-бот {BOT}</h2>
<p>Основной способ связи: в боте можно сообщить об ошибке, предложить идею, задать вопрос по оплате или доступу.
Ответы приходят в тот же чат с ботом. Обращения тех, кто оформил премиум-доступ, рассматриваются в первую очередь.</p>
<p><a href="{BOT_URL}">Открыть бота {BOT}</a></p>

<h2>Электронная почта</h2>
<p>Для обращений и возвратов: <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a>. Ответим в течение 10 дней.</p>

<h2>Другое</h2>
<ul><li>Новости проекта: <a href="{TG_URL}">Telegram-канал t.me/arsound_git</a></li></ul>
""")

EN["support"] = ("Support", f"""
<h1>Support</h1>
<p class="lead">Questions about payment and access, bugs and ideas.</p>

<h2>Telegram bot {BOT}</h2>
<p>The main way to reach us: in the bot you can report a bug, suggest an idea, or ask about payment or access.
Replies come in the same chat. Requests from users with premium access are handled first.</p>
<p><a href="{BOT_URL}">Open the bot {BOT}</a></p>

<h2>E-mail</h2>
<p>For requests and refunds: <a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a>. We reply within 10 days.</p>

<h2>Other</h2>
<ul><li>Project news: <a href="{TG_URL}">Telegram channel t.me/arsound_git</a></li></ul>
""")

NAV = {
    "ru": [("index", "Главная"), ("offer", "Оферта"), ("support", "Поддержка"), ("privacy", "Конфиденциальность"), ("terms", "Соглашение")],
    "en": [("index", "Home"), ("offer", "Offer"), ("support", "Support"), ("privacy", "Privacy"), ("terms", "Terms")],
}


def render(lang, key, title, body):
    pages = RU if lang == "ru" else EN
    other = "en" if lang == "ru" else "ru"
    nav = "".join(
        f'<a href="{k}.html"{" class=cur" if k == key else ""}>{t}</a>' for k, t in NAV[lang]
    )
    switch_href = (f"en/{key}.html" if lang == "ru" else f"../{key}.html")
    switch_text = "English" if lang == "ru" else "Русский"
    brand = "Премиум-доступ Arsound" if lang == "ru" else "Arsound Premium access"
    if SHOW_PERSONAL:
        foot = f"{NAME} · ИНН {INN}" if lang == "ru" else f"{NAME_EN} · INN {INN}"
    else:
        foot = "Arapplications"
    tl, td = ("Светлая тема", "Тёмная тема") if lang == "ru" else ("Light theme", "Dark theme")
    desc = (f"«Ранний доступ» к Arsound и модам RimWorld за {ACCESS_AMOUNT} ₽: закрытый канал с тестовыми "
            f"сборками, приоритет заявок, тег в чате."
            if lang == "ru" else
            f"Early access to Arsound and the RimWorld mods for {ACCESS_STARS} Stars ({ACCESS_AMOUNT} RUB): a private "
            f"channel with test builds, priority for requests, a chat tag.")
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title if key != "index" else brand}{"" if key == "index" else " — " + brand}</title>
<meta name="description" content="{title}. {desc}">
<script>{THEME_INIT}</script>
<style>{CSS}</style>
</head>
<body>
<div class="bar"><header><a class="brand" href="index.html">{LOGO}{brand}</a>{nav}<a href="{switch_href}">{switch_text}</a><button id="theme" type="button" data-l="{tl}" data-d="{td}">{SUN}{MOON}</button></header></div>
<main>{wave_svg() if key == "index" else ""}{body}</main>
<footer>{foot}</footer>
<script>{THEME_JS}{PAY_JS if key == "index" and PAY_FORM_URL else ""}</script>
</body>
</html>
"""


def main():
    (ROOT / "en").mkdir(exist_ok=True)
    for lang, pages in (("ru", RU), ("en", EN)):
        for key, (title, body) in pages.items():
            out = ROOT / ("en" if lang == "en" else ".") / f"{key}.html"
            out.write_text(render(lang, key, title, body), encoding="utf-8")
    (ROOT / ".nojekyll").write_text("", encoding="utf-8")
    if SHOW_PERSONAL and not POSTAL_ADDRESS:
        print("WARNING: POSTAL_ADDRESS пуст — платёжный сервис просит почтовый адрес в контактах")
    print("ok")


if __name__ == "__main__":
    main()
