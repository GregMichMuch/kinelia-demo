"""Single source of truth for the Kinelia demo playlist.

Every film below is released by its authors under a Creative Commons licence
(or dedicated to the public domain). Every channel is an invented name over a
public test stream offered for player testing. No real channel, broadcaster or
streaming service is used anywhere in this repository.
"""

PAGES = "https://gregmichmuch.github.io/kinelia-demo"

# ---------------------------------------------------------------------------
# Films: (poster slug, title, year, group, url, author, licence, palette, motif)
# ---------------------------------------------------------------------------
FILMS = [
    dict(slug="big-buck-bunny", title="Big Buck Bunny", year=2008, group="Animation",
         url="https://archive.org/download/BigBuckBunny_124/Content/big_buck_bunny_720p_surround.mp4",
         author="Blender Foundation", licence="CC BY 3.0", existing=True),
    dict(slug="elephants-dream", title="Elephants Dream", year=2006, group="Sci-Fi",
         url="https://download.blender.org/ED/elephantsdream-720-h264-st-aac.mov",
         author="Blender Foundation / Netherlands Media Art Institute", licence="CC BY 2.5", existing=True),
    dict(slug="sintel", title="Sintel", year=2010, group="Fantasy",
         url="https://download.blender.org/demo/movies/Sintel.2010.1080p.mkv",
         author="Blender Foundation", licence="CC BY 3.0", existing=True),
    dict(slug="tears-of-steel", title="Tears of Steel", year=2012, group="Sci-Fi",
         url="https://download.blender.org/demo/movies/ToS/tears_of_steel_720p.mov",
         author="Blender Foundation", licence="CC BY 3.0",
         palette=("#0b1d2a", "#3a6073", "#e6eef2"), motif="grid"),
    dict(slug="cosmos-laundromat", title="Cosmos Laundromat", year=2015, group="Fantasy",
         url="https://archive.org/download/CosmosLaundromatFirstCycle/Cosmos%20Laundromat%20-%20First%20Cycle%20(1080p).mp4",
         author="Blender Foundation", licence="CC BY 4.0",
         palette=("#2b1055", "#d76d77", "#ffd7a8"), motif="orbits"),
    dict(slug="glass-half", title="Glass Half", year=2015, group="Comedy",
         url="https://archive.org/download/GlassHalf1080p/Glass%20Half-1080p.mp4",
         author="Blender Foundation", licence="CC BY 3.0",
         palette=("#f2e8cf", "#bc4749", "#1d1d1b"), motif="split"),
    dict(slug="spring", title="Spring", year=2019, group="Fantasy",
         url="https://archive.org/download/spring_blenderopenmovie/Spring%20-%20Blender%20Open%20Movie%20-%20YouTube.mp4",
         author="Blender Foundation", licence="CC BY 4.0",
         palette=("#0f3443", "#34e89e", "#f1fff7"), motif="mountains"),
    dict(slug="coffee-run", title="Coffee Run", year=2020, group="Animation",
         url="https://archive.org/download/coffee-run/Coffee%20Run.mp4",
         author="Blender Foundation", licence="CC BY 4.0",
         palette=("#3e2723", "#ff8f00", "#fff3e0"), motif="rings"),
    dict(slug="sprite-fright", title="Sprite Fright", year=2021, group="Comedy & Horror",
         url="https://archive.org/download/sprite-fright-2021/Sprite%20Fright%20(2021).mp4",
         author="Blender Foundation", licence="CC BY 4.0", existing=True),
    dict(slug="wing-it", title="Wing It!", year=2023, group="Comedy",
         url="https://archive.org/download/wing_it/wing_it.mp4",
         author="Blender Foundation", licence="CC BY 4.0",
         palette=("#87ceeb", "#ffb703", "#023047"), motif="sun"),
    dict(slug="sita-sings-the-blues", title="Sita Sings the Blues", year=2008, group="Musical",
         url="https://archive.org/download/sita-sings-the-blues/sita-sings-the-blues.mp4",
         author="Nina Paley", licence="CC0 1.0 (public domain dedication)",
         palette=("#5f0f40", "#fb8b24", "#ffe8d6"), motif="mandala"),
]

# Series: Caminandes (unchanged, see README).
SERIES = [
    dict(title="Caminandes S01E01 Llama Drama",
         url="https://archive.org/download/Caminandes1LlamaDrama/01_llama_drama_1080p.mp4"),
    dict(title="Caminandes S01E02 Gran Dillama",
         url="https://archive.org/download/Caminandes2GranDillama/02_gran_dillama_1080p.mp4"),
    dict(title="Caminandes S01E03 Llamigos",
         url="https://archive.org/download/CaminandesLlamigos/Caminandes_%20Llamigos-1080p.mp4"),
]

# ---------------------------------------------------------------------------
# Live channels: invented names over public test streams.
# ---------------------------------------------------------------------------
CHANNELS = [
    dict(id="orbis-cine.demo", name="Orbis Ciné", group="Cinema", logo="orbis-cine",
         url="https://test-streams.mux.dev/tos_ismc/main.m3u8",
         colors=("#1b1f3b", "#e3a740"), mark="ORBIS\nCINÉ"),
    dict(id="pixelia-kids.demo", name="Pixelia Kids", group="Kids", logo="pixelia-kids",
         url="https://test-streams.mux.dev/x36xhzz/x36xhzz.m3u8",
         colors=("#ffb703", "#023047"), mark="PIXELIA\nKIDS"),
    dict(id="lumo.demo", name="Lumo Animation", group="Kids", logo="lumo",
         url="https://ireplay.tv/test/blender.m3u8",
         colors=("#7b2cbf", "#f7f1ff"), mark="LUMO"),
    dict(id="meridian.demo", name="Meridian Discovery", group="Discovery", logo="meridian",
         url="https://demo.unified-streaming.com/k8s/features/stable/video/tears-of-steel/tears-of-steel.ism/.m3u8",
         colors=("#0f4c5c", "#9ad1d4"), mark="MERIDIAN"),
    dict(id="vela.demo", name="Vela Maison", group="Lifestyle", logo="vela",
         url="https://test-streams.mux.dev/x36xhzz/x36xhzz.m3u8",
         colors=("#f4e1d2", "#9c3d54"), mark="VELA"),
]
