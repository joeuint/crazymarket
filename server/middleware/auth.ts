export default defineEventHandler(async (event) => {
    const session = getCookie(event, 'session_token');

    if (!session) {
        return;
    }

    event.context.user = (await auth.getUserBySessionToken(session)) ?? undefined;

    if (!event.context.user) {
        return;
    }

    event.context.profile = (await auth.getProfileByUser(event.context.user)) ?? undefined;
});
