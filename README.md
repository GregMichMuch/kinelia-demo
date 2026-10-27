# Kinelia demo playlist

This repository hosts a **legal demo playlist** for Kinelia, an Android and Android TV video player.
Kinelia provides no content. This playlist exists so that app reviewers and testers can try the player
without any subscription.

Playlist address: `https://gregmichmuch.github.io/kinelia-demo/demo.m3u`

It contains only:
- films released by their authors under **Creative Commons** licenses;
- **public test streams** offered for testing video players, under invented names.

No real TV channel, broadcaster or streaming service is included.
Kinelia is not affiliated with or endorsed by any of the authors below.

## Credits and licenses

| Work | Author | License |
|---|---|---|
| Big Buck Bunny (2008), 2013 "sunflower" re-render | (c) copyright 2008, Blender Foundation, www.bigbuckbunny.org; 4K / 60 fps changes (c) copyright 2013 Janus B. Kristensen | CC BY 3.0 |
| Sintel (2010) | (c) copyright Blender Foundation, durian.blender.org | CC BY 3.0 |
| Elephants Dream (2006) | Blender Foundation / Netherlands Media Art Institute, orange.blender.org | CC BY 2.5 |
| Sprite Fright (2021) | (CC) Blender Foundation, studio.blender.org | CC BY 4.0 |
| Caminandes 1: Llama Drama (2013), 2: Gran Dillama (2013), 3: Llamigos (2016) | Blender Foundation / Blender Institute, caminandes.com (files hosted on the Internet Archive) | CC BY 3.0 |

License texts: https://creativecommons.org/licenses/

Logos and trademarks (including the Blender, project and Creative Commons logos) are not covered by these licenses and are not used here.
Film and series posters in `posters/` are still frames taken from the works above, cropped and with the title added
(changes made for this demo); they are shared under the same license as the work they come from.
The two demo channel images (colour bars) were created for this demo.

Live demo channels use public test streams provided for player testing by their respective hosts
(ireplay.tv test stream, Mux test streams). Their content is Blender Foundation Creative Commons footage.

## Maintenance

Before every Google Play review, every line of `demo.m3u` must be played once (VLC or Kinelia).
A dead link is replaced or removed, never left in place.

## Legal pages of the Kinelia app

`legal/privacy.html` (privacy policy) and `legal/terms.html` (terms of use), in English, French and Spanish:

- https://gregmichmuch.github.io/kinelia-demo/legal/privacy.html
- https://gregmichmuch.github.io/kinelia-demo/legal/terms.html

They are generated from the app's own texts (`assets/legal/*.md` in the Kinelia source) by `tool/build_legal_pages.py`; do not edit the HTML by hand.
