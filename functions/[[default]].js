export async function onRequest(context) {
  const { request, env } = context;
  const url = new URL(request.url);

  // Only rewrite for en.jogomahjong.com
  if (url.hostname !== 'en.jogomahjong.com') {
    return env.ASSETS.fetch(request);
  }

  // For en.jogomahjong.com, serve from /en/ directory
  let path = url.pathname;

  // Skip assets - serve them from root
  if (path.startsWith('/assets/') || path.startsWith('/favicon') || path.startsWith('/ads.txt')) {
    return env.ASSETS.fetch(request);
  }

  // Rewrite path to /en/ prefix
  if (!path.startsWith('/en/')) {
    const newUrl = new URL(request.url);
    newUrl.pathname = '/en' + path;
    const newReq = new Request(newUrl, request);
    return env.ASSETS.fetch(newReq);
  }

  return env.ASSETS.fetch(request);
}