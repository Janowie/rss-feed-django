# rss-feed-django

Repo: https://github.com/Janowie/rss-feed-django  
Page: https://janowie.github.io/rss-feed-django/  

<ins>Technologies used</ins>:
- server: Django
- hosting: Github Pages
- CI-CD: Github Actions

## Jobs in Github workflows:

### build_test_render

Steps:
- <ins>Set up Python 3.7</ins>  
Sets up python with version specified.
- <ins>Install Dependencies  </ins>  
Upgrades pip and installs dependencies from the requirements.txt file inside of the WPUB file.
- <ins>Run Tests  </ins>  
This is a symbolic step which runs our only test, that always passes.
- <ins>Render Website  </ins>  
Creates a public dir and calls our custom manage.py function, that renders a static website with articles and
their metadata and returns it as a plain string, which is captured from the stdout and saved into the public folder
as index.html
- <ins>Upload rendered index</ins>  
We use GIT Artifacts to store the rendered website, which is used in the following job.

### load_deploy

Steps:
- <ins>Load rendered index</ins>   
This step downloads the index.html from artifact.
- <ins>Deploy to GitHub Pages</ins>   
We use the crazy-max/ghaction-github-pages@v2 to push the static file to our gh-pages branch, which is configured
as the root for Github pages.
