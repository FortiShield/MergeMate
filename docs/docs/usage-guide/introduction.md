
After [installation](https://khulnasoft.github.io/Docs-MergeMate/installation/), there are three basic ways to invoke KhulnaSoft MergeMate:

1. Locally running a CLI command
2. Online usage - by [commenting](https://github.com/Khulnasoft/mergemate/pull/229#issuecomment-1695021901) on a PR
3. Enabling MergeMate tools to run automatically when a new PR is opened


Specifically, CLI commands can be issued by invoking a pre-built [docker image](https://khulnasoft.github.io/Docs-MergeMate/installation/#run-from-source), or by invoking a [locally cloned repo](https://khulnasoft.github.io/Docs-MergeMate/installation/#locally).
For online usage, you will need to setup either a [GitHub App](https://khulnasoft.github.io/Docs-MergeMate/installation/#run-as-a-github-app), or a [GitHub Action](https://khulnasoft.github.io/Docs-MergeMate/installation/#run-as-a-github-action).
GitHub App and GitHub Action also enable to run MergeMate specific tool automatically when a new PR is opened.


**git provider**: The [git_provider](https://github.com/Khulnasoft/mergemate/blob/main/mergemate/settings/configuration.toml#L4) field in the configuration file determines the GIT provider that will be used by MergeMate. Currently, the following providers are supported:
`
"github", "gitlab", "bitbucket", "azure", "codecommit", "local", "gerrit"
`

