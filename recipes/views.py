from django.http import FileResponse, Http404
from io import BytesIO
import os
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from pywebhdfs.webhdfs import PyWebHdfsClient

from . import models
from .forms import RecipeForm

HDFS_BASE_PATH = "/user/hadoop/recipes"

# Create your views here.
def home(request):
    recipes = models.Recipe.objects.all()
    context = {"recipes": recipes}
    return render(request, "recipes/home.html", context)


class RecipeListView(ListView):
    model = models.Recipe
    template_name = "recipes/home.html"
    context_object_name = "recipes"


class RecipeDetailView(DetailView):
    model = models.Recipe

def hdfs_download_image(request, pk):
    try:
        recipe = models.Recipe.objects.get(pk=pk)
        if not recipe.image:
            raise Http404("No image associated with this recipe.")
        hdfs_path = f"{HDFS_BASE_PATH}/{recipe.id}/{recipe.image.name}"
        hdfs = PyWebHdfsClient(host="namenode", port="9870", user_name="hadoop")
        data = hdfs.read_file(hdfs_path)
        return FileResponse(BytesIO(data), content_type="image/jpeg")
    except models.Recipe.DoesNotExist:
        raise Http404("Recipe not found.")
    except Exception:
        raise Http404("Image not found in DFS")

def hdfs_download_video(request, pk):
    try:
        recipe = models.Recipe.objects.get(pk=pk)
        if not recipe.video:
            raise Http404("No video associated with this recipe.")
        hdfs_path = f"{HDFS_BASE_PATH}/{recipe.id}/{recipe.video.name}"
        hdfs = PyWebHdfsClient(host="namenode", port="9870", user_name="hadoop")
        data = hdfs.read_file(hdfs_path)
        return FileResponse(BytesIO(data), content_type="video/mp4")
    except models.Recipe.DoesNotExist:
        raise Http404("Recipe not found.")
    except Exception:
        raise Http404("Video not found in DFS")

def upload_to_hdfs(local_file_path, hdfs_path):
    hdfs = PyWebHdfsClient(host="namenode", port="9870", user_name="hadoop")
    parent_dir = "/".join(hdfs_path.split("/")[:-1])
    try:
        if not hdfs.exists_file_dir(parent_dir):
            hdfs.make_dir(parent_dir)
        with open(local_file_path, "rb") as f:
            file_data = f.read()
            hdfs.create_file(hdfs_path, file_data, overwrite=True)
        print(f"Uploaded {local_file_path} to HDFS at {hdfs_path}")
    except Exception as e:
        print(f"HDFS upload failed for {hdfs_path}: {e}")
    return hdfs_path


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = models.Recipe
    form_class = RecipeForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)

        if self.request.FILES.get("image"):
            img_local_path = form.instance.image.path
            hdfs_path_img = f"{HDFS_BASE_PATH}/{form.instance.id}/{form.instance.image.name}"
            upload_to_hdfs(img_local_path, hdfs_path_img)
            if os.path.exists(img_local_path):
                os.remove(img_local_path)

        if self.request.FILES.get("video"):
            vid_local_path = form.instance.video.path
            hdfs_path_vid = f"{HDFS_BASE_PATH}/{form.instance.id}/{form.instance.video.name}"
            upload_to_hdfs(vid_local_path, hdfs_path_vid)
            if os.path.exists(vid_local_path):
                os.remove(vid_local_path)

        return response

class RecipeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Recipe
    fields = ["title", "description", "image", "video"]

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author

    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)
        
        if self.request.FILES.get("image"):
            img_local_path = form.instance.image.path
            hdfs_path_img = f"{HDFS_BASE_PATH}/{form.instance.id}/{form.instance.image.name}"
            upload_to_hdfs(img_local_path, hdfs_path_img)
            if os.path.exists(img_local_path):
                os.remove(img_local_path)

        if self.request.FILES.get("video"):
            vid_local_path = form.instance.video.path
            hdfs_path_vid = f"{HDFS_BASE_PATH}/{form.instance.id}/{form.instance.video.name}"
            upload_to_hdfs(vid_local_path, hdfs_path_vid)
            if os.path.exists(vid_local_path):
                os.remove(vid_local_path)

        return response


class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Recipe
    success_url = reverse_lazy("recipes-home")

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author

def about(request):
    return render(request, "recipes/about.html")
