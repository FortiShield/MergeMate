The different tools and sub-tools used by KhulnaSoft MergeMate are adjustable via the **[configuration file](https://github.com/Khulnasoft/mergemate/blob/main/mergemate/settings/configuration.toml)**.

In addition to general configuration options, each tool has its own configurations. For example, the `review` tool will use parameters from the [pr_reviewer](https://github.com/Khulnasoft/mergemate/blob/main/mergemate/settings/configuration.toml#L16) section in the configuration file.
See the [Tools Guide](https://khulnasoft.github.io/Docs-MergeMate/tools/) for a detailed description of the different tools and their configurations.

There are three ways to set persistent configurations:

1. Wiki configuration page 💎
2. Local configuration file
3. Global configuration file 💎

In terms of precedence, wiki configurations will override local configurations, and local configurations will override global configurations.

## Wiki configuration file 💎

Specifically for GitHub, with MergeMate-Pro you can set configurations by creating a page called `.mergemate.toml` in the [wiki](https://github.com/Khulnasoft/mergemate/wiki/mergemate.toml) of the repo. 
The advantage of this method is that it allows to set configurations without needing to commit new content to the repo - just edit the wiki page and **save**.

![wiki_configuration](https://khulnasoft.com/images/mergemate/wiki_configuration.png){width=512}

Click [here](https://khulnasoft.com/images/mergemate/wiki_configuration_mergemate.mp4) to see a short instructional video. We recommend surrounding the configuration content with triple-quotes, to allow better presentation when displayed in the wiki as markdown.
An example content:

```
[pr_description]
generate_ai_title=true
```

MergeMate will know to remove the triple-quotes when reading the configuration content.

## Local configuration file

By uploading a local `.mergemate.toml` file to the root of the repo's main branch, you can edit and customize any configuration parameter. Note that you need to upload `.mergemate.toml` prior to creating a PR, in order for the configuration to take effect.

For example, if you set in `.mergemate.toml`:

```
[pr_reviewer]
extra_instructions="""\
- instruction a
- instruction b
...
"""
```

Then you can give a list of extra instructions to the `review` tool.


## Global configuration file 💎

If you create a repo called `mergemate-settings` in your **organization**, it's configuration file `.mergemate.toml` will be used as a global configuration file for any other repo that belongs to the same organization.
Parameters from a local `.mergemate.toml` file, in a specific repo, will override the global configuration parameters.

For example, in the GitHub organization `Khulnasoft`:
- The repo [`https://github.com/Khulnasoft/mergemate-settings`](https://github.com/Khulnasoft/mergemate-settings/blob/main/.mergemate.toml) contains a `.mergemate.toml` file that serves as a global configuration file for all the repos in the GitHub organization `Khulnasoft`.
- The repo [`https://github.com/Khulnasoft/mergemate`](https://github.com/Khulnasoft/mergemate/blob/main/.mergemate.toml) inherits the global configuration file from `mergemate-settings`.