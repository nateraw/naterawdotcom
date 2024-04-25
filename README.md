# nateraw.com

My personal website/blog, made with [Quarto](https://quarto.org).


## Development

Install Quarto by following the instructions [here](https://quarto.org/docs/get-started/).

Then, make sure you have Python installed and run:

```bash
pip install -r requirements.txt
```

To start the development server, run the following from the root of the repo:

```bash
quarto preview .
```

## Deployment

Deployment happens through GitHub Actions. If you are setting this up for the first time, you have to:

- add a blank `gh-pages` branch
- Set up the repo to use GitHub Pages from the `gh-pages` branch
- Make sure the `CNAME` file is in the root of the repo with your domain name
- Set "read and write" permissions for the `GITHUB_TOKEN` in the repo's secrets, which you can find in the actions tab under the settings of the repo
- run `quarto publish gh-pages` locally once to set up the initial deployment
- then the action should work (if I haven't missed anything)

## Additional Notes

- The `filter.py` script will add colab badges to the top of each notebook if you add `insert_colab_badge: true` in the metadata header of the notebook.