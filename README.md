# email_to_blog

This repo is used to update my blog post via eamil system. When I want to write some new blog, I just do it by sending an email to given address.
The server will check for new email every 10 minutes(can be configured), if new email arrives by allowed client(can be added), it will generate
the email context into webpage by hexo engine running on the server. The deploy it to the website.
The advantages of doing such a thing is that you can update your blog post almost everywhere anytime without the need of extra applications.
