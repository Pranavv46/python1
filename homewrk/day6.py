"""
You are building a basic dashboard for a blog website. The blog has a list that stores the number of views for different blog posts.
Your task is to:
Loop through the given list of blog post views.
For each blog post:
If views > 1000, print "Trending"
If views between 500 and 1000, print "Average"
If views < 500, print "Low Traffic"
After the loop:
Print the total number of views
Print how many posts were "Trending"
Use this list for blog views:
blog_views = [150, 800, 2500, 600, 1200, 450, 3000]
"""
blog_views = [150, 800, 2500, 600, 1200, 450, 3000]
total_views = 0
trending_posts = 0

for views in blog_views:
    if views > 1000:
        print(f"{views} views - Trending")
        trending_posts += 1
    elif 500 <= views <= 1000:
        print(f"{views} views - Average")
    else:
        print(f"{views} views - Low Traffic")   
        total_views += views
        print("\nTotal number of views across all posts:", total_views)
print("Number of Trending posts:", trending_posts)