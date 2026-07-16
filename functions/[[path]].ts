export async function onRequest(context) {
  const { request, env } = context;
  const url = new URL(request.url);
  const hostname = url.hostname;

  let filePath = url.pathname;
  if (filePath === '/' || filePath.endsWith('/')) {
    filePath += 'index.html';
  }

  if (hostname === 'en.jogomahjong.com') {
    filePath = '/en' + filePath;
  }

  try {
    const file = await env.ASSETS.fetch(new Request(filePath, { headers: request.headers }));
    if (file.status === 200) {
      return file;
    }
  } catch (e) {}

  if (hostname === 'en.jogomahjong.com') {
    try {
      const fallback = await env.ASSETS.fetch(new Request('/en/index.html', { headers: request.headers }));
      if (fallback.status === 200) {
        return fallback;
      }
    } catch (e) {}
  }

  try {
    const defaultFile = await env.ASSETS.fetch(new Request('/index.html', { headers: request.headers }));
    if (defaultFile.status === 200) {
      return defaultFile;
    }
  } catch (e) {}

  return new Response('Not found', { status: 404 });
}