export async function onRequest(context) {
  const { request, env } = context;
  const url = new URL(request.url);

  // For non-English domains, serve directly
  if (url.hostname !== 'en.jogomahjong.com') {
    return env.ASSETS.fetch(request);
  }

  let path = url.pathname;

  // Serve shared assets and embedded apps directly from root
  if (path.startsWith('/assets/') || path.startsWith('/favicon') || path.startsWith('/ads.txt') || path.startsWith('/robots.txt') || path.startsWith('/sitemap.xml') || path.startsWith('/mahjong-classico/mah-app/')) {
    return env.ASSETS.fetch(request);
  }

  // For en.jogomahjong.com, rewrite to /en/ prefix
  if (!path.startsWith('/en/')) {
    let enPath = '/en' + path;
    // Resolve directory to index.html
    if (enPath.endsWith('/')) {
      enPath += 'index.html';
    }
    // Try the English version
    const newUrl = new URL(request.url);
    newUrl.pathname = enPath;
    try {
      const response = await env.ASSETS.fetch(new Request(newUrl, request));
      if (response.status === 200) {
        return response;
      }
    } catch (e) {
      // Fall through to 404
    }
    // If English page doesn't exist, return 404 instead of serving Portuguese
    return new Response('Not found', { status: 404 });
  }

  return env.ASSETS.fetch(request);
}