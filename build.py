#!/usr/bin/env python3
"""Генератор статического сайта: python build.py -> HTML в корне репозитория (для GitHub Pages)."""
import pathlib

ROOT = pathlib.Path(__file__).parent

# ---- Настройки: всё, что может измениться, — здесь ----
NAME = "Попов Матвей Юрьевич"
NAME_EN = "Matvey Popov"
INN = "231521307407"
UPDATED_RU = "26 октября 2026 года"
UPDATED_EN = "October 26, 2026"
MIN_AMOUNT = 100
MAX_AMOUNT = 100000
CONTACT_EMAIL = ""   # впиши публичную почту для связи; пока пусто — страницы дадут GitHub Issues и Telegram
PAY_URL = ""         # ссылка на страницу оплаты платёжного сервиса; пока пусто — блок «скоро»
SITE_URL = "https://allvoid.github.io/support"
PAY_SERVICE = ""     # название платёжного сервиса — попадёт в политику конфиденциальности
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
]

CSS = """
:root{color-scheme:light;--bg:#f2f2f2;--bar:#fff;--panel:#fff;--ink:#333;--head:#111;--dim:#666;--line:#e5e5e5;--accent:#f50;--accent-ink:#c93c00;--wave-off:#ccc}
:root[data-theme=dark]{color-scheme:dark;--bg:#121212;--bar:#111;--panel:#1c1c1c;--ink:#ddd;--head:#fff;--dim:#999;--line:#2c2c2c;--accent:#f50;--accent-ink:#ff8a50;--wave-off:#444}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){color-scheme:dark;--bg:#121212;--bar:#111;--panel:#1c1c1c;--ink:#ddd;--head:#fff;--dim:#999;--line:#2c2c2c;--accent:#f50;--accent-ink:#ff8a50;--wave-off:#444}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.65 "Helvetica Neue",Helvetica,Arial,system-ui,sans-serif;padding:0 16px}
a{color:var(--accent-ink)}
.bar{background:var(--bar);border-bottom:1px solid var(--line);margin:0 -16px;padding:0 16px;position:sticky;top:0}
header,main,footer{max-width:860px;margin:0 auto}
header{display:flex;flex-wrap:wrap;gap:4px 22px;align-items:center;min-height:56px}
header .brand{display:flex;align-items:center;gap:10px;font-weight:700;color:var(--head);text-decoration:none;margin-right:auto;padding:8px 0}
header .brand svg{flex:none}
header a{text-decoration:none;color:var(--dim);font-size:.95rem;padding:6px 0;border-bottom:2px solid transparent}
header a:hover{color:var(--head)}
header a.cur{color:var(--head);border-bottom-color:var(--accent)}
header a.brand{border:0}
#theme{background:none;border:1px solid var(--line);color:var(--dim);border-radius:4px;padding:4px 10px;font:inherit;font-size:.85rem;cursor:pointer}
#theme:hover{color:var(--head);border-color:var(--dim)}
main{padding:28px 0 40px}
.wave{display:block;width:100%;height:56px;margin:0 0 22px}
.wave .on{fill:var(--accent)}
.wave .off{fill:var(--wave-off)}
h1{font-size:2rem;line-height:1.2;margin:0 0 8px;color:var(--head);letter-spacing:-.01em}
h2{font-size:1.2rem;margin:2.2rem 0 .5rem;color:var(--head)}
.lead{color:var(--dim);margin:0 0 1.5rem}
.card{background:var(--panel);border:1px solid var(--line);border-radius:4px;padding:16px 20px;margin:14px 0}
.card h3{margin:.1rem 0 .3rem;color:var(--head)}
.muted{color:var(--dim);font-size:.92rem}
.btn{display:inline-block;background:var(--accent);color:#fff;text-decoration:none;padding:10px 22px;border-radius:4px;font-weight:700}
.btn:hover{filter:brightness(1.08)}
ul{padding-left:1.3rem}
footer{border-top:1px solid var(--line);padding:18px 0 40px;color:var(--dim);font-size:.9rem}
@media (max-width:520px){h1{font-size:1.6rem}header{gap:2px 16px}}
"""

