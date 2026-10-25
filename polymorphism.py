class Post :
    def render(self):
        raise NotImplementedError("SubClass must impliment render()")
class TextPost(Post) :
     def __init__(self,text):
        self.text = text

     def render(self):
         print(f"Text : {self.text}")

class ImagePost(Post):
    def __init__(self,image_url):
        self.image_url = image_url

    def render(self):
        print(f"Image : [render image from {self.image_url}]")

class Videopost(Post):
    def __init__(self, video_url) :
        self.video_url = video_url

    def render(self):
        print(f"video : [play video from {self.video_url}] ")


# post1 = TextPost("Hello, how are you.....!")

# post1.render()

# post2 = ImagePost("https://www.istockphoto.com/photos/photo-image-art")

# post2.render()


# post3 = Videopost("https://www.istockphoto.com/photos/photo-image-art")

# post3.render()

feed = [ TextPost("Hello, how are you.....!"),
        ImagePost("sunset.jpg"),
        TextPost("Another thought")

]

for post in feed :
    post.render()


        
    

