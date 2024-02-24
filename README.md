# ComfyUI-LLMs

The dolphin is wiring up OpenAI and local LLMs. OpenAI v1.2.3 is required.

![cyberdolphin.png](examples/cyberdolphin.png)


## Installation

Git clone this repo into the `custom_nodes` folder.
If necessary, check the pip requirements. It will be necessary.

## Examples

There are workflows in the [examples folder](./examples)
![img.png](examples/img.png)
---

## Nodes

The nodes all share a config file at `settings.yaml`. Provided with the repo is the
`settings.yaml.example` which can be copied to a new file called `settings.yaml`
for editing. The `settings.yaml` file is ignored by git.

### OpenAI GPT Node

**REQUIRES** STRING  `user_prompt`

The text is the user portion of the gpt prompt.
_Generates_ an engineered prompt
from a user-editable template config file with the user text embedded.
Dropdown select from available OpenAI models. Most of these will not work.
The models that DO work at the time of writing are at least, including but not limited to
**gpt-3.5-turbo** and **gpt-4**.
Runs the prompt gpt-3.5-turbo (or a user-selected alternative) with the text.

**PRODUCES** STRING.

### OpenAI Compatible Node

**REQUIRES** STRING `text`

The text is embedded in the user prompt.
Generates an "engineered" prompt from template.
The user text is embedded in the engineered prompt.
Calls for completion of the prompt to the user-defined URL.

**PRODUCES** STRING

### OpenAI DALL·E Node

**REQUIRES** STRING `text`

Calls OpenAI DALL·E with the text.

**PRODUCES** IMAGE


---

### Pip requirements

This collection has some extra requirements that are not present in the ComfyUI distribution.
Things like openai, gradio-client and technologist tools.

### Experimental

This is an experimental collection of nodes. This project needs validation on MacOS, Windows and Linux.
So far, it works on my machine which is a Linux distribution.

## Contributions

Looking for participants, happy to work on PRs!

**Guidelines for the Dolphin:**

* Keep it small - PRs should be quick and easy.
* Large things must be compositions of smaller things.
* Dependencies should be external - i.e. loaded by a node
* For example:
    * _the Llava loader node passes the Llava model to the recogniser node which uses the Llava model to emit a list of
      objects_
    * _and not, the "Llava node does everything"_

**Keep it small**

In the spirit of "Keep it small", I'm trying to make sure my big ideas for the dolphin
stay within the realm of LLMs -

Here are some big ideas that didn't make it into the roadmap for CyberDolphin:

#### Big Ideas I have for future things that are not the dolphin:

**Cam Nodes**

* **Webcam Node** for phone/laptop
* **Cam Node** for HDMI type input devices
* **Live Stream Node** to capture vision from a _Thing of the Internet_

**Speech to Text**

* **Microphone node** Captures spoken instructions into **audio node**
* Instructions are transcribed using
    * **OpenAI-Whisper node** or
    * _TTS model_ loaded by the **TTS node**

**The Simple Storybook Production Kit**

Where "LLM-node" is short for "LLM powered node":

```text
LLM-node dreams up the story type
LLM-node dreams up the character names, their badge
LLM-node dreams up the story title
LLM-node dreams up chapter summaries

LLM-node generates a page in "the story"

LLM-node generates images of characters:
    id badge,
    smiling photo,
    frowning photo,
    'character' shot

LLM-node generates prompt for page illustration
LLM-node generates page text
```

## License

GPL 3.