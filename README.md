# Arsound Premium access

Static pages (RU + EN) for GitHub Pages: the premium access «Early access» for Arsound and the RimWorld mods, and the
legal texts for it (offer, terms, privacy). Premium access costs 500 RUB / 250 Telegram Stars (it can be paid in parts,
payments add up) and opens a private Telegram channel with test builds, priority for bug reports and ideas in the bot
@ArapplicationsBot, and a tag in the discussion chat. The wording matches the bot: payments are for premium access;
a payment above the price or after access is open is an «additional payment» (offer clause 2.3).

Edit settings at the top of `build.py`, then run `build.cmd` (or `python build.py`) and commit the generated `*.html`.

- `PAY_FORM_URL` — set to `https://arapplications.ru/pay` once ЮKassa is connected in the bot's server config:
  the site then shows a payment form; until then it only links to the bot.
- `POSTAL_ADDRESS` — postal address for the contacts block (the payment service asks for it); empty = no line.
- `ACCESS_AMOUNT` / `ACCESS_STARS` must match `ACCESS_RUB` / `ACCESS_STARS` in the bot's `/etc/arbot/arbot.env`.

Payments themselves are handled by the bot's server (repository `arapps-bot`): the form posts the amount there, the server
creates a ЮKassa payment, and after paying the user returns to the bot, which opens access.
