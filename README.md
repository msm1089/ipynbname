# ipynbname

When run in a Jupyter notebook, simply returns the notebook filename or the full path to the notebook.
I created this to help with automating posting blog posts written in Jupyter notebooks directly to
GitHub Pages.  
[Check it out](https://msm1089.github.io/2020/09/04/Automating-Jupyter-Notebook-Blog-Post-Deployment.html) if you're looking to use this method of blogging :metal:

You would think there was already some built-in way to access the current notebook name, but it took many hours
of searching for a way to do it. As it seems many others did, I tried using Javascript, but the async nature of
JS meant that it was unreliable. Finally I stumbled on this [post](https://forums.fast.ai/t/jupyter-notebook-enhancements-tips-and-tricks/17064/39).
I have refactored the code there so a user can get either the name or path, but credit for most of the code
goes to the author of this post, thanks!

## Examples

Get the notebook name:

```python
import ipynbname
nb_fname = ipynbname.name()
```

Get the full path to the notebook:

```python
import ipynbname
nb_path = ipynbname.path()
```
