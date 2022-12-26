# ai-jobs
ai-jobs is a tool that uses GPT-3 to write resumes and cover letters for jobs.

## Installation
To install ai-jobs, clone the repository and install the dependencies:

```bash
git clone https://github.com/supervised/ai-jobs.git
cd ai-cover-jobs
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
    save="cover_letter.txt",
    what='cover',
)
```

The write function accepts the following options:

* `background`: The name of the YAML file containing the user's background. This file should contain a list of dictionaries, each representing a job or education experience.

* `job`: The name of the text file containing the job posting.

* `save` (optional): The name of the file to save the output to. If not provided, the output will be printed to the console.

## License
ai-jobs is released under the MIT License.

## Credits
ai-jobs uses the OpenAI GPT-3 library to generate the cover letters.

## Disclaimer
ai-jobs is provided "as is", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software.

## Contribute
We welcome contributions to ai-jobs! If you have an idea for a feature or bug fix, please open an issue or submit a pull request.



