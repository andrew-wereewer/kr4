from django.contrib.auth.models import User
from news.models import Author
from news.models import Category
from news.models import Post
from news.models import PostCategory
from news.models import Comment
from django.db.models import Sum

u1 = User.objects.create_user('u1')
u2 = User.objects.create_user('u2')
a1 = Author.objects.create(user=u1)
a2 = Author.objects.create(user=u2)

c1 = Category.objects.create(name='c1')
c2 = Category.objects.create(name='c2')
c3 = Category.objects.create(name='c3')
c4 = Category.objects.create(name='c4')

p1 = Post.objects.create(author=a2,title='Lorem ipsum',text='Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.')

p2 = Post.objects.create(author=a2,title='Sed ut perspiciatis',text='Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet.')

n1 = Post.objects.create(author=a1,isnews=True,title='At vero eos et',text='At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id est laborum et dolorum fuga.')

pc1 = PostCategory.objects.create(post=p1,category=c1)
pc2 = PostCategory.objects.create(post=p1,category=c2)

pc3 = PostCategory.objects.create(post=p2,category=c2)
pc4 = PostCategory.objects.create(post=p2,category=c4)

pc5 = PostCategory.objects.create(post=n1,category=c2)
pc6 = PostCategory.objects.create(post=n1,category=c3)

co1 = Comment.objects.create(user=u1,post=p1,text='sdfsgtgdv')
co2 = Comment.objects.create(user=u2,post=p2,text='fgfg hdfsdasdgfg')
co3 = Comment.objects.create(user=u1,post=n1,text='sdfsdfv vyjtyj gtgdv')
co4 = Comment.objects.create(user=u2,post=p1,text='sdfsa ascas xasd gtgdv')

c1.like()
p1.dislike()
p2.like()
p3.like()
c2.dislike()
c3.like()
c4.like()

a1.update_rating()
a2.update_rating()

a = Author.objects.order_by('-rating')[0]
print(f'Автор: {a.user.username}, рейтинг: {a.rating}')

p = Post.objects.filter(isnews=False).order_by('-rating')[0]

print(f'Дата: {p.created}, Автор: {p.author.user.username}, Рейтинг: {p.rating}, Заголовок: {p.title}, Превью: {p.preview()}')

for c in Comment.objects.filter(post_id=p.id):
  print(f'Дата: {c.created}, Автор: {c.user.username}, Рейтинг: {c.rating}, Текст: {c.text}\r\n')
