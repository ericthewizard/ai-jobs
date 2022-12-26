# ai-jobs
ai-jobs is a tool that uses GPT-3 to write cover letters and resumes for jobs.

## Installation
To install ai-jobs, clone the repository and install the dependencies:

```bash
git clone https://github.com/supervised/ai-jobs.git
cd ai-jobs
pip install -r requirements.txt
```

You will also need to obtain an API key for the OpenAI GPT-3 library.

## Usage
To use ai-jobs, import the `jobs` module and call the `write` function:

```python
import jobs

jobs.write(
    background="background.yaml",
    job="job_posting.txt",
    what="cover",
    temperature=0,
    max_tokens=1024,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    best_of=3,
    save="cover_letter.txt",
)
```

The write function generates a cover letter or a resume based on the what option and uses the GPT-3 options provided to control the generation. It accepts the following options:

- `background`: The name of the YAML file containing the user's background. This file should contain a list of dictionaries, each representing a job or education experience.

- `job`: The name of the text file containing the job posting.

- `what`: The type of content to generate. This can be either "cover" for a cover letter or "resume" for a resume.

- `temperature`: The temperature to use for sampling. Higher values means the model will take more risks. Try 0.9 for more creative applications, and 0 (argmax sampling) for ones with a well-defined answer.

- `max_tokens`: The maximum number of tokens (words and word pieces) to generate in the prompt.

- `top_p`: Controls the proportion of the mass of the distribution to be included in the top_p mass of the sorted list of candidates. If top_p is 1, then the model will always select the most likely token. If top_p < 1, then the model will consider a subset of the sorted list.

- `frequency_penalty`: Controls the relative importance of frequency of appearance and novelty. If frequency_penalty is 0, then the model will prefer novel tokens. If frequency_penalty is > 0, then the model will penalize novel tokens.

- `presence_penalty`: Controls the relative importance of presence in the prompt and absence. If presence_penalty is 0, then the model will prefer tokens that are not present in the prompt. If presence_penalty is > 0, then the model will penalize tokens that are not present in the prompt.

- `best_of`: The number of top candidates to consider for each token. Higher values means slower decoding and higher quality.

- `save` (optional): The name of the file to save the output to. If not provided, the output will be printed to the console.

## License
ai-jobs is licensed under the MIT License. See the LICENSE file for more information.

## Credits
ai-jobs uses the OpenAI GPT-3 library to generate the cover letters.

## Disclaimer
ai-jobs is provided "as is", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software.

## Contribute
We welcome contributions to ai-jobs! If you have an idea for a feature or bug fix, please open an issue or submit a pull request.