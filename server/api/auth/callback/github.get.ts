import { OAuth2Tokens } from 'arctic';

export default defineEventHandler(async (event) => {
    if (!event.node.req.url) {
        setResponseStatus(event, 400);
        return;
    }

    const { code, state } = getQuery(event);

    if (typeof code !== 'string' || typeof state !== 'string') {
        setResponseStatus(event, 400);
        return;
    }

    const cookieState = getCookie(event, 'github_oauth_state');

    if (!code || !state || state !== cookieState) {
        setResponseStatus(event, 400);
        return;
    }

    if (state !== cookieState) {
        setResponseStatus(event, 400);
        return;
    }

    let tokens: OAuth2Tokens;

    try {
        tokens = await github.validateAuthorizationCode(code);
    } catch (error) {
        setResponseStatus(event, 400);
        return;
    }

    const githubUserResponse = await $fetch('https://api.github.com/user', {
        headers: {
            Authorization: `Bearer ${tokens.accessToken()}`,
        },
    });

    let githubConnection = await prisma.githubConnection.findUnique({
        where: {
            githubId: (githubUserResponse as any).id.toString(),
        },
    });

    const githubId = (githubUserResponse as any).id.toString();
    const githubLogin = (githubUserResponse as any).login;

    let user = null;

    if (!githubConnection) {
        console.log('No existing GitHub connection found. Creating a new user!');
        user = await prisma.user.create({
            data: { username: githubLogin },
        });

        await prisma.githubConnection.create({
            data: { userId: user.id, githubId },
        });

        await prisma.profile.create({
            data: {
                userId: user.id,
                avatarUrl: (githubUserResponse as any).avatar_url,
            },
        });
    } else {
        user = await auth.getUserById(githubConnection.userId);

        if (!user) {
            setResponseStatus(event, 500);
            console.error('GitHub connection exists but no user found!');
            return;
        }
    }

    const token = await auth.createSessionToken(user);

    setCookie(event, 'session_token', token, {
        httpOnly: true,
        secure: true,
        sameSite: 'lax',
        path: '/',
    });

    return githubConnection ? sendRedirect(event, '/') : sendRedirect(event, '/welcome');
});
