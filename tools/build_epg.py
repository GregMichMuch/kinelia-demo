"""Builds the invented TV guides of the demo channels: guide-en.xml.gz, guide-fr.xml.gz, guide-es.xml.gz.

Run: python3 tools/build_epg.py [start YYYY-MM-DD] [days]
Every programme below is invented for this demo. The guide must be rebuilt before
it runs out (see README, "Maintenance").
"""
import datetime as dt
import gzip
import random
import sys
from pathlib import Path
from xml.sax.saxutils import escape
from zoneinfo import ZoneInfo

sys.path.insert(0, str(Path(__file__).parent))
from catalog import CHANNELS  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
TZ = ZoneInfo("Europe/Paris")
LANGS = ("en", "fr", "es")

# Each programme: minutes, {lang: (title, description)}
P = {
    "orbis-cine.demo": [
        (105, {"en": ("The Lighthouse Keepers", "On a storm-battered island, two brothers who have not spoken in years must keep the light burning one last winter."),
               "fr": ("Les Gardiens du phare", "Sur une île battue par les tempêtes, deux frères brouillés depuis des années doivent garder le phare allumé un dernier hiver."),
               "es": ("Los guardianes del faro", "En una isla azotada por las tormentas, dos hermanos distanciados deben mantener el faro encendido un último invierno.")}),
        (98, {"en": ("Midnight in Valparaíso", "A night-shift taxi driver picks up a passenger who knows far too much about her past."),
              "fr": ("Minuit à Valparaíso", "Une chauffeuse de taxi de nuit prend une passagère qui en sait beaucoup trop sur son passé."),
              "es": ("Medianoche en Valparaíso", "Una taxista del turno de noche recoge a una pasajera que sabe demasiado sobre su pasado.")}),
        (92, {"en": ("The Summer of Kites", "Three cousins spend the holidays at their grandmother's seaside house and decide to win the village kite contest."),
              "fr": ("L'Été des cerfs-volants", "Trois cousins passent les vacances chez leur grand-mère au bord de la mer et décident de gagner le concours de cerfs-volants du village."),
              "es": ("El verano de las cometas", "Tres primos pasan las vacaciones en la casa de su abuela junto al mar y deciden ganar el concurso de cometas del pueblo.")}),
        (45, {"en": ("Short Films: the Open Selection", "A selection of animated short films released under free licences."),
              "fr": ("Courts métrages : la sélection libre", "Une sélection de courts métrages d'animation diffusés sous licence libre."),
              "es": ("Cortometrajes: la selección libre", "Una selección de cortometrajes de animación publicados con licencia libre.")}),
        (30, {"en": ("Orbis Cinema Magazine", "This week's releases, interviews and behind-the-scenes reports."),
              "fr": ("Orbis, le magazine du cinéma", "Les sorties de la semaine, des entretiens et des reportages en coulisses."),
              "es": ("Orbis, la revista del cine", "Los estrenos de la semana, entrevistas y reportajes entre bastidores.")}),
        (101, {"en": ("The Bridge in the Mist", "An engineer returns to her home town to repair the old bridge, and uncovers a secret buried with it."),
               "fr": ("Le Pont des brumes", "Une ingénieure revient dans sa ville natale pour réparer le vieux pont et découvre un secret enfoui avec lui."),
               "es": ("El puente de la niebla", "Una ingeniera vuelve a su pueblo natal para reparar el viejo puente y descubre un secreto enterrado con él.")}),
        (96, {"en": ("Operation Paper Crane", "Two retired spies are called back for one last, very clumsy mission."),
              "fr": ("Opération Grue de papier", "Deux espions à la retraite sont rappelés pour une dernière mission, très maladroite."),
              "es": ("Operación Grulla de papel", "Dos espías jubilados vuelven al servicio para una última misión, muy torpe.")}),
        (88, {"en": ("Under the Desert Stars", "A young astronomer and a nomad guide cross the dunes in search of a fallen meteorite."),
              "fr": ("Sous les étoiles du désert", "Une jeune astronome et un guide nomade traversent les dunes à la recherche d'une météorite."),
              "es": ("Bajo las estrellas del desierto", "Una joven astrónoma y un guía nómada cruzan las dunas en busca de un meteorito.")}),
    ],
    "pixelia-kids.demo": [
        (25, {"en": ("Pip and Lulu's Adventures", "Pip the fox and Lulu the hedgehog build a raft to explore the pond."),
              "fr": ("Les Aventures de Pip et Lulu", "Pip le renard et Lulu le hérisson construisent un radeau pour explorer l'étang."),
              "es": ("Las aventuras de Pip y Lulú", "Pip el zorro y Lulú el erizo construyen una balsa para explorar el estanque.")}),
        (20, {"en": ("The Big Workshop", "Easy crafts to make at home with paper, glue and cardboard."),
              "fr": ("Le Grand Atelier", "Des bricolages faciles à faire à la maison avec du papier, de la colle et du carton."),
              "es": ("El gran taller", "Manualidades fáciles para hacer en casa con papel, pegamento y cartón.")}),
        (15, {"en": ("Funny Creatures", "Every day, a surprising animal and its secrets."),
              "fr": ("Drôles de bêtes", "Chaque jour, un animal étonnant et ses secrets."),
              "es": ("Bichos curiosos", "Cada día, un animal sorprendente y sus secretos.")}),
        (25, {"en": ("Robot Rocket", "Bolt the little robot learns to fly his rocket to the Moon."),
              "fr": ("Robot Rocket", "Bolt, le petit robot, apprend à piloter sa fusée jusqu'à la Lune."),
              "es": ("Robot Rocket", "Bolt, el pequeño robot, aprende a pilotar su cohete hasta la Luna.")}),
        (15, {"en": ("The Story Cabin", "A bedtime story read and illustrated live."),
              "fr": ("La Cabane à histoires", "Une histoire du soir lue et illustrée en direct."),
              "es": ("La cabaña de los cuentos", "Un cuento para dormir leído e ilustrado en directo.")}),
        (25, {"en": ("Mission Blue Planet", "Little explorers discover how to protect oceans and forests."),
              "fr": ("Mission Planète bleue", "De petits explorateurs découvrent comment protéger les océans et les forêts."),
              "es": ("Misión Planeta Azul", "Pequeños exploradores descubren cómo proteger océanos y bosques.")}),
    ],
    "lumo.demo": [
        (60, {"en": ("Animation Night", "An evening of short animated films from independent studios."),
              "fr": ("Nuit de l'animation", "Une soirée de courts métrages d'animation de studios indépendants."),
              "es": ("Noche de animación", "Una velada de cortometrajes de animación de estudios independientes.")}),
        (30, {"en": ("Lumo Studio: Behind the Scenes", "How an animated film is made, from the first sketch to the final render."),
              "fr": ("Studio Lumo : dans les coulisses", "Comment se fabrique un film d'animation, du premier croquis à l'image finale."),
              "es": ("Estudio Lumo: entre bastidores", "Cómo se hace una película de animación, del primer boceto a la imagen final.")}),
        (25, {"en": ("The Mist Chronicles", "Nora and her flying cat explore a kingdom hidden in the clouds."),
              "fr": ("Les Chroniques de Brume", "Nora et son chat volant explorent un royaume caché dans les nuages."),
              "es": ("Las crónicas de la Bruma", "Nora y su gato volador exploran un reino escondido entre las nubes.")}),
        (20, {"en": ("Draw Me a Story", "An illustrator draws a story suggested by young viewers."),
              "fr": ("Dessine-moi une histoire", "Un illustrateur dessine une histoire proposée par les jeunes téléspectateurs."),
              "es": ("Dibújame una historia", "Un ilustrador dibuja una historia propuesta por los jóvenes espectadores.")}),
        (25, {"en": ("Pixel Quest", "Four friends trapped in a video game must reach the last level."),
              "fr": ("Pixel Quest", "Quatre amis coincés dans un jeu vidéo doivent atteindre le dernier niveau."),
              "es": ("Pixel Quest", "Cuatro amigos atrapados en un videojuego deben llegar al último nivel.")}),
    ],
    "meridian.demo": [
        (52, {"en": ("Iceland's Volcanoes", "Scientists camp at the foot of an awakening volcano."),
              "fr": ("Les Volcans d'Islande", "Des scientifiques campent au pied d'un volcan qui se réveille."),
              "es": ("Los volcanes de Islandia", "Científicos acampan al pie de un volcán que despierta.")}),
        (52, {"en": ("Secret Oceans", "Into the deep sea, where light never reaches."),
              "fr": ("Océans secrets", "Plongée dans les grands fonds, là où la lumière n'arrive jamais."),
              "es": ("Océanos secretos", "Inmersión en las profundidades, donde nunca llega la luz.")}),
        (45, {"en": ("Cities of Tomorrow", "Architects imagine greener, quieter cities."),
              "fr": ("Villes du futur", "Des architectes imaginent des villes plus vertes et plus calmes."),
              "es": ("Ciudades del futuro", "Arquitectos imaginan ciudades más verdes y tranquilas.")}),
        (52, {"en": ("On the Tea Roads", "From the mountains to the markets, the journey of a tea leaf."),
              "fr": ("Sur les routes du thé", "Des montagnes aux marchés, le voyage d'une feuille de thé."),
              "es": ("Por las rutas del té", "De las montañas a los mercados, el viaje de una hoja de té.")}),
        (45, {"en": ("The Bee Kingdom", "A year in the life of a hive."),
              "fr": ("Le Peuple des abeilles", "Une année dans la vie d'une ruche."),
              "es": ("El reino de las abejas", "Un año en la vida de una colmena.")}),
        (30, {"en": ("Starry Skies", "What to look for in the night sky this month."),
              "fr": ("Ciel étoilé", "Ce qu'il faut observer dans le ciel nocturne ce mois-ci."),
              "es": ("Cielos estrellados", "Qué observar en el cielo nocturno este mes.")}),
    ],
    "vela.demo": [
        (30, {"en": ("Vela Kitchen: Seasonal Flavours", "Three simple recipes with this week's vegetables."),
              "fr": ("Vela cuisine : saveurs de saison", "Trois recettes simples avec les légumes de la semaine."),
              "es": ("Cocina Vela: sabores de temporada", "Tres recetas sencillas con las verduras de la semana.")}),
        (45, {"en": ("Homes with Character", "A tour of a renovated farmhouse full of good ideas."),
              "fr": ("Maisons de caractère", "Visite d'une ferme rénovée pleine de bonnes idées."),
              "es": ("Casas con carácter", "Visita a una granja renovada llena de buenas ideas.")}),
        (30, {"en": ("In the Garden with Clara", "Clara prepares the garden for winter."),
              "fr": ("Au jardin avec Clara", "Clara prépare le jardin pour l'hiver."),
              "es": ("En el jardín con Clara", "Clara prepara el jardín para el invierno.")}),
        (50, {"en": ("Getaways", "A long weekend in a quiet coastal town."),
              "fr": ("Escapades", "Un long week-end dans une petite ville côtière tranquille."),
              "es": ("Escapadas", "Un fin de semana largo en un tranquilo pueblo costero.")}),
        (60, {"en": ("The Baking Challenge", "Four amateur bakers, one theme, one hour."),
              "fr": ("Le Défi pâtissier", "Quatre pâtissiers amateurs, un thème, une heure."),
              "es": ("El reto de repostería", "Cuatro reposteros aficionados, un tema, una hora.")}),
        (20, {"en": ("Morning Yoga", "A gentle session to start the day."),
              "fr": ("Yoga au réveil", "Une séance douce pour bien commencer la journée."),
              "es": ("Yoga al despertar", "Una sesión suave para empezar el día.")}),
    ],
}


