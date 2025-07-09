[Link to Google Doc](https://docs.google.com/document/d/1ZQbwwv5RqtLOhg414PCBLfFtUH7VeVKKoo-jww6-sJs/edit?usp=sharing)

## **Getting Started with GitHub Actions**

GitHub Actions is a powerful automation tool integrated into the GitHub platform that allows you to automate your software development workflows. Think of it as a way to make things happen automatically in your repository based on certain events, like pushing code, creating a pull request, or on a set schedule. These automated workflows are often used for Continuous Integration and Continuous Deployment (CI/CD), which means they can automatically build, test, and deploy your code.

At its core, a GitHub Action workflow is defined in a YAML file that you place in a special directory within your repository: `.github/workflows/`. Inside this file, you specify what events should trigger the workflow and what jobs should be run.


### **A Good First Action?: "Hello, World!"**

For someone new to GitHub Actions, a great place to start is with a simple "Hello, World!" workflow. This will help you understand the basic structure of a workflow file and see it in action without needing to set up any complex configurations.

This basic action will simply print "Hello, world!" in the workflow's log file. It's a fantastic way to verify that you've set up the workflow correctly and to see the results of an action.

Here's the code for a simple "Hello, World!" GitHub Action. You would save this as a `.yml` file (for example, `hello.yml`) inside the `.github/workflows/` directory of your repository.

```YML
name: Hello World

on: [push]

jobs:
  hello_world_job:
    runs-on: ubuntu-latest
    steps:
      - name: Say hello
        run: echo "Hello, world!"
```

### **Breaking Down the "Hello, World!" Action**

Let's quickly look at what each part of this workflow does:

* **<code>name: Hello World</code>**: This is simply the name of your workflow, which will be displayed on the "Actions" tab of your repository.
* **<code>on: [push]</code>**: This is the **trigger**. In this case, the workflow will run every time you `push` new code to any branch in your repository.
* **<code>jobs:</code>** This section defines all the jobs that will run as part of this workflow.
* **<code>hello_world_job:</code>**: This is the name of our single job.
* **<code>runs-on: ubuntu-latest</code>**: This specifies that the job should run on the latest version of an Ubuntu Linux virtual machine provided by GitHub.
* **<code>Steps: </code>**This is where you define the individual tasks that make up the job.
* **<code>- name: Say hello</code>**: This is a descriptive name for the step.
* **<code>run: echo "Hello, world!":</code>** This is the command that will be executed in the virtual machine's shell. In this case, it's the simple `echo` command to print "Hello, world!".

Once you commit this file to your repository and push a change, you can go to the "Actions" tab of your repository to see your workflow run. You'll be able to click on the workflow run and see the "Hello, world!" output in the log. This simple first step opens the door to more complex and powerful automations.

### Similarity to Docker?

If you have done the Docker activities you've noticed a great similarity! They both use YAML to define a set of instructions, which makes them look alike at a glance.

However, their core **purpose** is quite different.

### **How They Differ**

* **Docker Compose (<code>docker-compose.yml</code>)**: Its main job is **container orchestration** on a single machine. You use it to define and manage a multi-container application, specifying the services, networks, and volumes needed to run your app's environment locally. Think of it as a blueprint for your application's architecture. \

* **GitHub Actions (<code>.github/workflows/workflow.yml</code>)**: Its main job is **workflow automation** CI/CD (Continuous integration/ Continuous Development). It's event-driven, reacting to things like code pushes or pull requests. It runs a sequence of steps to build, test, lint, or deploy your code. Think of it as an automated assembly line for your software.

In short, Docker Compose defines *what* your application environment is, while GitHub Actions defines *what to do* when something happens in your repository. A GitHub Actions workflow might even include a step that uses Docker Compose to spin up your application for testing!

# **Examples By language**

## **Example For Python** 

For a Python data project, you should run actions that ensure your code is clean, correct, and your analyses are reproducible.


### **Linting with <code>ruff</code></strong>

Linting checks your code for stylistic and programmatic errors. Using a linter helps maintain code quality and consistency, which is crucial when collaborating. **<code>ruff</code>** is a very fast and popular linter for Python. This action will run on every push and pull request.

```YML
name: Lint
on: [push, pull_request]
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: pip install ruff
      - name: Run ruff
        run: ruff check .
```

### **Testing with <code>pytest</code></strong>

Automated testing ensures your data processing and analysis functions work as expected. **<code>pytest</code>** is a common framework for writing tests in Python. This action will install your project's dependencies from a `requirements.txt` file and then run your test suite.

```YML
name: Test
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests with pytest
        run: pytest
```

### **Validating Jupyter Notebooks**

If your project includes Jupyter Notebooks, it's a good practice to ensure they can run from top to bottom without errors. This action uses **<code>nbconvert</code>** to execute the notebook, which helps catch issues in your analysis workflow.

```YML
name: Validate Notebook
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: pip install nbconvert ipykernel
      - name: Run notebook
        run: jupyter nbconvert --to script --execute 'path/to/your/notebook.ipynb'
```

## **JavaScript Example:** 

### **Using ESLint**

For JavaScript and TypeScript, the industry standard linter is **ESLint**. You would run it using `npx` after setting up a Node.js environment.

Create a file like `.github/workflows/lint-js.yml`:

```YML
name: Lint JavaScript

on: [push, pull_request]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20' # Specify your Node.js version
      - name: Install dependencies
        run: npm install
      - name: Run ESLint
        run: npx eslint . --ext .js,.jsx,.ts,.tsx
```

## **C# Example:** 

### **Using the .NET CLI**

For C#, you typically use the built-in formatting and analysis tools provided by the **.NET command-line interface (CLI)**. The `dotnet format` command can check your code against your project's `.editorconfig` rules.

Create a file like `.github/workflows/lint-cs.yml`:

```YML
name: Lint C#

on: [push, pull_request]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-dotnet@v4
        with:
          dotnet-version: '8.0.x' # Specify your .NET version
      - name: Restore dependencies
        run: dotnet restore
      - name: Check formatting
        run: dotnet format --verify-no-changes
```

## **Recommended Structure**

You should create a different file for each action.

It's best practice to put each of those distinct workflows, lint, test, and validate into its own YAML file within the `.github/workflows/` directory.

Your repository should look something like this:

```shell
.github/
└── workflows/
    ├── lint.yml
    ├── test.yml
    └── validate_notebook.yml
```

### **Why Separate Files Are Better**



* **Clarity and Organization**: Each file has a single, clear purpose. This makes your automation setup much easier to understand and manage as your project grows.
* **Parallel Execution**: GitHub runs workflows from separate files in parallel by default. This means your linting, testing, and notebook validation can all run at the same time, giving you much faster feedback on your pull requests.
* **Independent Status Checks**: In a pull request, you'll see a separate, independent check for each workflow. This makes it immediately obvious which specific part of your process failed, without needing to dig into the logs of a single, large workflow.

While you *can* put multiple jobs in a single workflow file, separating them into different files is the standard and more scalable approach.

```shell
my_data_project/
├── .github/
│   └── workflows/
│       └── test.yml              <-- The workflow instructions
├── my_project_code/
│   └── data_analysis.py
├── tests/
│   └── test_data_analysis.py     <-- Your pytest test file goes here
└── requirements.txt
```

### **When your YAML uses another file example**

We will look at the structure for running a python pytest file. You include the pytest file in your project's source code, **not** in the workflow folder or inside the YAML file.

The YAML workflow file only contains the *instructions* to run your tests. The `pytest` command, when executed by the workflow, looks for your test files within your repository's directory structure.

**How It Works**

1. **Your Project Structure**: Your tests should live in a dedicated `tests/` folder in the root of your project, alongside your source code.
2. **The Workflow File (<code>test.yml</code>)**: This file tells GitHub Actions to check out your code, install your dependencies (including `pytest`), and then run the `pytest` command.
3. **Execution**: When the workflow runs, `pytest` automatically discovers and runs the test files (like `test_my_functions.py`) located in your `tests/` directory.

Here’s what your project layout should look like:

```shell
my_data_project/
├── .github/
│   └── workflows/
│       └── test.yml              <-- The workflow instructions
├── my_project_code/
│   └── data_analysis.py
├── tests/
│   └── test_data_analysis.py     <-- Your pytest test file goes here
└── requirements.txt
```