# Волна-украшение: детерминированные столбики, первая треть — оранжевая, как проигранная часть трека
def wave_svg():
    import math
    bars = []
    for i in range(96):
        h = 6 + int(34 * abs(math.sin(i * 0.37) * math.cos(i * 0.11)) + 8 * abs(math.sin(i * 1.7)))
        cls = "on" if i < 32 else "off"
        bars.append(f'<rect class="{cls}" x="{i * 8}" y="{28 - h // 2}" width="5" height="{h}" rx="2"/>')
    return f'<svg class="wave" viewBox="0 0 768 56" preserveAspectRatio="none" aria-hidden="true">{"".join(bars)}</svg>'


LOGO = ('<svg width="30" height="20" viewBox="0 0 30 20" aria-hidden="true"><g fill="#f50">'
        '<rect x="0" y="9" width="3" height="8" rx="1.5"/><rect x="5" y="5" width="3" height="12" rx="1.5"/>'
        '<rect x="10" y="1" width="3" height="16" rx="1.5"/><rect x="15" y="6" width="3" height="11" rx="1.5"/>'
        '<rect x="20" y="3" width="3" height="14" rx="1.5"/><rect x="25" y="8" width="3" height="9" rx="1.5"/></g></svg>')

THEME_JS = """(function(){var r=document.documentElement,b=document.getElementById('theme');
function cur(){var t=r.getAttribute('data-theme');return t||(matchMedia('(prefers-color-scheme:dark)').matches?'dark':'light')}
function label(){b.textContent=cur()==='dark'?b.dataset.l:b.dataset.d}
label();try{matchMedia('(prefers-color-scheme:dark)').addEventListener('change',label)}catch(e){}
b.addEventListener('click',function(){var n=cur()==='dark'?'light':'dark';r.setAttribute('data-theme',n);
try{localStorage.setItem('theme',n)}catch(e){}label()})})();"""

THEME_INIT = """try{var t=localStorage.getItem('theme');if(t==='dark'||t==='light')document.documentElement.setAttribute('data-theme',t)}catch(e){}"""


def contact_ru():
    mail = (f'<a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a>' if CONTACT_EMAIL
            else "<b>[e-mail будет указан до публикации]</b>")
    return (f'<ul><li>Самозанятый: {NAME}</li><li>ИНН: {INN}</li>'
            f'<li>E-mail для обращений и возвратов: {mail}</li>'
            f'<li>Новости проекта: <a href="{TG_URL}">Telegram-канал t.me/arsound_git</a></li></ul>')


def contact_en():
    mail = (f'<a href="mailto:{CONTACT_EMAIL}">{CONTACT_EMAIL}</a>' if CONTACT_EMAIL
            else "<b>[e-mail to be set before publishing]</b>")
    return (f'<ul><li>Self-employed (Russian NPD regime): {NAME_EN}</li><li>Taxpayer ID (INN): {INN}</li>'
            f'<li>E-mail for requests and refunds: {mail}</li>'
            f'<li>Project news: <a href="{TG_URL}">Telegram channel t.me/arsound_git</a></li></ul>')


def pay_ru():
    if PAY_URL:
        return f'<p><a class="btn" href="{PAY_URL}">Поддержать</a></p>'
    return '<p class="muted">Ссылка на страницу оплаты появится после подключения платёжного сервиса.</p>'


def pay_en():
    if PAY_URL:
        return f'<p><a class="btn" href="{PAY_URL}">Donate</a></p>'
    return '<p class="muted">The payment link will appear once a payment service is connected.</p>'


def mods_list():
    return "".join(f'<li><a href="{u}">{n}</a></li>' for n, u in MODS)


# ------------------------------------------------------------------ RU
RU = {}

RU["index"] = ("Поддержка проектов", f"""
<h1>Поддержка проектов</h1>
<p class="lead">Страница добровольных пожертвований независимому разработчику: приложение Arsound и моды для RimWorld.</p>

<div class="card">
<h3>Это не магазин</h3>
<p>Здесь ничего не продаётся. Все проекты бесплатны для всех, с пожертвованием и без него. Пожертвование — добровольный
подарок разработчику, оно не открывает функций, не даёт преимуществ и не создаёт обязательств сверх описанных в
<a href="offer.html">публичной оферте о пожертвовании</a>.</p>
</div>

<h2>Что поддерживаете</h2>
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

<h2>Как поддержать</h2>
<p>Сумма — любая, от {MIN_AMOUNT} до {MAX_AMOUNT} ₽ за один платёж. Деньги идут на разработку:
время на новые версии, тестовые устройства и инфраструктуру. После платежа на указанную почту приходит чек
самозанятого.</p>
{pay_ru()}
<p class="muted">Нажимая «Поддержать», вы принимаете условия <a href="offer.html">публичной оферты</a>.
Возврат пожертвования — только в случаях из раздела 5 оферты.</p>

<h2>Кто получает пожертвования</h2>
{contact_ru()}
""")

