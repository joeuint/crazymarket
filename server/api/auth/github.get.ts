import { generateState } from 'arctic';

export default defineEventHandler(async (event) => {
    const state = generateState();
    const url = github.createAuthorizationURL(state, []);

    setCookie(event, 'github_oauth_state', state, {
        httpOnly: true,
        secure: process.env.NODE_ENV === 'production',
        sameSite: 'lax',
        maxAge: 10 * 60, // 10 minutes
        path: '/',
    });

    return sendRedirect(event, url.toString(), 302);
});
