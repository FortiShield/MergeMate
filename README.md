<div align="center">

<div align="center">


<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://khulnasoft.com/images/mergemate/logo-dark.png" width="330">
  <source media="(prefers-color-scheme: light)" srcset="https://khulnasoft.com/images/mergemate/logo-light.png" width="330">
  <img src="https://khulnasoft.com/images/mergemate/logo-light.png" alt="logo" width="330">

</picture>
<br/>
CodiumAI MergeMate aims to help efficiently review and handle pull requests, by providing AI feedbacks and suggestions
</div>

[![GitHub license](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://github.com/Khulnasoft/mergemate/blob/main/LICENSE)
[![Discord](https://badgen.net/badge/icon/discord?icon=discord&label&color=purple)](https://discord.com/channels/1057273017547378788/1126104260430528613)
[![Twitter](https://img.shields.io/twitter/follow/khulnasoft)](https://twitter.com/khulnasoft)
    <a href="https://github.com/Khulnasoft/mergemate/commits/main">
    <img alt="GitHub" src="https://img.shields.io/github/last-commit/Khulnasoft/mergemate/main?style=for-the-badge" height="20">
    </a>
</div>

### [Documentation](https://mergemate-docs.khulnasoft.com/)
- See the [Installation Guide](https://mergemate-docs.khulnasoft.com/installation/) for instructions on installing MergeMate on different platforms.

- See the [Usage Guide](https://mergemate-docs.khulnasoft.com/usage-guide/) for instructions on running MergeMate tools via different interfaces, such as CLI, PR Comments, or by automatically triggering them when a new PR is opened.

- See the [Tools Guide](https://mergemate-docs.khulnasoft.com/tools/) for a detailed description of the different tools, and the available configurations for each tool.


## Table of Contents
- [News and Updates](#news-and-updates)
- [Overview](#overview)
- [Example results](#example-results)
- [Try it now](#try-it-now)
- [MergeMate Pro 💎](#mergemate-pro-)
- [How it works](#how-it-works)
- [Why use MergeMate?](#why-use-mergemate)
  
## News and Updates

### April 14, 2024
You can now ask questions about images that appear in the comment, where the entire PR is considered as the context.
see [here](https://mergemate-docs.khulnasoft.com/tools/ask/#ask-on-images) for more details.

<kbd><img src="https://khulnasoft.com/images/mergemate/ask_images5.png" width="512"></kbd>

### March 24, 2024
MergeMate is now available for easy installation via [pip](https://mergemate-docs.khulnasoft.com/installation/locally/#using-pip-package).

### March 17, 2024
- A new feature is now available for the review tool: [`require_can_be_split_review`](https://mergemate-docs.khulnasoft.com/tools/review/#enabledisable-features). 
If set to true, the tool will add a section that checks if the PR contains several themes, and can be split into smaller PRs.

<kbd><img src="https://khulnasoft.com/images/mergemate/multiple_pr_themes.png" width="512"></kbd>

### March 10, 2024
- A new [knowledge-base website](https://mergemate-docs.khulnasoft.com/) for MergeMate is now available. It includes detailed information about the different tools, usage guides and more, in an accessible and organized format.

### March 8, 2024

- A new tool, [Find Similar Code](https://mergemate-docs.khulnasoft.com/tools/similar_code/) 💎 is now available. 
<br>This tool retrieves the most similar code components from inside the organization's codebase, or from open-source code:

<kbd><a href="https://khulnasoft.com/images/mergemate/similar_code.mp4"><img src="https://khulnasoft.com/images/mergemate/similar_code_global2.png" width="512"></a></kbd>

(click on the image to see an instructional video)

### Feb 29, 2024
- You can now use the repo's [wiki page](https://mergemate-docs.khulnasoft.com/usage-guide/configuration_options/) to set configurations for MergeMate 💎

<kbd><img src="https://khulnasoft.com/images/mergemate/wiki_configuration.png" width="512"></kbd>


## Overview
<div style="text-align:left;">

Supported commands per platform:

|       |                                                                                                                   | GitHub             | Gitlab             | Bitbucket          | Azure DevOps       |
|-------|-------------------------------------------------------------------------------------------------------------------|:--------------------:|:--------------------:|:--------------------:|:--------------------:|
| TOOLS | Review                                                                                                            | ✅ | ✅ | ✅ | ✅ |
|       | ⮑ Incremental                                                                                                     | ✅ |                    |                    |                    |
|       | ⮑ [SOC2 Compliance](https://mergemate-docs.khulnasoft.com/tools/review/#soc2-ticket-compliance) 💎            | ✅ | ✅ | ✅ | ✅ |
|       | Describe                                                                                                          | ✅ | ✅ | ✅ | ✅ |
|       | ⮑ [Inline File Summary](https://mergemate-docs.khulnasoft.com/tools/describe#inline-file-summary) 💎          | ✅ |                    |                    |                    |
|       | Improve                                                                                                           | ✅ | ✅ | ✅ | ✅ |
|       | ⮑ Extended                                                                                                        | ✅ | ✅ | ✅ | ✅ |
|       | Ask                                                                                                               | ✅ | ✅ | ✅ | ✅ |
|       | ⮑ [Ask on code lines](https://mergemate-docs.khulnasoft.com/tools/ask#ask-lines)                              | ✅ | ✅ |                    |                    |
|       | [Custom Suggestions](https://mergemate-docs.khulnasoft.com/tools/custom_suggestions/) 💎                      | ✅ | ✅ | ✅ | ✅ |
|       | [Test](https://mergemate-docs.khulnasoft.com/tools/test/) 💎                                                  | ✅ | ✅ |                    | ✅ |
|       | Reflect and Review                                                                                                | ✅ | ✅ | ✅ | ✅ |
|       | Update CHANGELOG.md                                                                                               | ✅ | ✅ | ✅ | ✅ |
|       | Find Similar Issue                                                                                                | ✅ |                    |                    |                    |
|       | [Add PR Documentation](https://mergemate-docs.khulnasoft.com/tools/documentation/) 💎                         | ✅ | ✅ |                   | ✅ |
|       | [Custom Labels](https://mergemate-docs.khulnasoft.com/tools/custom_labels/) 💎                                | ✅ | ✅ |                    | ✅ |
|       | [Analyze](https://mergemate-docs.khulnasoft.com/tools/analyze/) 💎                                            | ✅ | ✅ |                    | ✅ |
|       | [CI Feedback](https://mergemate-docs.khulnasoft.com/tools/ci_feedback/) 💎                                    | ✅ |                    |                    |                    |
|       | [Similar Code](https://mergemate-docs.khulnasoft.com/tools/similar_code/) 💎                                  | ✅ |                    |                    |                    |
|       |                                                                                                                   |                    |                    |                    |                    |
| USAGE | CLI                                                                                                               | ✅ | ✅ | ✅ | ✅ |
|       | App / webhook                                                                                                     | ✅ | ✅ | ✅ | ✅ |
|       | Tagging bot                                                                                                       | ✅ |                    |                    |                    |
|       | Actions                                                                                                           | ✅ |                    | ✅ |                    |
|       |                                                                                                                   |                    |                    |                    |                    |
| CORE  | PR compression                                                                                                    | ✅ | ✅ | ✅ | ✅ |
|       | Repo language prioritization                                                                                      | ✅ | ✅ | ✅ | ✅ |
|       | Adaptive and token-aware file patch fitting                                                                       | ✅ | ✅ | ✅ | ✅ |
|       | Multiple models support                                                                                           | ✅ | ✅ | ✅ | ✅ |
|       | [Static code analysis](https://mergemate-docs.khulnasoft.com/core-abilities/#static-code-analysis) 💎         | ✅ | ✅ | ✅ | ✅ |
|       | [Global and wiki configurations](https://mergemate-docs.khulnasoft.com/usage-guide/configuration_options/) 💎 | ✅ | ✅ | ✅ | ✅ |
|       | [PR interactive actions](https://www.khulnasoft.com/images/mergemate/pr-actions.mp4) 💎                                 | ✅ |                    |                    |                    |
- 💎 means this feature is available only in [MergeMate Pro](https://www.khulnasoft.com/pricing/)

[//]: # (- Support for additional git providers is described in [here]&#40;./docs/Full_environments.md&#41;)
___

‣ **Auto Description ([`/describe`](https://mergemate-docs.khulnasoft.com/tools/describe/))**: Automatically generating PR description - title, type, summary, code walkthrough and labels.
\
‣ **Auto Review ([`/review`](https://mergemate-docs.khulnasoft.com/tools/review/))**: Adjustable feedback about the PR, possible issues, security concerns, review effort and more.
\
‣ **Code Suggestions ([`/improve`](https://mergemate-docs.khulnasoft.com/tools/improve/))**: Code suggestions for improving the PR.
\
‣ **Question Answering ([`/ask ...`](https://mergemate-docs.khulnasoft.com/tools/ask/))**: Answering free-text questions about the PR.
\
‣ **Update Changelog ([`/update_changelog`](https://mergemate-docs.khulnasoft.com/tools/update_changelog/))**: Automatically updating the CHANGELOG.md file with the PR changes.
\
‣ **Find Similar Issue ([`/similar_issue`](https://mergemate-docs.khulnasoft.com/tools/similar_issues/))**: Automatically retrieves and presents similar issues.
\
‣ **Add Documentation 💎  ([`/add_docs`](https://mergemate-docs.khulnasoft.com/tools/documentation/))**: Generates documentation to methods/functions/classes that changed in the PR.
\
‣ **Generate Custom Labels 💎 ([`/generate_labels`](https://mergemate-docs.khulnasoft.com/tools/custom_labels/))**: Generates custom labels for the PR, based on specific guidelines defined by the user.
\
‣ **Analyze 💎 ([`/analyze`](https://mergemate-docs.khulnasoft.com/tools/analyze/))**: Identify code components that changed in the PR, and enables to interactively generate tests, docs, and code suggestions for each component.
\
‣ **Custom Suggestions 💎 ([`/custom_suggestions`](https://mergemate-docs.khulnasoft.com/tools/custom_suggestions/))**: Automatically generates custom suggestions for improving the PR code, based on specific guidelines defined by the user.
\
‣ **Generate Tests 💎 ([`/test component_name`](https://mergemate-docs.khulnasoft.com/tools/test/))**: Generates unit tests for a selected component, based on the PR code changes.
\
‣ **CI Feedback 💎 ([`/checks ci_job`](https://mergemate-docs.khulnasoft.com/tools/ci_feedback/))**: Automatically generates feedback and analysis for a failed CI job.
\
‣ **Similar Code 💎 ([`/find_similar_component`](https://mergemate-docs.khulnasoft.com/tools/similar_code/))**: Retrieves the most similar code components from inside the organization's codebase, or from open-source code.
___

## Example results
</div>
<h4><a href="https://github.com/Khulnasoft/mergemate/pull/530">/describe</a></h4>
<div align="center">
<p float="center">
<img src="https://www.khulnasoft.com/images/mergemate/describe_new_short_main.png" width="512">
</p>
</div>
<hr>

<h4><a href="https://github.com/Khulnasoft/mergemate/pull/732#issuecomment-1975099151">/review</a></h4>
<div align="center">
<p float="center">
<kbd>
<img src="https://www.khulnasoft.com/images/mergemate/review_new_short_main.png" width="512">
</kbd>
</p>
</div>
<hr>

<h4><a href="https://github.com/Khulnasoft/mergemate/pull/732#issuecomment-1975099159">/improve</a></h4>
<div align="center">
<p float="center">
<kbd>
<img src="https://www.khulnasoft.com/images/mergemate/improve_new_short_main.png" width="512">
</kbd>
</p>
</div>
<hr>

<h4><a href="https://github.com/Khulnasoft/mergemate/pull/530">/generate_labels</a></h4>
<div align="center">
<p float="center">
<kbd><img src="https://www.khulnasoft.com/images/mergemate/geneare_custom_labels_main_short.png" width="300"></kbd>
</p>
</div>

[//]: # (<h4><a href="https://github.com/Khulnasoft/mergemate/pull/78#issuecomment-1639739496">/reflect_and_review:</a></h4>)

[//]: # (<div align="center">)

[//]: # (<p float="center">)

[//]: # (<img src="https://www.khulnasoft.com/images/reflect_and_review.gif" width="800">)

[//]: # (</p>)

[//]: # (</div>)

[//]: # (<h4><a href="https://github.com/Khulnasoft/mergemate/pull/229#issuecomment-1695020538">/ask:</a></h4>)

[//]: # (<div align="center">)

[//]: # (<p float="center">)

[//]: # (<img src="https://www.khulnasoft.com/images/ask-2.gif" width="800">)

[//]: # (</p>)

[//]: # (</div>)

[//]: # (<h4><a href="https://github.com/Khulnasoft/mergemate/pull/229#issuecomment-1695024952">/improve:</a></h4>)

[//]: # (<div align="center">)

[//]: # (<p float="center">)

[//]: # (<img src="https://www.khulnasoft.com/images/improve-2.gif" width="800">)

[//]: # (</p>)

[//]: # (</div>)
<div align="left">


</div>
<hr>


## Try it now

Try the GPT-4 powered MergeMate instantly on _your public GitHub repository_. Just mention `@CodiumAI-Agent` and add the desired command in any PR comment. The agent will generate a response based on your command.
For example, add a comment to any pull request with the following text:
```
@CodiumAI-Agent /review
```
and the agent will respond with a review of your PR

![Review generation process](https://www.khulnasoft.com/images/demo-2.gif)


To set up your own MergeMate, see the [Installation](https://mergemate-docs.khulnasoft.com/installation/) section below.
Note that when you set your own MergeMate or use CodiumAI hosted MergeMate, there is no need to mention `@CodiumAI-Agent ...`. Instead, directly start with the command, e.g., `/ask ...`.

---

[//]: # (## Installation)

[//]: # (To use your own version of MergeMate, you first need to acquire two tokens:)

[//]: # ()
[//]: # (1. An OpenAI key from [here]&#40;https://platform.openai.com/&#41;, with access to GPT-4.)

[//]: # (2. A GitHub personal access token &#40;classic&#41; with the repo scope.)

[//]: # ()
[//]: # (There are several ways to use MergeMate:)

[//]: # ()
[//]: # (**Locally**)

[//]: # (- [Using pip package]&#40;https://mergemate-docs.khulnasoft.com/installation/locally/#using-pip-package&#41;)

[//]: # (- [Using Docker image]&#40;https://mergemate-docs.khulnasoft.com/installation/locally/#using-docker-image&#41;)

[//]: # (- [Run from source]&#40;https://mergemate-docs.khulnasoft.com/installation/locally/#run-from-source&#41;)

[//]: # ()
[//]: # (**GitHub specific methods**)

[//]: # (- [Run as a GitHub Action]&#40;https://mergemate-docs.khulnasoft.com/installation/github/#run-as-a-github-action&#41;)

[//]: # (- [Run as a GitHub App]&#40;https://mergemate-docs.khulnasoft.com/installation/github/#run-as-a-github-app&#41;)

[//]: # ()
[//]: # (**GitLab specific methods**)

[//]: # (- [Run a GitLab webhook server]&#40;https://mergemate-docs.khulnasoft.com/installation/gitlab/&#41;)

[//]: # ()
[//]: # (**BitBucket specific methods**)

[//]: # (- [Run as a Bitbucket Pipeline]&#40;https://mergemate-docs.khulnasoft.com/installation/bitbucket/&#41;)

## MergeMate Pro 💎
[MergeMate Pro](https://www.khulnasoft.com/pricing/) is a hosted version of MergeMate, provided by CodiumAI. It is available for a monthly fee, and provides the following benefits:
1. **Fully managed** - We take care of everything for you - hosting, models, regular updates, and more. Installation is as simple as signing up and adding the MergeMate app to your GitHub\GitLab\BitBucket repo.
2. **Improved privacy** - No data will be stored or used to train models. MergeMate Pro will employ zero data retention, and will use an OpenAI account with zero data retention.
3. **Improved support** - MergeMate Pro users will receive priority support, and will be able to request new features and capabilities.
4. **Extra features** -In addition to the benefits listed above, MergeMate Pro will emphasize more customization, and the usage of static code analysis, in addition to LLM logic, to improve results. 
See [here](https://mergemate-docs.khulnasoft.com/#mergemate-pro) for a list of features available in MergeMate Pro.



## How it works

The following diagram illustrates MergeMate tools and their flow:

![MergeMate Tools](https://khulnasoft.com/images/mergemate/diagram-v0.9.png)

Check out the [PR Compression strategy](https://mergemate-docs.khulnasoft.com/core-abilities/#pr-compression-strategy) page for more details on how we convert a code diff to a manageable LLM prompt

## Why use MergeMate?

A reasonable question that can be asked is: `"Why use MergeMate? What makes it stand out from existing tools?"`

Here are some advantages of MergeMate:

- We emphasize **real-life practical usage**. Each tool (review, improve, ask, ...) has a single GPT-4 call, no more. We feel that this is critical for realistic team usage - obtaining an answer quickly (~30 seconds) and affordably.
- Our [PR Compression strategy](https://mergemate-docs.khulnasoft.com/core-abilities/#pr-compression-strategy)  is a core ability that enables to effectively tackle both short and long PRs.
- Our JSON prompting strategy enables to have **modular, customizable tools**. For example, the '/review' tool categories can be controlled via the [configuration](mergemate/settings/configuration.toml) file. Adding additional categories is easy and accessible.
- We support **multiple git providers** (GitHub, Gitlab, Bitbucket), **multiple ways** to use the tool (CLI, GitHub Action, GitHub App, Docker, ...), and **multiple models** (GPT-4, GPT-3.5, Anthropic, Cohere, Llama2).


## Data privacy

If you host MergeMate with your OpenAI API key, it is between you and OpenAI. You can read their API data privacy policy here:
https://openai.com/enterprise-privacy

When using MergeMate Pro 💎, hosted by CodiumAI, we will not store any of your data, nor will we use it for training.
You will also benefit from an OpenAI account with zero data retention.

## Links

[![Join our Discord community](https://raw.githubusercontent.com/Khulnasoft/khulnasoft-vscode-release/main/media/docs/Joincommunity.png)](https://discord.gg/kG35uSHDBc)

- Discord community: https://discord.gg/kG35uSHDBc
- CodiumAI site: https://khulnasoft.com
- Blog: https://www.khulnasoft.com/blog/
- Troubleshooting: https://www.khulnasoft.com/blog/technical-faq-and-troubleshooting/
- Support: support@khulnasoft.com
