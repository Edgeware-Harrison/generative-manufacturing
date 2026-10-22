---
title: "Intent, not drawings"
description: "Why the drawing belongs in the middle of the process, not at the front door, and what a system owes a person who states a need in plain words."
status: draft
---

# Intent, not drawings

Drawings are the language factories need. They aren't the language people have. Today, anyone who wants something custom made has to produce a drawing or pay someone to, and that requirement quietly decides who gets to ask. Generative Manufacturing (GenM) moves the drawing out of the front door. A person states intent, and a system produces the drawing, the parts list, and the plan in the middle of the process, then stands behind the result with a commitment, not a stack of drawings. The test is simple and it can fail: can making start without a drawing or a catalog item? If it can't, the front door hasn't moved.

## Before the drawing

When I was a kid, my grandmother made tofu for the family. She grew the beans, soaked them, ground them, and set the curd herself. Neighbors dropped by to help. Nobody wrote a specification, because the person who wanted the tofu and the person who made it were the same person. Intent needed no translation.

Then production and consumption came apart. Today most of us buy tofu from a central factory with a cold chain behind it. We get good, cheap food, and we gave up any say in how it's made. When people wanted more control, home soy milk and tofu machines appeared and brought some production back into the house. Using and cleaning them stayed complicated.

I think the same thing happened to physical objects, with one difference. Most people can't make a bowl or a shelf at home without tools and skills they don't have. So the separation hardened into a language barrier, and the drawing is where the barrier sits.

## Why drawings sit at the front door

A drawing does a real job. It's an unambiguous contract between whoever designs a thing and whoever makes it. Without one, a shop can't quote, plan, or build. I'm not arguing against drawings.

I'm arguing against where we put them. Because the shop needs one, the person with the need has to supply one, or hire someone who can. That's the gate. People who can't speak drawings, bills of materials, process routes, and minimum order quantities don't get custom work. They settle for the nearest item on the menu.

I've written down why custom work is so expensive. Information passes through layers from customer to factory, and each layer risks decay and misunderstanding. A mistake on a one-off is a total loss, so the factory adds a risk premium to the quote. A custom order also interrupts the line, which costs money every time. The drawing is the best tool for a hard job. The job is hard because the need and the machine speak different languages.

## What intent contains

Intent is what a person would say if nobody asked them to translate. It has four parts. What the thing has to do. Where and how it will be used. What it can't exceed, such as size, budget, or time. And how they'd know it worked.

The last part gets forgotten. "A sensor that filters formaldehyde and fits a study corner" is an example from my own notes. It names a function, a place, and a limit. A good system would also ask how the person will judge success: air quality, noise, how it looks. Intent without an acceptance test is a wish, and nobody can deliver against a wish.

Intent is also incomplete on purpose. People shouldn't have to know every answer before they ask. The system's job is to fill the gaps by asking, to bound what's possible, and to refuse what can't be done and say why in plain words.

A prompt isn't the same thing. If a prompt gets you a picture, it has produced a picture. Intent is met when something physical matches it.

## An example (hypothetical)

*This is an illustration. I haven't delivered this case.*

A bakery owner needs a display for the front counter. It has to fit under a window, hold trays at several heights, and survive being wiped down every day. She has a budget ceiling and wants it in time for a seasonal menu.

She says exactly that, in plain words, and gives the window gap. She doesn't draw anything.

The system asks two questions she can answer standing at the counter: how heavy a loaded tray gets, and whether the window is ever opened. It tells her the thin shelf she pictured won't carry loaded trays across that span, and it offers two alternatives, each with a cost and a delivery date. She picks one.

From there the system produces what a shop needs: dimensions, connections, a parts list, cutting files, assembly steps, inspection rules. She never reads them. A shop makes the display. Then it's checked against what she said. Does it fit under the window? Do the trays stay level? Does it wipe clean? Anything that fails goes back into the next version, and she receives a commitment that says what was checked and by whom.

Every step in that story has to be real for the claim to count. I'm describing a target, not a result.

## Why a faster drawing isn't the answer

A tempting shortcut is to let AI draw. Describe an object, get geometry back. That's a real advance. But look at who has to read the result. If the requester has to review and approve the geometry, they're still in the producer's language, and the drawing has only gotten cheaper.

A generated model is a drawing made faster. It leaves the hard questions to somebody later. Will it hold? Can this shop make it? What will it cost, and when will it arrive? A system that really moves the front door has to answer those questions itself before it asks the person to say yes.

## The order of truth

When the drawing moves to the middle, something else has to be the thing everyone can trust. I use a rule from my own product notes: structure comes first and appearance second. Dimensions, connections, parts, cutting files, assembly steps, and inspection rules are the truth. A rendering helps a person decide. It must never overrule the structure, and nothing should be built from it alone.

Different people need different levels of that truth. The person who stated the need should see what it will look like, what can change, what it costs, and when it arrives. The shop should see the files. Nobody should be forced to read a level they didn't ask for. The system is responsible for making sure that what the person sees is backed by structure that can actually be built. If it says a part can be swapped later, there has to be a real joint behind that sentence.

## What the system owes in return

Taking someone's intent is a promise, so it creates a debt. In return for a plain-language request, the system owes the person a commitment. That means a statement of what will be delivered, the cost, the date, what was checked against their intent, and who checked it. A stack of drawings isn't a commitment. A stack of drawings tells the person to go and find out.

I think this is where the idea gets real or doesn't. Anyone can build a friendly front end that accepts a sentence. The hard part is standing behind the sentence after the physical thing exists, and being specific about which parts of the promise were verified and which weren't.

## What this has to do with rights

This is the practical meaning of giving authorship back. Authorship isn't a feeling of ownership. It's being able to say what you need and have it taken seriously, without first learning someone else's language.

Here is a test I use, and it can fail. If a person must learn bills of materials, process routes, or a module catalog before they can order, the right hasn't come back. That test may cut against many products that call themselves custom. I haven't checked any by name.

## Where this could fail

Three problems stay open, and the evidence on each is insufficient.

First, questions can become a new gate. A system that asks twenty things before it will help has brought the producer's language back through the side door. I can't yet say how many questions are too many.

Second, acceptance tests. "Feels sturdy" and "looks warm" aren't measurable. Turning them into checks someone can run, without forcing people to specify everything up front, is an unsolved design problem.

Third, accountability. Someone has to sign the commitment. My working hypothesis is that whoever runs the verification signs for what was actually checked. I haven't tested it.

I also don't have a measured case in which a stranger stated a need in plain words and received a verified physical result. That evidence is insufficient, and I won't pretend otherwise.

## What I'm asking

If you build things, tell me where the front door breaks. Has anyone ordered a physical thing from plain intent and received what they meant? What did it take? Where would you push back?

Follow for the next notes.

Reference page: [https://whatisgenm.com](https://whatisgenm.com)

Generative Manufacturing (GenM) is the manufacturing paradigm in which AI compiles human intent into fulfillable physical outcomes, so the demand side speaks in intent and verified engineering paths make good on it.
