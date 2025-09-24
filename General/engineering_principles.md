<div align="center">
    <h1> Engineering Principles </h1>
</div>

Engineering, whether in software, mechanical, electrical or other domains requires more than technical competence in tools or languages. True engineering maturity is measured in **consistency, reliability and foresight**. The ability to anticipate challenges, align work with overarching system constraints and deliver solutions that function correctly under expected and unexpected conditions.

For junior engineers, common mistakes include beginning work without full context, proceeding without iterative validation and discovering critical issues only near the end of development. These mistakes are rarely about a lack of intelligence or skill, they reflect insufficient process discipline.

## Preparation Before Development

The preparation phase determines whether development begins with clarity or hidden assumptions. Common mistakes in this phase include **misinterpreted requirements, undiscovered dependencies and unacknowledged edge cases**.

#### Key Mistakes

1. **Assuming Complete Requirements** - Accepting initial specifications are at face value without vertification or exploration.
2. **Limited Context Discovery** - Failing to understand the broader system or analogous implementations.
3. **Lack of Risk Assessment** - Not anticipating potential failure modes or areas of uncertainty.

#### Core Principles

1. **Understand Before You Act**

   - Build a mental model of the system. **The inputs, transformations and outputs**.
   - **Diagram workflows** and data flows to visualize dependencies.

2. **Identify Unknowns and Risks Early**

   - Conduct pre-mortems. Imagine failure and determine likely causes. This could be "Requirements were misunderstood", "Integration breaks existing functionality", "Performance is unacceptable" or "Data format assumptions are wrong".
   - Explore alternative data paths, edge cases and integration points.

3. **Stakeholder Alignment**

   - Restate requirements and assumptions to product managers, team leaders or peers.
   - Ask clarifying questions to uncover implicit constraints.

4. **Research Existing Patterns**

   - Review similar features or components in the codebase.
   - Reuse proven solutions to reduce novelty-related errors.

5. **Understand The Problem Domain**

   - Learn the business context, not just the technical requirements.
   - Think in systems, consider how your change affects the entire application.
   - For AC incompleteness, the suggestion is to create a **data flow diagram** showing all input sources. Additionally, confirmation of scope boundaries with product managers.

6. **Alternative Generation**

   - Create 2 to 3 different approaches to solve the problem. Evaluate each approach against criteria, maintainability, performance, complexity, alignment with existing patterns. Ensure your chosen approach follows existing system patterns and finally list what could go wrong with your approach.

In any engineering discipline, **preparation is not passive reading**. It is **active exploration and validation** of assumptions.

## Development and Iteration

The development phase is where most errors manifest when **uncertainty, design conflicts or assumptions go untested**.

#### Key mistakes

1. **Ignoring Conflicts Between Design Principles** - Choosing expedient solutions rather than reconciling or consulting peers.
2. **Overcommitting to a Single Implementation Path** - Investing heavily in a solution before validating critical assumptions.
3. **Insufficient Iterative Validation** - Not checking intermediate results against expectations or system constraints.

#### Core Principles

1. **Design for Clarity, Consistency, and Maintainability**

   - Prefer solutions that are explicit and easily understood.
   - Conform to existing patterns or introduce neutral abstractions when necessary.

2. **Fail Early and Iterate Often**

   - Prototype uncertain or risky parts (“spikes”) before full implementation.
   - Pause development when **surprises occur to realign with requirements**.

3. **Continuous Validation**

   - Review intermediate work with peers or stakeholders.
   - Test incrementally against edge cases, not just nominal paths.

4. **Document Decisions and Trade-offs**
   - Keep records of design choices and their rationale.
   - This ensures that future engineers can understand context and reduces hidden assumptions.

Iterative validation and early feedback loops are universal engineering practices that minimize late-stage failure disciplines.

During development **stop and reassess if**,

1. You're writing more code than expected.
2. You're fighting the existing architecture.
3. You're creating new patterns instead of using existing ones.
4. You're adding many conditional branches or special cases.
5. You're modifying code in unexpected places.
6. Tests are becoming complex or brittle.

## Completion, Testing and Reflection

The final phase ensures that the solution integrates into the system and that lessons are captured for continuous improvement.

## Key Mistakes

1. **Limited End-to-End Testing** - Testing only the paths you anticipated rather than all realistic scenarios.
2. **Skipping Design Compliance Checks** - Overlooking whether the implementation aligns with system-wide principles.
3. **Ignoring Post-Implementation Reflection** - Failing to analyze mistakes or uncover process gaps.

**Core Principles**

1. **Test for Confidence, Not Just Coverage**

   - Evaluate normal, edge, and failure paths.
   - Simulate realistic workflows to ensure the system behaves correctly.

2. **Conduct Post-Implementation Review**

   - Assess what assumptions were wrong or incomplete.
   - Document lessons learned to improve future preparedness.

3. **Maintain a Continuous Improvement Mindset**
   - Treat each project as an opportunity to refine engineering judgment.
   - Incorporate insights into standards, checklists, or design guidelines.

Reflection and confidence-building testing are universal principles that prevent recurring mistakes and foster reliable execution.

## Cross-Cutting Engineering Principles

Beyond the three phases, several timeless engineering principles support reliable work across all domains.

1. **Separation of Concerns / Modularity**

   - Keep components focused and independent to reduce hidden dependencies.

2. **Single Responsibility Principle**

   - Each module or functionshould have on reason to change, enhancing clarity and maintainability.

3. **Defensive Engineering**

   - Assume that inputs, dependencies or assumptions may be violated.
   - Build validation and error handling proactively.

4. **Iterative Learning**

   - Engineering is as much about discovery as execution. Treat unknowns as expected and design processes to uncover them.

5. **Communication and Alignment**

   - Continuous dialogue with stakeholders is not optional. It is a force multiplier for preventing late-stage surprises.

6. **Core Questions**

   - Can I explain this problem to someone else in 2 minutes?
   - Have I found how similar problems were solved in this codebase?
   - Do I know exactly what "done" looks like?
   - Have I identified what could force me to restart?

## Engineering Mistakes

- **Having assumptions without validating them** - Assumptions in an Engineering process or feature development without validation can lead to poor decision making without the assumption validated. Additionally, if the assumption was incorrect and not validated early, it can lead the the entire development being halted due to code blockers or technical debt.
- **Accepting Acceptance Criteria at face value** - Expecting perfectly written Acceptance Criteria is never something to expect, discoveries can occur during development. Additionally, challenge the Acceptance Criteria for breaking scenarios.
- **Conflicting Design Principles** - Software Engineering can have multiple useful design principles, two may include DRY and 'only pass what is needed'. As an example, if you are not able to implement both patterns due to conflicts, it's best to step back and consider the bigger architectural design.
- **Simple Solution != Architecturally Correct** - Simple solutions do not mean they're architecturally correct. It's ideal to search for best practices and use framework best practices. A simple solution such as filtering may include framework filtering rather than self-written code filtering.

## Conclusion

The path of engineering progression is not defined solely by technical knowledge, but by the systematic application of engineering principles across all phases of work. Mistakes such as hidden assumptions, late discovery of edge cases or conflicting design choices arise **from gaps in preparation, iterative validation and reflection**.

By adhering to the following framework,

1. **Before Development** - Understand system context, identify risks, align assumptions, research analogous solutions.
2. **During Development** - Iterate, validate continuously, design for clarity and maintainability, document decisions.
3. **After Development** - Test thoroughly, review for compliance and capture lessons for continuous imporvement.