def schedule(channel_id, start, end):
    pool = P[channel_id]
    rnd = random.Random(channel_id)
    t, last, out = start, None, []
    while t < end:
        choice = rnd.randrange(len(pool))
        if choice == last and len(pool) > 1:
            choice = (choice + 1) % len(pool)
        last = choice
        minutes, texts = pool[choice]
        stop = t + dt.timedelta(minutes=minutes)
        # programmes end (and the next one starts) on a 5-minute boundary, without gaps
        stop += dt.timedelta(minutes=(5 - stop.minute % 5) % 5)
        out.append((t, stop, texts))
        t = stop
    return out


def xmltv_time(t):
    return t.astimezone(dt.timezone.utc).strftime("%Y%m%d%H%M%S +0000")


def build(lang, start, end):
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<tv generator-info-name="kinelia-demo (invented guide)">']
    for ch in CHANNELS:
        lines.append(f'  <channel id="{ch["id"]}"><display-name>{escape(ch["name"])}</display-name></channel>')
    for ch in CHANNELS:
        for a, b, texts in schedule(ch["id"], start, end):
            title, desc = texts[lang]
            lines.append(
                f'  <programme start="{xmltv_time(a)}" stop="{xmltv_time(b)}" channel="{ch["id"]}">'
                f'<title lang="{lang}">{escape(title)}</title><desc lang="{lang}">{escape(desc)}</desc></programme>')
    lines.append("</tv>")
    return "\n".join(lines).encode("utf-8")


if __name__ == "__main__":
    day = dt.date.fromisoformat(sys.argv[1]) if len(sys.argv) > 1 else dt.date.today()
    days = int(sys.argv[2]) if len(sys.argv) > 2 else 120
    start = dt.datetime.combine(day - dt.timedelta(days=1), dt.time(0), TZ)
    end = start + dt.timedelta(days=days + 1)
    for lang in LANGS:
        data = build(lang, start, end)
        with gzip.GzipFile(ROOT / f"guide-{lang}.xml.gz", "wb", mtime=0) as f:
            f.write(data)
        print(lang, len(data), "bytes before compression")
    print("guide covers", start.date(), "to", end.date())