RU["offer"] = ("Публичная оферта о пожертвовании", f"""
<h1>Публичная оферта о добровольном пожертвовании</h1>
<p class="lead">Дата последнего обновления: {UPDATED_RU}</p>
<p>Проекты бесплатны для всех. Настоящий документ регулирует только добровольные пожертвования: они не являются
оплатой товаров, работ или услуг и не дают никаких дополнительных прав или функций.</p>

<h2>1. Термины</h2>
<p>1.1. <b>Получатель</b> — {NAME}, физическое лицо, применяющее специальный налоговый режим «Налог на профессиональный
доход» (самозанятый), ИНН {INN}.</p>
<p>1.2. <b>Жертвователь</b> — дееспособное физическое лицо, добровольно перечисляющее денежные средства.</p>
<p>1.3. <b>Проекты</b> — приложение Arsound (патчи с открытым кодом для Android-приложения SoundCloud) и моды для RimWorld,
перечисленные на странице <a href="index.html">«Поддержка проектов»</a>.</p>
<p>1.4. <b>Пожертвование</b> — безвозмездная и добровольная передача денежных средств Получателю на цели из п. 2.2.</p>

<h2>2. Предмет оферты</h2>
<p>2.1. Настоящий документ — публичная оферта (предложение) заключить договор пожертвования в соответствии со статьями 572
и 582 Гражданского кодекса Российской Федерации.</p>
<p>2.2. Пожертвование направляется на поддержку и развитие Проектов — свободно распространяемого программного обеспечения с
открытым исходным кодом, доступного неограниченному кругу лиц бесплатно (общеполезная цель): время разработки,
тестирование, тестовые устройства, серверы и сервисы, необходимые для сборки и распространения.</p>
<p>2.3. Пожертвование добровольно и безвозмездно. Оно не является оплатой товаров, работ или услуг и не обязывает Получателя
предоставить Жертвователю какие-либо товары, услуги, дополнительный или приоритетный функционал, преимущества либо иное
встречное предоставление. Проекты доступны всем одинаково и бесплатно — независимо от факта и размера пожертвования.</p>
<p>2.4. Договор считается заключённым с момента перечисления пожертвования. Перечисление означает полное и безоговорочное
принятие (акцепт) условий настоящей оферты.</p>
<p>2.5. Оферта опубликована по адресу: <a href="{SITE_URL}/offer.html">{SITE_URL}/offer.html</a>.</p>

<h2>3. Размер и порядок перечисления</h2>
<p>3.1. Размер пожертвования определяет Жертвователь самостоятельно, в пределах от {MIN_AMOUNT} ₽ до {MAX_AMOUNT} ₽ за одну операцию.</p>
<p>3.2. Перечисление производится в российских рублях через платёжные сервисы, доступные на момент операции. Данные банковской
карты вводятся на стороне платёжного сервиса; Получатель их не получает.</p>
<p>3.3. Перед перечислением Жертвователь указывает адрес электронной почты, на который направляется чек в соответствии с
законодательством о налоге на профессиональный доход.</p>
<p>3.4. Пожертвование считается совершённым в момент подтверждения операции платёжным сервисом.</p>

<h2>4. Права и обязанности</h2>
<p>4.1. Получатель обязуется использовать средства на цели из п. 2.2, направить Жертвователю чек на указанный адрес и
обращаться с данными Жертвователя в соответствии с <a href="privacy.html">Политикой конфиденциальности</a>.</p>
<p>4.2. Получатель вправе использовать пожертвования по своему усмотрению в рамках целей из п. 2.2 без отчёта о расходовании.</p>
<p>4.3. Жертвователь подтверждает, что перечисляет средства добровольно, понимает безвозмездный характер пожертвования и не
ожидает встречного предоставления.</p>
<p>4.4. Жертвователь гарантирует, что средства принадлежат ему на законных основаниях и что он вправе совершать пожертвование.
Если Жертвователю меньше 18 лет, пожертвование совершается с согласия родителей или законных представителей.</p>

<h2>5. Возврат</h2>
<p>5.1. Ввиду безвозмездного характера пожертвование по общему правилу возврату не подлежит.</p>
<p>5.2. Возврат возможен в исключительных случаях: двойное или ошибочное списание из-за технического сбоя; перечисление в
ошибочном размере вследствие явной технической ошибки — при обращении в разумный срок.</p>
<p>5.3. Для возврата нужно написать Получателю на e-mail из раздела «Контакты и реквизиты» с указанием даты, суммы и адреса
почты, на который пришёл чек. Не публикуйте эти данные в открытых местах (чатах, трекерах).
Срок рассмотрения — до 7 рабочих дней. Возврат делается тем же способом, которым платили.</p>

<h2>6. Заключительные положения</h2>
<p>6.1. Оферта регулируется законодательством Российской Федерации.</p>
<p>6.2. Споры решаются путём переговоров; при недостижении согласия — в порядке, установленном законодательством РФ.</p>
<p>6.3. Получатель вправе изменять условия оферты. Действующая редакция всегда доступна по адресу из п. 2.5; изменения не
затрагивают уже совершённых пожертвований.</p>

<h2>Контакты и реквизиты</h2>
{contact_ru()}
""")

