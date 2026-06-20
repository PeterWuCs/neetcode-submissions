class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.post = defaultdict(list)
        self.postCount = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.post[userId].append((- self.postCount, tweetId))
        self.postCount += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        all_possible_task = self.post[userId].copy()
        
        for followee in (self.following[userId]):
            if followee == userId:
                continue
            for tweet in self.post[followee]:
                all_possible_task.append(tweet)

        heapq.heapify(all_possible_task)

        result = []
        count = 10
        while all_possible_task and count > 0:
            a = heapq.heappop(all_possible_task)
            result.append(a[1])
            count -= 1

        return result
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        
