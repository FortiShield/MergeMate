# Overview

CodiumAI MergeMate is an open-source tool to help efficiently review and handle pull requests.

- See the [Installation Guide](./installation/index.md) for instructions on installing and running the tool on different git platforms.

- See the [Usage Guide](./usage-guide/index.md) for instructions on running the MergeMate commands via different interfaces, including _CLI_, _online usage_, or by _automatically triggering_ them when a new PR is opened.

- See the [Tools Guide](./tools/index.md) for a detailed description of the different tools.


## MergeMate Features
MergeMate offers extensive pull request functionalities across various git providers.

|       |                                                                                                                     | GitHub | Gitlab | Bitbucket | Azure DevOps |
|-------|---------------------------------------------------------------------------------------------------------------------|:------:|:------:|:---------:|:------------:|
| TOOLS | Review                                                                                                              |   ✅    |   ✅    |   ✅       |      ✅      |
|       | ⮑ Incremental                                                                                                       |   ✅    |        |            |              |
|       | ⮑ [SOC2 Compliance](https://khulnasoft.github.io/mergemate/tools/review/#soc2-ticket-compliance){:target="_blank"} 💎                                     |   ✅    |   ✅    |   ✅        |      ✅      |
|       | Ask                                                                                                                 |   ✅    |   ✅    |   ✅        |      ✅      |
|       | Describe                                                                                                            |   ✅    |   ✅    |   ✅        |      ✅      |
|       | ⮑ [Inline file summary](https://khulnasoft.github.io/mergemate/tools/describe/#inline-file-summary){:target="_blank"} 💎                                 |   ✅    |   ✅    |           |      ✅      |
|       | Improve                                                                                                             |   ✅    |   ✅    |   ✅        |      ✅      |
|       | ⮑ Extended                                                                                                          |   ✅    |   ✅    |   ✅        |      ✅      |
|       | [Custom Suggestions](./tools/custom_suggestions.md){:target="_blank"} 💎                                               |   ✅    |   ✅    |   ✅        |      ✅      |
|       | Reflect and Review                                                                                                  |   ✅    |   ✅    |   ✅        |      ✅      |
|       | Update CHANGELOG.md                                                                                                 |   ✅    |   ✅    |   ✅        |      ️       |
|       | Find Similar Issue                                                                                                  |   ✅    |        |             |      ️       |
|       | [Add PR Documentation](./tools/documentation.md){:target="_blank"} 💎                                                  |   ✅    |   ✅    |          |      ✅      |
|       | [Generate Custom Labels](./tools/describe.md#handle-custom-labels-from-the-repos-labels-page-💎){:target="_blank"} 💎 |   ✅    |   ✅    |            |      ✅      |
|       | [Analyze PR Components](./tools/analyze.md){:target="_blank"} 💎                                                       |   ✅    |   ✅    |       |      ✅      |
|       |                                                                                                                     |        |        |            |      ️       |
| USAGE | CLI                                                                                                                 |   ✅    |   ✅    |   ✅       |      ✅      |
|       | App / webhook                                                                                                       |   ✅    |   ✅    |    ✅        |      ✅      |
|       | Actions                                                                                                             |   ✅    |        |            |      ️       |
|       |                                                                                                                     |        |        |            |
| CORE  | PR compression                                                                                                      |   ✅    |   ✅    |   ✅       |   ✅        |
|       | Repo language prioritization                                                                                        |   ✅    |   ✅    |   ✅       |   ✅        |
|       | Adaptive and token-aware file patch fitting                                                                         |   ✅    |   ✅    |   ✅     |   ✅        |
|       | Multiple models support                                                                                             |   ✅    |   ✅    |   ✅       |   ✅        |
|       | Incremental PR review                                                                                               |   ✅    |        |            |           |
|       | [Static code analysis](./tools/analyze.md/){:target="_blank"} 💎                                                        |   ✅    |   ✅     |    ✅    |   ✅        |
|       | [Multiple configuration options](./usage-guide/configuration_options.md){:target="_blank"} 💎                           |   ✅    |   ✅     |    ✅    |   ✅        |

💎 marks a feature available only in [MergeMate Pro](https://www.khulnasoft.com/pricing/){:target="_blank"}


## Example Results
<hr>

#### [/describe](https://github.com/Khulnasoft/mergemate/pull/530)
<figure markdown="1">
![/describe](https://www.khulnasoft.com/images/mergemate/describe_new_short_main.png){width=512}
</figure>
<hr>

#### [/review](https://github.com/Khulnasoft/mergemate/pull/732#issuecomment-1975099151)
<figure markdown="1">
![/review](https://www.khulnasoft.com/images/mergemate/review_new_short_main.png){width=512}
</figure>
<hr>

#### [/improve](https://github.com/Khulnasoft/mergemate/pull/732#issuecomment-1975099159)
<figure markdown="1">
![/improve](https://www.khulnasoft.com/images/mergemate/improve_new_short_main.png){width=512}
</figure>
<hr>

#### [/generate_labels](https://github.com/Khulnasoft/mergemate/pull/530)
<figure markdown="1">
![/generate_labels](https://www.khulnasoft.com/images/mergemate/geneare_custom_labels_main_short.png){width=300}
</figure>
<hr>

## How it Works

The following diagram illustrates MergeMate tools and their flow:

![MergeMate Tools](https://khulnasoft.com/images/mergemate/diagram-v0.9.png)

Check out the [PR Compression strategy](core-abilities/index.md) page for more details on how we convert a code diff to a manageable LLM prompt



## MergeMate Pro 💎

[MergeMate Pro](https://www.khulnasoft.com/pricing/) is a hosted version of MergeMate, provided by CodiumAI. It is available for a monthly fee, and provides the following benefits:

1. **Fully managed** - We take care of everything for you - hosting, models, regular updates, and more. Installation is as simple as signing up and adding the MergeMate app to your GitHub\GitLab\BitBucket repo.
2. **Improved privacy** - No data will be stored or used to train models. MergeMate Pro will employ zero data retention, and will use an OpenAI account with zero data retention.
3. **Improved support** - MergeMate Pro users will receive priority support, and will be able to request new features and capabilities.
4. **Extra features** -In addition to the benefits listed above, MergeMate Pro will emphasize more customization, and the usage of static code analysis, in addition to LLM logic, to improve results. It has the following additional tools and features:
    - (Tool): [**Analyze PR components**](./tools/analyze.md/)
    - (Tool): [**Custom Code Suggestions**](./tools/custom_suggestions.md/)
    - (Tool): [**Tests**](./tools/test.md/)
    - (Tool): [**PR documentation**](./tools/documentation.md/)
    - (Tool): [**Improve Component**](https://khulnasoft.github.io/mergemate/tools/improve_component/)
    - (Tool): [**Similar code search**](https://khulnasoft.github.io/mergemate/tools/similar_code/)
    - (Tool): [**CI feedback**](./tools/ci_feedback.md/)
    - (Feature): [**Interactive triggering**](./usage-guide/automations_and_usage.md/#interactive-triggering)
    - (Feature): [**SOC2 compliance check**](./tools/review.md/#soc2-ticket-compliance)
    - (Feature): [**Custom labels**](./tools/describe.md/#handle-custom-labels-from-the-repos-labels-page)
    - (Feature): [**Global and wiki configuration**](./usage-guide/configuration_options.md/#wiki-configuration-file)
    - (Feature): [**Inline file summary**](https://khulnasoft.github.io/mergemate/tools/describe/#inline-file-summary)

   
## Data Privacy

If you host MergeMate with your OpenAI API key, it is between you and OpenAI. You can read their API data privacy policy here:
https://openai.com/enterprise-privacy

When using MergeMate Pro 💎, hosted by CodiumAI, we will not store any of your data, nor will we use it for training.
You will also benefit from an OpenAI account with zero data retention.
