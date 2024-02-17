# Analyze Tool 💎
The `analyze` tool combines static code analysis with LLM capabilities to provide a comprehensive analysis of the PR code changes.

The tool scans the PR code changes, find the code components (methods, functions, classes) that changed, and summarizes the changes in each component.

It can be invoked manually by commenting on any PR:
```
/analyze
```

An example [result](https://github.com/khulnasoft/mergemate/pull/546#issuecomment-1868524805):

<kbd><img src=https://khulnasoft.com/images/mergemate/analyze_1.png width="768"></kbd>
___
<kbd><img src=https://khulnasoft.com/images/mergemate/analyze_2.png width="768"></kbd>
___
<kbd><img src=https://khulnasoft.com/images/mergemate/analyze_3.png width="768"></kbd>


Notes 
- Language that are currently supported: Python, Java, C++, JavaScript, TypeScript.