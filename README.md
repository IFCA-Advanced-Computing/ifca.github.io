# grid.ifca.es pelican site

Pelican documentation: http://getpelican.com

## How to publish the site

1. Install pelican `aptitude install python-pelican`
2. Edit whatever you want in the `content/` directory.
   * `pages/` contain static pages that will be linked in the top menu.
   * You can create a post in a category by creating it inside a directory,
     so `content/news/hello-world.md` will make hello-world belong to the news
     category.
3. Once you're done, create the output: `make publish`
4. Add the output directory `git add output`
5. Commit your changes `git commit -a`
6. Publish to `grid.ifca.es`: `make ssh_upload`
7. Publish to github: `make github`
