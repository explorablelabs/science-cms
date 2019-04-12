# Science Hugo template for Netlify CMS with Netlify Identity

This is a science-focused template built with [Victor Hugo](https://github.com/netlify/victor-hugo) and [Netlify CMS](https://github.com/netlify/netlify-cms), originalled designed and developed by [Darin Dimitroff](http://www.darindimitroff.com/), [spacefarm.digital](https://www.spacefarm.digital). Modified by [Explorable Labs](https://www.explorablelabs.com) to include the ability to draw small molecules (via smiles-drawer.js), and data charts (with Chart.js).

## [DEMO](https://science-cms-demo.netlify.com)
* Play with an [example Admin page](https://cms-demo.netlify.com/#/collections/posts) for Netlify CMS.
* This SCIENCE template Admin page is the same as the Netlify demo, but includes extra widget options beyond the basics like Text, Image, File, etc. They are: Molecule (for drawing 2D molecules based on SMILES) and ChartCSV (for charting CSV data that is uploaded via a file). 
* [Editing the page on the left](https://user-images.githubusercontent.com/45920345/56070185-51e61e80-5d3b-11e9-977f-525177004b43.png) to produce a preview on the right. 

## Getting started

Use our deploy button to get your own copy of the repository. 

[![Deploy to Netlify](https://www.netlify.com/img/deploy/button.svg)](https://app.netlify.com/start/deploy?repository=https://github.com/explorablelabs/science-cms/)

This will setup everything needed for running the CMS:

* A new repository in your GitHub account with the code
* Full Continuous Deployment to Netlify's global CDN network
* Control users and access with Netlify Identity (extra fee beyond N users)
* Manage content with Netlify CMS

Once the initial build finishes, you can invite yourself as a user. Go to the Identity tab in your new site, click "Invite" and send yourself an invite.

Now you're all set, and you can start editing content!

## Local Development

Clone this repository, and run `yarn` or `npm install` from the new folder to install all required dependencies.

Then start the development server with `yarn start` or `npm start`.

## Layouts

The template is based on small, content-agnostic partials that can be mixed and matched. The new partials are for molecule drawing and charts. The pre-built pages showcase just a few of the possible combinations. Refer to the `site/layouts/partials` folder for all available partials.

Use Hugo’s `dict` functionality to feed content into partials and avoid repeating yourself and creating discrepancies.

All of the coffee-related content on this site is from Netlify's original CMS demo, and remains here as humorous placeholder content.

## CSS

The template uses a custom fork of Tachyons and PostCSS with cssnext and cssnano. To customize the template for your brand, refer to `src/css/imports/_variables.css` where most of the important global variables like colors and spacing are stored.

## SVG

All SVG icons stored in `site/static/img/icons` are automatically optimized with SVGO (gulp-svgmin) and concatenated into a single SVG sprite stored as a a partial called `svg.html`. Make sure you use consistent icons in terms of viewport and art direction for optimal results. Refer to an SVG via the `<use>` tag like so:

```
<svg width="16px" height="16px" class="db">
  <use xlink:href="#SVG-ID"></use>
</svg>
```
