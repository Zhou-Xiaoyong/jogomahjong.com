export async function onRequest(context) {
  const { request, env } = context;
  const url = new URL(request.url);

  // Only rewrite for English domain
  if (url.hostname !== 'en.jogomahjong.com') {
    return env.ASSETS.fetch(request);
  }

  let path = url.pathname;

  // Shared resources - serve from root
  if (path.startsWith('/assets/') ||
      path.startsWith('/favicon') ||
      path.startsWith('/ads.txt') ||
      path.startsWith('/robots.txt') ||
      path.startsWith('/sitemap.xml') ||
      path.startsWith('/mahjong-classico/mah-app/')) {
    return env.ASSETS.fetch(request);
  }

  // Already under /en/ - serve directly
  if (path.startsWith('/en/')) {
    return env.ASSETS.fetch(request);
  }

  // Rewrite to /en/ prefix for English domain
  let enPath = '/en' + path;
  if (enPath.endsWith('/')) {
    enPath += 'index.html';
  }

  const enUrl = new URL(request.url);
  enUrl.pathname = enPath;

  const enResponse = await env.ASSETS.fetch(enUrl.toString());
  if (enResponse.status === 200) {
    return enResponse;
  }

  // Fallback: try with index.html appended
  if (!enPath.endsWith('index.html')) {
    enUrl.pathname = enPath + '/index.html';
    const fallbackResponse = await env.ASSETS.fetch(enUrl.toString());
    if (fallbackResponse.status === 200) {
      return fallbackResponse;
    }
  }

  // Final fallback: serve from root (shared content)
  return env.ASSETS.fetch(request);
}