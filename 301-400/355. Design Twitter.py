# Runtime: 104 ms, faster than 63.92% of Python3 online submissions
# Memory Usage: 19.3 MB, less than 5.26% of Python3 online submissions


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.index = 0
        self.twitters = dict()
        self.followers = dict()

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        if userId in self.twitters:
            self.twitters[userId].append((tweetId, self.index))
        else:
            self.twitters.setdefault(userId, [(tweetId, self.index)])
        self.index += 1

    def getNewsFeed(self, userId: int) -> list:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        tweets = []
        if userId in self.twitters:
            tweets += self.twitters[userId]
        if userId in self.followers:
            for followeeId in self.followers[userId]:
                if followeeId in self.twitters:
                    tweets += self.twitters[followeeId]
        return [tweet[0] for tweet in sorted(tweets, key=lambda t: t[1], reverse=True)[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId == followeeId:
            return
        if followerId in self.followers:
            self.followers[followerId].add(followeeId)
        else:
            self.followers.setdefault(followerId, {followeeId})

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId == followeeId:
            return
        if followerId in self.followers:
            if followeeId in self.followers[followerId]:
                self.followers[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
