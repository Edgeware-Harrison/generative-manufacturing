---
title: "Why no one has a compiler for physical things yet"
description: "Six jobs a compiler for physical things would have to do, who covers which part, and where the evidence runs out."
status: draft
---

# Why no one has a compiler for physical things yet

Several efforts already say "compiler" or "generative manufacturing" about physical work, so my claim is narrower than the title might suggest. As far as I could find, nobody has a system where a person states a need in their own words and is held to a verified physical result. Between the need and the factory sits a chain of human translators. Each one turns the need into a different document, and each hand-off loses something. A compiler for physical things would have to replace that chain. This essay lists the jobs it would have to do, says who is doing which part, and marks where the evidence runs out. Nobody has shown all of it working, and I haven't either.

## What a compiler actually does

Software people take compilers for granted, so it's worth saying what one does.

It reads a language a person can write. It checks the program and refuses the ones that can't run, before anything runs. And it produces an executable for a specific target machine, one that fits that machine's real limits.

Two other things make this work in software. Running a program costs almost nothing, so a failed run is cheap. And the target machine behaves the same way every time. Neither is true in a factory. A failed run uses material, machine time, and calendar days. And no two shops, machines, or material lots behave quite alike.

That's why I don't think the answer is to copy software's compiler. The answer is to build the jobs it does, in a world where mistakes cost money.

## The chain that stands in for a compiler

Follow a custom order through a traditional supply chain. A person says what they want. Someone turns that into a spec. Someone draws it. Someone lists the parts. Someone plans the route through the shop. Someone quotes it. Every step is a person translating into the next person's vocabulary.

I've written down what this costs. Information passes from customer to factory through layer after layer, and the chance of decay and misunderstanding grows with each one. If a custom product comes out wrong, all of it is scrap, so factories build a large risk premium into the quote. Custom work also breaks the rhythm of a line. Every switch and interruption costs money.

I've seen the same structure shape products in furniture, an industry where I spent ten years running an ODM factory. A brand wants shorter lead times, so the factory buys automation. Automation only pays at volume, so the brand makes the design more generic. A second brand sees the generic design sell and asks the same line for something close. Customers end up with lookalike products and buy the cheapest one. Nobody in that loop was careless. The system rewards copying and punishes change, and a compiler would have to flip that.

## Why the chain survives

If the chain is so lossy, why is it still there? Part of the answer is that every translator in it is also a business. The person who turns a need into a drawing, the person who plans the route, and the person who prices the job each earn a living from being necessary. Removing the language gap removes some of those jobs, and nobody inside the chain has a reason to hurry that along.

The other part is economic. Batch production makes copying cheap and changing expensive, so a drawing frozen once and reused many times is the sensible unit. In that world a custom request is an exception that has to be handled by hand. A compiler only makes sense if the unit changes, from a fixed design that gets replicated to a path that gets generated and checked for each request. I haven't seen that change prove itself at scale, and my own evidence is insufficient, but it explains why the chain has lasted this long.

## The shortcut I tried first

When I first took this problem seriously, I assumed a universal machine would solve it. I tested that idea on 3D printers, from desktop models to near-industrial ones, in a small print matrix.

Small parts worked. A connector prototype took about eight hours, which was fine. Then we tried a table leg. The software estimated 79 hours for one of four. The plastics we could afford looked cheap and cracked between layers under load. Longer prints failed overnight, and in the morning we found a tangle of filament instead of a part.

The lesson I took wasn't that printing is bad. A machine that can make any shape doesn't know what it can promise. A compiler has to know the limits of its target and say so. This was a small internal test, and I'm not drawing a general conclusion about printing today. The evidence for that is insufficient.

## What a compiler for physical things has to do

Here are the six jobs I'd hold any candidate to. Each comes with a test that could fail.

**1. Accept intent in the requester's terms.** A person should be able to say what the thing has to do, where it goes, and what it can't exceed. One example from my own notes is a sensor that filters formaldehyde and fits a study corner. No part numbers. Test: can the system start making something without a drawing or a catalog item? If it can't, intent isn't the input.

**2. Say no before material is spent.** This is the software type checker's job. Before anything is cut or printed, the system should check tolerances, loads, process limits, cost, and lead time, and tell the person in plain words what won't work and why. Carnegie Mellon's paper on its Generative Manufacturing compiler does a version of this for parts. It probes suppliers first and drops infeasible combinations of process and material before it runs the design optimizer, and it can explain why a given method is infeasible under the constraints ([arXiv](https://arxiv.org/abs/2409.03089)). Test: does the system refuse bad requests early, and can someone who isn't an engineer understand the refusal?

**3. Know the real limits of the machines it targets.** A plan is only as good as its knowledge of the shop that will run it: which machines are free, which materials are in stock, what tolerances that shop actually holds. Test: does the system work from the current state of real shops, and does its answer change when that state changes?

**4. Go beyond a fixed module library.** I taught myself some programming years ago, and it changed how I think about this. Software isn't built by stacking a fixed set of blocks. It's written. A system that can only combine pre-made modules is modular, which is useful but limited. Test: can it express a constraint or a continuous parameter that isn't in its library?

