class Facebook:
    def __init__(self, likes):
        self.likes = likes

    @staticmethod
    def total_likes(b1, b2, b3):
        return b1.likes + b2.likes + b3.likes


b1 = Facebook(100)
print(f"Uma's Likes: {b1.likes}")
b2 = Facebook(200)
print(f"Jay's Likes: {b2.likes}")
b3 = Facebook(300)
print(f"Bhavesh's Likes: {b3.likes}")
print(f"Total Likes: {Facebook.total_likes(b1, b2, b3)}")