RU["privacy"] = ("Политика конфиденциальности", f"""
<h1>Политика конфиденциальности</h1>
<p class="lead">Дата последнего обновления: {UPDATED_RU}</p>

<h2>1. Кто мы</h2>
<p>Оператор данных — {NAME}, самозанятый, ИНН {INN}. Связь: см. раздел «Контакты» ниже.</p>

<h2>2. Этот сайт</h2>
<p>Сайт статический: у него нет аккаунтов, форм, куки, счётчиков посещений, рекламы и сторонней аналитики. Размещён на
GitHub Pages; как и любой веб-сервер, GitHub может фиксировать технические данные запроса (IP-адрес, браузер, время) по
собственной политике — Получатель к этим данным доступа не имеет.</p>

<h2>3. Пожертвования</h2>
<p>При пожертвовании обрабатываются: сумма, дата и статус платежа, идентификатор операции, адрес электронной почты, который вы
указали для чека. Оплата проходит на стороне платёжного сервиса — номер карты, CVC и имя держателя Получатель не получает и
не хранит. Платёжный сервис{" (" + PAY_SERVICE + ")" if PAY_SERVICE else ""} обрабатывает данные по своей политике.</p>
<p>Оплачивая, вы даёте согласие на обработку указанных выше данных на условиях этой Политики. Согласие можно отозвать, написав
по контактам ниже; сведения, которые закон требует хранить, при этом сохраняются на установленный срок.</p>
<p>Для формирования чека сведения о платеже вносятся в приложение «Мой налог» (ФНС России).</p>

<h2>4. Зачем и как долго</h2>
<p>Данные используются только для приёма платежа, отправки чека, ответа на обращения и выполнения налоговых и бухгалтерских
обязанностей. Не продаются и не передаются третьим лицам, кроме платёжного сервиса и ФНС в объёме, нужном для платежа и
отчётности. Сведения о платежах хранятся в течение срока налоговой и бухгалтерской отчётности (не менее 4 лет), обращения —
пока нужны для решения вопроса.</p>

<h2>5. Ваши права</h2>
<p>Вы можете запросить сведения о своих данных, их исправление или удаление, если закон не требует их хранения. Напишите по
контактам ниже; ответ — в срок до 10 рабочих дней. Если вы считаете, что ваши права нарушены, можно обратиться в
Роскомнадзор.</p>

<h2>6. Сами проекты</h2>
<p>Arsound и моды для RimWorld не отправляют данные Получателю. Что приложение отправляет на сторонние сервисы (например,
названия треков и исполнителей в Last.fm для рекомендаций), описано в <a href="{ARSOUND_URL}">README проекта</a>; эти
функции настраиваются пользователем.</p>

<h2>7. Изменения</h2>
<p>Актуальная версия всегда на этой странице. Новая редакция вступает в силу с момента публикации.</p>

<h2>Контакты</h2>
{contact_ru()}
""")

