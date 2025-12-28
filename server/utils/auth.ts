import crypto from "crypto";
import { get } from "http";
import { User, Profile } from "~~/lib/generated/prisma/client";

export const auth = {
  async createSessionToken(user: User): Promise<string> {
    const token = crypto.randomBytes(32).toString("hex");

    await prisma.userSession.create({
      data: {
        userId: user.id,
        token: token,
      },
    });

    return token;
  },

  async getUserById(userId: string): Promise<User | null> {
    return await prisma.user.findUnique({
      where: {
        id: userId,
      },
    });
  },

  async getUserBySessionToken(token: string): Promise<User | null> {
    const session = await prisma.userSession.findUnique({
      where: {
        token: token,
      },
      include: {
        user: true,
      },
    });

    return session ? session.user : null;
  },

  async getProfileByUser(user: User): Promise<Profile | null> {
    return await prisma.profile.findUnique({
      where: {
        userId: user.id,
      },
    });
  },
};
