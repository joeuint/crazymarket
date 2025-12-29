import type { H3Context } from 'h3';
import type { User } from '../lib/generated/prisma/client';

User;

declare module 'h3' {
    interface H3EventContext {
        user?: User;
    }
}
