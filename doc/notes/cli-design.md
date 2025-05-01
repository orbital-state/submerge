
## Commands

- **reflect**: Reflect on the current state of the code into `.div/contracts` files etc. This is the main command that will be used to generate the initial code and update it as the code changes.

- **ask**: Ask the agent by sending in the generated content of the prompt. The result is stored as `.div/response.json` files. File contains both the prompt and the response. Previous versions are moved into `.div/history/*.json` files.

- **plan**: Plan the next steps for the agent to take. This will generate a *plan* based on the current state of the code and the agent's goals.

- **apply**: Apply any actions in the *plan* as proposed by the agent to change the codebase. This may include modifying existing files or creating new ones as necessary. The idea is to check the difference with `git diff`. Hence, if the state is not committed, the agent will not be able to apply the changes. If configured, the agent will automatically work with `git stash` and `git stash pop` to revert.

- **test**: Run the tests in the codebase. This will be used to check if the changes made by the agent are working as expected. The agent will be able to run the tests and check if they pass or fail. If they fail, the agent will be able to debug the code and fix it.

- **thread**: Subset of commands that are related to the thread nodes (aka children or derived nodes) in the div-tree. This includes commands to add, remove, or modify nodes in the div-tree. 

- **status**: Check the status of the current thread. The root thread corresponds to `<project-root>/.div/` folder.