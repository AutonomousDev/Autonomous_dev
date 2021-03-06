from django.shortcuts import render, get_object_or_404
from .models import Post, Project
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User


class PostListView(ListView):
    """This view list all post with pagination for now it's also the home page"""
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    """This view will show all post made by a user."""
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    """This view shows a single post. if the user is the author the template has
    update and delete buttons"""
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    """This view is used for creating new posts."""
    model = Post
    fields = ['title', 'content', 'project']

    def form_valid(self, form):
        """Set author before validating the form"""
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """This view is used for updating posts"""
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        """Set author before validating the form"""
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """Logic for checking the current user is the same as the author before they can
        make updates"""
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Deletes the posts and redirects to home."""
    model = Post
    success_url = '/'

    def test_func(self):
        """Logic for checking the current user is the same as the author before they can
        make deletes"""
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


# Project display system
class ProjectListView(ListView):
    """This view is used to display my main portfolio as a grid"""
    model = Project
    template_name = 'blog/project_list.html'
    context_object_name = 'projects'
    ordering = ['-rank']

    # Pagination doesn't make sense for this view I think.
    # paginate_by = 5


class ProjectDetailView(DetailView):
    """This view shows a single project. If post have a matching category they show up as well"""
    model = Project

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['posts'] = Post.objects.filter(project=self.object).order_by('-date_posted')
        return context


class ProjectCreateView(LoginRequiredMixin, CreateView):
    """This view is used for creating new projects."""
    model = Project
    fields = ['title',
              'card_content',
              'content',
              'rank',
              'image',
              'demo_link',
              'github_link',
              ]

    def form_valid(self, form):
        """Set author before validating the form"""
        form.instance.author = self.request.user
        return super().form_valid(form)


class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """This view is used for updating posts"""
    model = Project
    fields = ['title',
              'card_content',
              'content',
              'rank',
              'image',
              'demo_link',
              'github_link',
              ]

    def form_valid(self, form):
        """Set author before validating the form"""
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """Logic for checking the current user is the same as the author before they can
        make updates"""
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Deletes the posts and redirects to home."""
    model = Project
    success_url = '/'

    def test_func(self):
        """Logic for checking the current user is the same as the author before they can
        make deletes"""
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False
