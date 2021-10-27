from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
# from django.shortcuts import redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from .forms import CommentForm

# Create your views here.
def recipe_page(request):
    return render(request, 'recipe_page.html')

def recipe_detail_bruschetta(request):
    return render(request, 'recipe_detail_bruschetta.html')


def recipe_detail_shrimp(request):
    return render(request, 'recipe_detail_shrimp.html')

def recipe_detail_salad(request):
    return render(request, 'recipe_detail_salad_caprese.html')  

def recipe_detail_greek_chicken(request):
    return render(request, 'recipe_detail_greek_chicken.html')  

def recipe_detail_salmon(request):
    return render (request, 'recipe_detail_salmon.html')

# def post_detail(request, slug):
#     template_name = 'post_detail.html'
#     post = get_object_or_404(Post, slug=slug)
#     comments = post.comments.filter(active=True)
#     new_comment = None
#     # Comment posted
#     if request.method == 'POST':
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():

#             # Create Comment object but don't save to database yet
#             new_comment = comment_form.save(commit=False)
#             # Assign the current post to the comment
#             new_comment.post = post
#             # Save the comment to the database
#             new_comment.save()
#     else:
#         comment_form = CommentForm()

#     return render(request, template_name, {'post': post,
#                                            'comments': comments,
#                                            'new_comment': new_comment,
#                                            'comment_form': comment_form})