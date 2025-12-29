import type { Profile, User } from '~~/lib/generated/prisma/client';

import { auth } from '~~/server/utils/auth';

export const useUser = async () => {
    return useAsyncData<{ user: User; profile: Profile } | null>('user-session', async () => {
        if (import.meta.server) {
            const session = useCookie('session_token');

            if (!session.value) {
                return null;
            }

            const user = await auth.getUserBySessionToken(session.value);

            if (!user) {
                return null;
            }

            const profile = await auth.getProfileByUser(user);

            if (!profile) {
                return null;
            }

            return {
                user,
                profile,
            };
        }

        console.log('Fetching user data on client side');

        let data;
        try {
            data = await $fetch('/api/user');
        } catch (e) {
            console.log('Error fetching user data on client:', e);
            console.log('User is probably not logged in.');
            return null;
        }

        if (!data || !data.user || !data.profile) {
            console.error('Incomplete user data received on client:', data);
            return null;
        }

        return {
            user: data.user,
            profile: data.profile,
        };
    });
};
