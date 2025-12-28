import type { User, Profile } from "~~/lib/generated/prisma/client";

export default defineEventHandler(
  async (event): Promise<{ user: User; profile: Profile } | undefined> => {
    if (event.context.user && event.context.profile) {
      return {
        user: event.context.user,
        profile: event.context.profile,
      };
    }

    setResponseStatus(event, 401);

    return;
  },
);
