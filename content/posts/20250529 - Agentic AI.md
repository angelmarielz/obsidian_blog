## What is Agents?

AI Agents are programs where LLM outputs control the workflow. People often describes a solution as “AI Solution” that involves any of the following:  

1. Multiple LLM calls
2. LLMs with ability to use Tools
3. An environment where LLMs interact with each other
4. A planner to coordinate activities
5. Autonomy

## Difference between Workflow and Agents

1. Workflow - Systems where LLMs and tools are orchestrated through pre-defined code paths
2. Agents - Systems where LLM dynamically direct their own processes and tool usage, maintaining control over how they accomplish tasks

## Workflow Design Patterns

1. **Prompt Chaining**  
Use cases: Flows that could be divided. For example, split a long story into four episode and then translate them into different languages.

!![Image Description](/images/Pasted%20image%20202509111.png.png)

2. **Routing**  
Use cases: ICMs, applying category tags, customer service calls.

!![Image Description](/images/Pasted%20image%20202509112.png.png)

3. **Parallelization**  
Use cases: Monitoring

!![Image Description](/images/Pasted%20image%20202509113.png.png)
4. **Orchestrator-Worker**  
Use cases: Difficult tasks that needs to be solved in topological order, for example data analysis.

!![Image Description](/images/Pasted%20image%20202509114.png.png)

5. **Evaluation-Optimizer**  
Use cases: Translation and grammar check.

!![Image Description](/images/Pasted%20image%20202509115.png.png)

6. **Agents**

!![Image Description](/images/Pasted%20image%20202509116.png.png)


## Risk

1. Unpredictable Path
2. Unpredictable Output
3. Unpredictable Cost

## Hands-On

1. How to setup environment to call endpoint
2. Evaluation-Optimizer pattern demonstrate
3. How to define tools and how LLM is using it