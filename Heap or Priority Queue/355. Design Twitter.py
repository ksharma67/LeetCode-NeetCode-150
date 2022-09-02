from typing import List
import heapq
from collections import defaultdict, deque



class Twitter:

    def __init__(self):
        self.users = defaultdict(set) # map: userId -> {followeeId, ...}
        self.tweets = defaultdict(deque) # map: userId -> deque of size 10
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].appendleft((self.time, tweetId))
        while len(self.tweets[userId]) > 10:
            self.tweets[userId].pop()

    def getNewsFeed(self, userId: int) -> List[int]:
        allfeeds = []
        allfeeds.extend(self.tweets[userId])
        for followee in self.users[userId]:
            allfeeds.extend(self.tweets[followee])
        return [tweetId for _, tweetId in heapq.nlargest(10, allfeeds)]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)
