# Kinelia demo playlist

This repository hosts a **legal demo playlist** for Kinelia, an Android and Android TV video player.
Kinelia provides no content. This playlist exists so that app reviewers and testers can try the player
without any subscription.

Playlist address: `https://gregmichmuch.github.io/kinelia-demo/demo.m3u`

It contains only:
- films released by their authors under **Creative Commons** licenses (or dedicated to the public domain);
- **public test streams** offered for testing video players, under **invented channel names**;
- an **invented TV guide** for those channels (no real programme or broadcaster).

TV guide addresses (enter one in the app's "TV guide URL" field; same channels, one language each):
- English: `https://gregmichmuch.github.io/kinelia-demo/guide-en.xml.gz`
- French: `https://gregmichmuch.github.io/kinelia-demo/guide-fr.xml.gz`
- Spanish: `https://gregmichmuch.github.io/kinelia-demo/guide-es.xml.gz`

No real TV channel, broadcaster or streaming service is included.
Kinelia is not affiliated with or endorsed by any of the authors below.

## Credits and licenses

| Work | Author | License |
|---|---|---|
| Big Buck Bunny (2008), 2013 "sunflower" re-render | (c) copyright 2008, Blender Foundation, www.bigbuckbunny.org; 4K / 60 fps changes (c) copyright 2013 Janus B. Kristensen | CC BY 3.0 |
| Sintel (2010) | (c) copyright Blender Foundation, durian.blender.org | CC BY 3.0 |
| Elephants Dream (2006) | Blender Foundation / Netherlands Media Art Institute, orange.blender.org | CC BY 2.5 |
| Sprite Fright (2021) | (CC) Blender Foundation, studio.blender.org | CC BY 4.0 |
| Tears of Steel (2012) | (CC) Blender Foundation, mango.blender.org | CC BY 3.0 |
| Cosmos Laundromat: First Cycle (2015) | (CC) Blender Foundation, gooseberry.blender.org (file hosted on the Internet Archive) | CC BY 4.0 |
| Glass Half (2015) | (CC) Blender Foundation, studio.blender.org (file hosted on the Internet Archive) | CC BY 3.0 |
| Hero (2018) | (CC) Blender Foundation, studio.blender.org (file hosted on the Internet Archive) | CC BY 4.0 |
| Spring (2019) | (CC) Blender Foundation, studio.blender.org (file hosted on the Internet Archive) | CC BY 4.0 |
| Coffee Run (2020) | (CC) Blender Foundation, studio.blender.org (file hosted on the Internet Archive) | CC BY 4.0 |
| Wing It! (2023) | (CC) Blender Foundation, studio.blender.org (file hosted on the Internet Archive) | CC BY 4.0 |
| Sita Sings the Blues (2008) | Nina Paley, sitasingstheblues.com (file hosted on the Internet Archive) | CC0 1.0 (public domain dedication) |
| Caminandes 1: Llama Drama (2013), 2: Gran Dillama (2013), 3: Llamigos (2016) | Blender Foundation / Blender Institute, caminandes.com (files hosted on the Internet Archive) | CC BY 3.0 |

License texts: https://creativecommons.org/licenses/

Logos and trademarks (including the Blender, project and Creative Commons logos) are not covered by these licenses and are not used here.
Posters of Big Buck Bunny, Sintel, Elephants Dream, Sprite Fright and Caminandes in `posters/` are still frames taken from
the works above, cropped and with the title added (changes made for this demo); they are shared under the same license
as the work they come from. The other film posters are original typographic designs made for this demo
(`tools/make_artwork.py`): they contain no frame, logo or artwork from the films.
Channel logos were created for this demo. Channel names (Orbis Ciné, Pixelia Kids, Lumo Animation, Meridian Discovery,
Vela Maison) and every programme of the TV guide are invented.

Live demo channels use public test streams provided for player testing by their respective hosts
(ireplay.tv test stream, Mux test streams, Unified Streaming demo, Akamai test stream). Except for the Akamai test
stream (test pattern), their content is Blender Foundation Creative Commons footage.

## Maintenance

`demo.m3u`, the posters and the guides are generated from `tools/catalog.py`:

```
python3 tools/build_playlist.py
python3 tools/make_artwork.py <folder with the Bricolage Grotesque and Instrument Sans fonts>
python3 tools/build_epg.py YYYY-MM-DD 120
```

Before every Google Play review, every line of `demo.m3u` must be played once (VLC or Kinelia).
A dead link is replaced or removed, never left in place.
The TV guide covers 120 days from its build date: **the current guides end on 26 February 2027**;
rebuild them before that date (and before any review that could happen after it).

## Legal pages of the Kinelia app

`legal/privacy.html` (privacy policy) and `legal/terms.html` (terms of use), in English, French and Spanish:

- https://gregmichmuch.github.io/kinelia-demo/legal/privacy.html
- https://gregmichmuch.github.io/kinelia-demo/legal/terms.html

They are generated from the app's own texts (`assets/legal/*.md` in the Kinelia source) by `tool/build_legal_pages.py`; do not edit the HTML by hand.