RU["terms"] = ("Пользовательское соглашение", f"""
<h1>Пользовательское соглашение</h1>
<p class="lead">Дата последнего обновления: {UPDATED_RU}</p>

<h2>1. Общие положения</h2>
<p>1.1. Соглашение определяет условия использования сайта и проектов {NAME} (далее — Автор): приложения Arsound и модов для
RimWorld. Пользуясь ими, вы принимаете условия Соглашения.</p>
<p>1.2. Проекты распространяются бесплатно, с открытым исходным кодом, на условиях лицензий, указанных в их репозиториях.
Пожертвования регулируются отдельно — <a href="offer.html">публичной офертой</a>.</p>

<h2>2. Неофициальные проекты</h2>
<p>2.1. Arsound — неофициальный проект. Он не связан и не одобрен SoundCloud, ReVanced, Valve, Ludeon Studios и другими
правообладателями. Названия и товарные знаки принадлежат их владельцам.</p>
<p>2.2. Пользователь сам отвечает за соблюдение условий сервисов, с которыми работает Arsound (в частности пользовательского
соглашения SoundCloud и законов об авторском праве), и за то, как использует загруженные материалы. Автор не предоставляет
доступа к платному контенту, не хранит и не раздаёт чужие треки.</p>

<h2>3. Отсутствие гарантий</h2>
<p>3.1. Проекты предоставляются «как есть». Автор не гарантирует бесперебойную работу, совместимость с будущими версиями
SoundCloud, RimWorld и Android, и не отвечает за косвенные убытки, потерю данных или блокировку аккаунтов у сторонних сервисов.</p>
<p>3.2. Установка и использование — на риск пользователя. Рекомендуется делать резервные копии сохранений и данных.</p>

<h2>4. Пожертвования</h2>
<p>4.1. Пожертвование добровольно, ничего не открывает и не даёт приоритета в поддержке, функциях или исправлениях.</p>
<p>4.2. Условия, размер и возврат — в <a href="offer.html">оферте</a>.</p>

<h2>5. Изменения</h2>
<p>Автор может менять Соглашение; актуальная версия — на этой странице.</p>

<h2>6. Применимое право</h2>
<p>Право Российской Федерации. Споры решаются путём переговоров, а при недостижении согласия — по законодательству РФ.</p>

<h2>Контакты</h2>
{contact_ru()}
""")

# ------------------------------------------------------------------ EN
EN = {}

EN["index"] = ("Support the projects", f"""
<h1>Support the projects</h1>
<p class="lead">A page for voluntary donations to an independent developer: the Arsound app and RimWorld mods.</p>

<div class="card">
<h3>This is not a shop</h3>
<p>Nothing is sold here. Every project is free for everyone, with or without a donation. A donation is a voluntary gift to
the developer: it unlocks no features, gives no advantages and creates no obligations beyond those in the
<a href="offer.html">public donation offer</a>.</p>
</div>

<h2>What you support</h2>
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

<h2>How to donate</h2>
<p>Any amount from {MIN_AMOUNT} to {MAX_AMOUNT} RUB per payment. The money goes to development: time for new versions, test
devices and infrastructure. After the payment a self-employed receipt is sent to the e-mail you give.</p>
{pay_en()}
<p class="muted">By donating you accept the <a href="offer.html">public offer</a>. A donation is refunded only in the cases of
section 5 of the offer.</p>

<h2>Who receives donations</h2>
{contact_en()}
""")

