facebook_posts = [{'Likes':11, 'Comment':9},
                  {'Likes':22, 'Comment':6},
                  {'Share':23, 'Comment':12},
                  {'Share':13, 'Comment':11},
                  {'Likes':17, 'Comment':23}]
likes = 0
for posts in facebook_posts:
    try: 
        likes = likes + posts['Likes']
    except KeyError:
        pass        
    
print (likes)