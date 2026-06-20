class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.post = defaultdict(list)
        self.postCount = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        
        self.post[userId].append((self.postCount, tweetId))
        self.postCount -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        possible = []
        self.following[userId].add(userId)
        for followee in self.following[userId]:
            if self.post[followee]:
                index = len(self.post[followee]) - 1
                postCount, tweetId = self.post[followee][index]
                possible.append((postCount, tweetId, followee, index))

        heapq.heapify(possible)

        while possible and len(result) < 10:
            postCount, tweetId, followee, index = heapq.heappop(possible)
            result.append(tweetId)

            if index > 0:
                index -= 1
                postCount, tweetId = self.post[followee][index]
                heapq.heappush(possible, (postCount, tweetId, followee, index))

        return result
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        