EN["offer"] = ("Public donation offer", f"""
<h1>Public offer for a voluntary donation</h1>
<p class="lead">Last updated: {UPDATED_EN}. The Russian version prevails in case of discrepancy.</p>
<p>The projects are free for everyone. This document governs voluntary donations only: they are not payment for goods, work
or services and give no additional rights or features.</p>

<h2>1. Terms</h2>
<p>1.1. <b>Recipient</b> — {NAME_EN}, an individual under the Russian special tax regime "Tax on Professional Income"
(self-employed), taxpayer ID {INN}.</p>
<p>1.2. <b>Donor</b> — a legally capable individual who voluntarily transfers money.</p>
<p>1.3. <b>Projects</b> — the Arsound app (open-source patches for the Android SoundCloud app) and the RimWorld mods listed on
the <a href="index.html">main page</a>.</p>
<p>1.4. <b>Donation</b> — a gratuitous, voluntary transfer of money to the Recipient for the purposes in clause 2.2.</p>

<h2>2. Subject</h2>
<p>2.1. This is a public offer to conclude a donation agreement under Articles 572 and 582 of the Civil Code of the Russian
Federation.</p>
<p>2.2. A donation supports and develops the Projects — free, open-source software available to an unlimited number of people at
no cost (a public-benefit purpose): development time, testing, test devices, and servers and services needed for building and
distribution.</p>
<p>2.3. A donation is voluntary and gratuitous. It is not payment for goods, work or services and does not oblige the Recipient
to provide any goods, services, extra or priority features, advantages or other consideration. The Projects are available to
everyone equally and free of charge, regardless of whether or how much was donated.</p>
<p>2.4. The agreement is concluded when the donation is transferred; the transfer is full and unconditional acceptance of this offer.</p>
<p>2.5. Published at <a href="{SITE_URL}/en/offer.html">{SITE_URL}/en/offer.html</a>.</p>

<h2>3. Amount and payment</h2>
<p>3.1. The Donor chooses the amount, from {MIN_AMOUNT} to {MAX_AMOUNT} RUB per payment.</p>
<p>3.2. Payment is made in Russian rubles through payment services available at the time. Card details are entered on the payment
service's side; the Recipient does not receive them.</p>
<p>3.3. Before paying, the Donor gives an e-mail address to which a receipt is sent as required by the professional income tax law.</p>
<p>3.4. The donation is made when the payment service confirms the operation.</p>

<h2>4. Rights and obligations</h2>
<p>4.1. The Recipient will use the funds for the purposes in clause 2.2, send a receipt to the given address and handle the
Donor's data under the <a href="privacy.html">Privacy Policy</a>.</p>
<p>4.2. The Recipient may spend donations at their discretion within those purposes, without reporting to the Donor.</p>
<p>4.3. The Donor confirms the transfer is voluntary, understands it is gratuitous and expects nothing in return.</p>
<p>4.4. The Donor guarantees the funds are lawfully theirs. A Donor under 18 donates with the consent of a parent or guardian.</p>

<h2>5. Refunds</h2>
<p>5.1. Because a donation is gratuitous, it is generally not refundable.</p>
<p>5.2. A refund is possible in exceptional cases: a double or erroneous charge caused by a technical failure; a wrong amount caused
by an obvious technical error — if requested within a reasonable time.</p>
<p>5.3. To request a refund, write to the e-mail in "Contacts and details" with the date, amount and the e-mail the receipt went to.
Do not post these details in public places (chats, trackers).
Review takes up to 7 business days. The refund goes back by the same method.</p>

<h2>6. Final provisions</h2>
<p>6.1. Governed by the law of the Russian Federation.</p>
<p>6.2. Disputes are settled by negotiation; failing that, under the legislation of the Russian Federation.</p>
<p>6.3. The Recipient may change this offer. The current version is always at the address in clause 2.5; changes do not affect
donations already made.</p>

<h2>Contacts and details</h2>
{contact_en()}
""")

EN["privacy"] = ("Privacy policy", f"""
<h1>Privacy policy</h1>
<p class="lead">Last updated: {UPDATED_EN}. The Russian version prevails in case of discrepancy.</p>

<h2>1. Who we are</h2>
<p>The data operator is {NAME_EN}, self-employed, taxpayer ID {INN}. Contacts are listed below.</p>

<h2>2. This site</h2>
<p>The site is static: no accounts, forms, cookies, visit counters, ads or third-party analytics. It is hosted on GitHub Pages;
like any web server, GitHub may log technical request data (IP address, browser, time) under its own policy — the Recipient has
no access to it.</p>

<h2>3. Donations</h2>
<p>For a donation we process the amount, date and status of the payment, the operation ID, and the e-mail you gave for the
receipt. Payment happens on the payment service's side; we never receive or store your card number, CVC or cardholder name. The
payment service{" (" + PAY_SERVICE + ")" if PAY_SERVICE else ""} processes data under its own policy.</p>
<p>By paying you consent to the processing of the data above under this Policy. You may withdraw consent by writing to the contacts
below; data the law requires us to keep is retained for the statutory period.</p>
<p>To issue a receipt, payment details are entered into the "My Tax" app of the Federal Tax Service of Russia.</p>

<h2>4. Purpose and retention</h2>
<p>Data is used only to accept the payment, send the receipt, answer requests and meet tax and accounting duties. It is not sold
or passed to third parties, except the payment service and the tax service as needed for the payment and reporting. Payment records
are kept for the statutory tax and accounting period (at least 4 years); requests — as long as needed to resolve them.</p>

<h2>5. Your rights</h2>
<p>You may ask what data we hold, and ask to correct or delete it unless the law requires keeping it. Write to the contacts below;
we reply within 10 business days. If you believe your rights are violated, you may contact Roskomnadzor, the Russian data
protection authority.</p>

<h2>6. The projects themselves</h2>
<p>Arsound and the RimWorld mods do not send data to the Recipient. What the app sends to third-party services (for example track and
artist names to Last.fm for recommendations) is described in the <a href="{ARSOUND_URL}">project README</a>; these features are
user-configurable.</p>

<h2>7. Changes</h2>
<p>The current version is always on this page. A new version takes effect when published.</p>

<h2>Contacts</h2>
{contact_en()}
""")

