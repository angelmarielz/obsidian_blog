---
title: My Insane Blog Pipeline
date: 2025-09-03
draft: false
tags:
  - testing
  - blog
---

## How to start

[Link to start](https://github.com/panr/hugo-theme-terminal#how-to-start)

You can download the theme manually by going to [https://github.com/panr/hugo-theme-terminal.git](https://github.com/panr/hugo-theme-terminal.git) and pasting it to `themes/terminal` in your root directory.

You can also choose **one of the 3 possibilities** to install the theme:

1. as Hugo Module
2. as a standalone local directory
3. as a git submodule

⚠️ The theme needs at least Hugo **Extended** v0.90.x.

### Install theme as Hugo Module

```shell
# If this is the first time you're using Hugo Modules
# in your project. You have to initiate your own module before
# you fetch the theme module.
#
# hugo mod init [your website/module name]
hugo mod get github.com/panr/hugo-theme-terminal/v4
```

and in your config file add:

```toml
[module]
  # this is needed when you fetch the theme as a submodule to your repo.
  # replacements = "github.com/panr/hugo-theme-terminal/4 -> themes/terminal"
[[module.imports]]
  path = 'github.com/panr/hugo-theme-terminal/v4'
```

Keep in mind that the theme by default won't show up in the `themes` directory. This means that you are using the theme as it was on the repository at the moment you fetched it. Your local `go.sum` file keeps all the references. Read more about Hugo Modules in the [official documentation](https://gohugo.io/hugo-modules/).

### Install theme locally

```shell
git clone https://github.com/panr/hugo-theme-terminal.git themes/terminal
```

This will clone the repository directly to the `themes/terminal` directory.

### Install theme as a submodule

```shell
git submodule add -f https://github.com/panr/hugo-theme-terminal.git themes/terminal
```

This will install the repository as a submodule in the `themes/terminal` directory.

⚠️ If you encounter any issues with:

```shell
Error: module "terminal" not found; either add it as a Hugo Module or store it in "[...your custom path]/themes".: module does not exist
```

then please try to remove `theme = "terminal"` from your config file.