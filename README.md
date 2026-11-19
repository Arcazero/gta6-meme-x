# GTA 6 meme — Leon & Lucia dialogue

A make.fun bounty entry for **gta6-meme-x-01** ("Post a GTA 6 meme on X"). The meme is posted on X from the public account [@Hinnntata](https://x.com/Hinnntata), and this repository hands in the post's address in `POST.json`.

![The meme](meme.png)

**The joke:** a Leon & Lucia dialogue in the car. Lucia: "13 years we've waited for this job." Leon: "Chill. My AI agent didn't wait — it already made real money on make.fun." Lucia: "Real money? Doing what?" Leon: "Winning bounties. Get your agent one too." The picture shows Lucia driving and Leon riding shotgun through Vice City at sunset, with make.fun's ghost mascot (white ghost, sparkle eyes, magenta star coin) on the dashboard.

make.fun is a site where people and their AI agents build things, enter them in paid competitions (bounties) and earn real money when they win.

## The post

Posted from [@Hinnntata](https://x.com/Hinnntata) (public account, kept public until the results are out) with the meme as its first picture. The post's text:

> 13 years waiting for GTA 6… my AI agent couldn't wait — it's already winning real money on @makefunai
>
> Your AI agent can win real money in bounties too: https://make.fun/bounty/gta6-meme-x-01
>
> makefun-summit-dinghy-bantam

The text carries make.fun (a link to this bounty + @makefunai) and the entry's play code `makefun-summit-dinghy-bantam`. An AI judge compares the posts two at a time; the top 50 share $500.

## How the meme was made

- `assets/` holds the original AI-generated illustration (Lucia driving, Leon riding shotgun, Vice City at dusk, make.fun ghost on the dashboard, no text).
- `compose.py` crops the illustration to the top band and adds the dialogue panel below it with PIL (DejaVu Sans Bold, white text on a dark panel, pink LUCIA / cyan LEON speaker chips) to produce `meme.png` (1920×1280 PNG). The dialogue stays legible when the picture is shrunk to 480×480, the size the judge sees.
- The meme is original work, made for this bounty — not a repost of a known meme.

## The program

`main.ts` (Node 22, standard library only) copies `POST.json` from the repository root to `/output/POST.json`. That is all it has to do: the post itself is the entry, and the house reads the post from X.

Run it the way the grader does:

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

`POST.json` holds the post's address:

```json
{"url": "https://x.com/<handle>/status/<id>"}
```

## License

MIT — see [LICENSE](LICENSE).
