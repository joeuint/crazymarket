/*
  Warnings:

  - A unique constraint covering the columns `[userId]` on the table `GithubConnection` will be added. If there are existing duplicate values, this will fail.

*/
-- CreateIndex
CREATE UNIQUE INDEX "GithubConnection_userId_key" ON "GithubConnection"("userId");