**5. Produce structure before pictures, and stand behind it.** The output of a compiler is something a machine can run. For physical work, that means dimensions, connections, a parts list, cutting or machining files, assembly steps, inspection rules, a cost, and a lead time, plus a commitment that says what was checked and by whom. A render is a picture of an outcome, and a shop can't build from it. Test: can the output go to a shop without a human redrawing it, and does the person receive a commitment instead of a stack of files?

**6. Check the physical result and send failures back.** I offer this as a criterion, not as something anyone has achieved. A system that meets it compares the result with the original intent, and what failed changes the next attempt. A system that doesn't is a design tool, and its generation is design acceleration. Test: after delivery, can the result be checked against the original intent, and does a failure change what the system does next? I'm not claiming any system has passed it.

## Who else uses these words

Three efforts I could open use the word compiler, "generative manufacturing," or both. Each covers part of the list.

The Carnegie Mellon work, supported by Lockheed Martin, takes engineering requirements, business requirements such as volume, cost, and lead time, and the current state of manufacturing resources. It generates process alternatives along with the designs each one implies. That covers job two for mechanical parts, and job three only in simulation, because the suppliers were configured for the study rather than real shops. In the results I read, two example parts, a cantilever bracket and a rocket engine mount, were worked out against those configured suppliers. I didn't find a physical build and test in the paper, so on job six the evidence there is insufficient. The authors also list assembly as future work.

CloudNC uses the exact phrase as a paradigm claim. In October 2024, its co-founder Chris Emery wrote that software "doesn't just generate designs for a component," and that its AI "creates the strategy to actually manufacture it." A user describes a component and its constraints, and the software produces a way to make it within the limits of scheduling, machine capability, and tooling, at the lowest overall cost ([CloudNC](https://www.cloudnc.com/blog/generative-manufacturing-or-how-to-transform-how-we-make-everything-forever)). The post says the company already does this for CNC programming, and it talks to shop owners about upskilling their staff. I didn't see it describe checking a finished part against what a requester asked for.

Atomic Machines came out of stealth on October 7 with a system it calls the Matter Compiler. The company says code alone decides which micro-machine gets built, with no molds, masks, or fixed tooling, and that the system measures and corrects every step in real time ([The Next Web](https://thenextweb.com/news/atomic-machines-250m-matter-compiler-micro-machines)). Its own page says its aim is "one-shot Prompt-to-Product" and that the process "starts with a prompt," after which the system designs, simulates, and writes its own process ([Atomic Machines](https://www.atomicmachines.com/matter-compiler)). That puts it closer to job one than I first assumed, and, if the claims hold, to jobs four through six in a narrow domain. But it is an aim. The first product is shipping to early-access customers for evaluation, the customers aren't named, and I found no published example of a request in a person's own words that ended in a verified delivered device. Evidence on that is insufficient.

## How my use of the term differs

I'm not the first to use the name, and I don't want to blur what's already there. Carnegie Mellon uses "generative manufacturing" for part-making optimization. CloudNC uses it for generating the manufacturing strategy that a shop runs. Both are valuable, and both speak mainly to the people who make things.

Generative Manufacturing (GenM), as I use it, is aimed at the person who has the need. It has two parts. The first is the paradigm, stated as a principle, with a commitment attached: a system compiles stated intent into a path that gets verified, and the person receives a commitment about what was checked and by whom. The second is who holds authorship: the demand side speaks in intent, and the producer's language stops being the price of admission. The overlap with these efforts is real on the first part. The second part is the one I haven't seen claimed, and I could be wrong about that.

For my own work the evidence is insufficient. I have no measured orders, costs, or lead times to point to, and I won't imply otherwise.

## Why I keep coming back to the first job

If a compiler only accepts an engineer's input, you've built a better factory. If it accepts intent, and refuses and explains in plain words, you've changed who gets to author what gets made. That's the part I care about most, and the one I'd most like to see tested by people who build things.

## Where I might be wrong

Maybe six jobs is too many, or the wrong six. Maybe physical verification costs too much to close for most products. Maybe the compiler metaphor misleads, because a factory has people and suppliers inside it and a program doesn't. If you've seen a system that does all six on a real product, or one that failed at the sixth, tell me. I'd like to see the evidence.

Follow for the next notes.

## Sources

- [Carnegie Mellon / Lockheed Martin, Generative Manufacturing paper (arXiv)](https://arxiv.org/abs/2409.03089)
- [CloudNC, "Generative manufacturing"](https://www.cloudnc.com/blog/generative-manufacturing-or-how-to-transform-how-we-make-everything-forever)
- [The Next Web, Atomic Machines Matter Compiler](https://thenextweb.com/news/atomic-machines-250m-matter-compiler-micro-machines)
- [Atomic Machines, Matter Compiler](https://www.atomicmachines.com/matter-compiler)

Reference page: [https://whatisgenm.com](https://whatisgenm.com)

Generative Manufacturing (GenM) is the manufacturing paradigm in which AI compiles human intent into fulfillable physical outcomes, so the demand side speaks in intent and verified engineering paths make good on it.
