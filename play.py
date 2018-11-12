import re
for i in range(2):

    page = """<span itemprop='position'>#2</span>
                   </div>
                   <div class='post' itemprop='articleBody'>
                     <p>Hey <a class="mention" href="/u/Dag">@Dag</a>- I’m not sure I understand what you’re trying to do, but the thread on the tether connector is M5x0.8. Best of luck!</p>
             <p>-Eric</p>
                   </div>
                   <meta itemprop='interactionCount' content='UserLikes:1'>
                   <meta itemprop='interactionCount' content='UserComments:1'>
                   <meta itemprop='headline' content='What thread for the tether connection?'>
                   <hr>
               </div>
               <div itemscope itemtype='http://schema.org/DiscussionForumPosting'>
                   <div class='creator'>
                     <span>
                       <a href='/u/Dag'><b itemprop='author'>Dag</b></a>

                        <time datetime='2018-10-10T16:04:14Z' itemprop='datePublished'>
                          2018-10-10 16:04:14 UTC
                        </time>
                     </span>"""
    texts = re.findall('<p>(.*?)</p>', page, re.M|re.S)
    time = re.findall('<time>(.*?)</time>', page, re.M|re.S)

    print(texts,time)

