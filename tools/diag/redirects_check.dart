import 'dart:io';

/// Suit les renvois (codes 301, 302, 303, 307, 308) d'une adresse de lecture
/// et rend l'adresse finale, pour la donner directement au moteur principal
/// (essai de la V1.1, « cause du moteur principal », activé dans les outils
/// de test). En cas de doute (erreur, délai, réponse inattendue), rend
/// l'adresse d'origine : la lecture se fait alors comme avant.
///
/// L'adresse n'est jamais journalisée.
class RedirectResolver {
  RedirectResolver._();

  static const maxHops = 5;
  static const timeout = Duration(seconds: 5);

  /// Remplaçable dans les tests.
  static Future<String> Function(String url) resolve = _resolve;

  static Future<String> _resolve(String url) async {
    final current = Uri.tryParse(url);
    if (current == null || !(current.isScheme('http') || current.isScheme('https'))) return url;
    final client = HttpClient()
      ..connectionTimeout = timeout
      ..autoUncompress = false;
    try {
      return await _follow(client, current).timeout(timeout * 2, onTimeout: () => url);
    } catch (_) {
      return url;
    } finally {
      client.close(force: true);
    }
  }

  static Future<String> _follow(HttpClient client, Uri start) async {
    var current = start;
    for (var hop = 0; hop < maxHops; hop++) {
      final request = await client.headUrl(current).timeout(timeout);
      request.followRedirects = false;
      final response = await request.close().timeout(timeout);
      await response.drain<void>().catchError((_) {});
      final location = response.headers.value(HttpHeaders.locationHeader);
      if (!response.isRedirect || location == null || location.isEmpty) return current.toString();
      final next = current.resolve(location);
      if (!(next.isScheme('http') || next.isScheme('https'))) return current.toString();
      current = next;
    }
    return current.toString();
  }
}

Future<void> main(List<String> args) async {
  final urls = File(args[0]).readAsLinesSync().where((l) => l.contains('archive.org/download')).map((l) => l.trim());
  for (final url in urls) {
    final parsed = Uri.tryParse(url);
    stdout.writeln('== $url');
    stdout.writeln('   Uri.toString identique : ${parsed?.toString() == url} (${parsed?.toString()})');
    final c = HttpClient();
    try {
      final req = await c.headUrl(parsed!);
      req.followRedirects = false;
      final res = await req.close();
      await res.drain<void>();
      stdout.writeln('   HEAD : ${res.statusCode} isRedirect=${res.isRedirect} location=${res.headers.value('location')}');
    } catch (e) {
      stdout.writeln('   HEAD : exception $e');
    } finally {
      c.close(force: true);
    }
    final w = Stopwatch()..start();
    final r = await RedirectResolver.resolve(url);
    stdout.writeln('   resolve (${w.elapsedMilliseconds} ms) : ${r == url ? 'INCHANGÉE' : r}');
  }
}