EN["terms"] = ("Terms of use", f"""
<h1>Terms of use</h1>
<p class="lead">Last updated: {UPDATED_EN}. The Russian version prevails in case of discrepancy.</p>

<h2>1. General</h2>
<p>1.1. These terms govern the use of this site and the projects of {NAME_EN} (the Author): the Arsound app and RimWorld mods.
By using them you accept these terms.</p>
<p>1.2. The projects are free and open-source under the licenses stated in their repositories. Donations are governed
separately by the <a href="offer.html">public offer</a>.</p>

<h2>2. Unofficial projects</h2>
<p>2.1. Arsound is unofficial. It is not affiliated with or endorsed by SoundCloud, ReVanced, Valve, Ludeon Studios or other
rights holders. Names and trademarks belong to their owners.</p>
<p>2.2. Users are responsible for complying with the terms of services Arsound works with (notably SoundCloud's terms and
copyright law) and for how they use downloaded material. The Author does not provide access to paid content and does not store
or distribute third-party tracks.</p>

<h2>3. No warranty</h2>
<p>3.1. The projects are provided "as is". The Author does not guarantee uninterrupted operation or compatibility with future
versions of SoundCloud, RimWorld or Android, and is not liable for indirect losses, data loss or account restrictions at
third-party services.</p>
<p>3.2. Installation and use are at your own risk. Back up saves and data.</p>

<h2>4. Donations</h2>
<p>4.1. A donation is voluntary, unlocks nothing and gives no priority in support, features or fixes.</p>
<p>4.2. Terms, amounts and refunds are in the <a href="offer.html">offer</a>.</p>

<h2>5. Changes</h2>
<p>The Author may change these terms; the current version is on this page.</p>

<h2>6. Governing law</h2>
<p>Law of the Russian Federation. Disputes are settled by negotiation; failing that, under Russian legislation.</p>

<h2>Contacts</h2>
{contact_en()}
""")

NAV = {
    "ru": [("index", "Главная"), ("offer", "Оферта"), ("privacy", "Конфиденциальность"), ("terms", "Соглашение")],
    "en": [("index", "Home"), ("offer", "Offer"), ("privacy", "Privacy"), ("terms", "Terms")],
}


def render(lang, key, title, body):
    pages = RU if lang == "ru" else EN
    other = "en" if lang == "ru" else "ru"
    nav = "".join(
        f'<a href="{k}.html"{" class=cur" if k == key else ""}>{t}</a>' for k, t in NAV[lang]
    )
    switch_href = (f"en/{key}.html" if lang == "ru" else f"../{key}.html")
    switch_text = "English" if lang == "ru" else "Русский"
    brand = "Поддержка проектов" if lang == "ru" else "Support the projects"
    foot = f"{NAME} · ИНН {INN}" if lang == "ru" else f"{NAME_EN} · INN {INN}"
    tl, td = ("Светлая тема", "Тёмная тема") if lang == "ru" else ("Light theme", "Dark theme")
    desc = ("Добровольные пожертвования независимому разработчику: Arsound и моды RimWorld."
            if lang == "ru" else "Voluntary donations to an independent developer: Arsound and RimWorld mods.")
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
<div class="bar"><header><a class="brand" href="index.html">{LOGO}{brand}</a>{nav}<a href="{switch_href}">{switch_text}</a><button id="theme" type="button" data-l="{tl}" data-d="{td}"></button></header></div>
<main>{wave_svg() if key == "index" else ""}{body}</main>
<footer>{foot}</footer>
<script>{THEME_JS}</script>
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
    if not CONTACT_EMAIL:
        print("WARNING: CONTACT_EMAIL пуст — в контактах стоит заглушка, не публиковать")
    print("ok")


if __name__ == "__main__":
    main()
