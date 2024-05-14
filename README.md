# AI-Powered Academic Research Assistant

Our project aims to aid students in computer science, or those passionate about the field, in comprehending research papers more easily. This research assistant seeks to empower students, making their academic endeavors more efficient and contributing to advancements in the field of computer science. It’s potential lies in easing the burden on students when it comes to retrieving information, conducting data analysis, and navigating through extensive literature.



## Working Implementation



## Proposed Solution
- The proposed solution is to design an AI-powered academic research assistant that utilizes document scraping, machine learning, and natural language processing techniques to enhance the research process. 
- The project will culminate in the development of a user-friendly web interface where users can input topics, browse search results, and explore papers.
- Then the system will dynamically generate lay summaries from three distinct papers related to the specified topic. 
- Each summary will be presented with the paper's title displayed at the top, accompanied by key takeaways extracted from the content of each paper. 
- This streamlined approach aims to provide users with concise yet comprehensive insights, facilitating a more accessible and efficient research process.
- This project uses the LongT5 model which is trained on the [Scisumm](https://cs.stanford.edu/~myasu/projects/scisumm_net/) dataset and the [textsum](https://pypi.org/project/textsum/) package for summarization.
- The model card can be found at [daniel-was-taken/long-t5-scisumm-accelerate-v2](https://huggingface.co/daniel-was-taken/long-t5-scisumm-accelerate-v2)

## Installation 

> [!NOTE]
> In case of any errors or issues while installing, refer to the Resources section in the README.

1. Create a virtual environment.
   - In this project we use the virtualenv package which can be installed by running ``` pip install virtualenv ``` in the terminal.
   - Create a virtual environment by running ``` python -m virtualenv venv ```
   - Activate the virtual environment by running ``` venv\Scripts\activate ``` on Windows.
    
2. Install the required packages.
   - The packages can be installed by running ``` pip install -r requirements.txt ```.
   - This should install the necessary packages, however, some packages could be deprecated.
  
3. Run the project.
   - To start the project run ```flask app run``` in the terminal.
    
## Resources

- virtualenv ([https://pypi.org/project/virtualenv/](https://virtualenv.pypa.io/en/latest/installation.html))
- Flask Documentation (https://flask.palletsprojects.com/en/3.0.x/)
- textsum (https://pypi.org/project/textsum/)
- Finetuned from ([pszemraj/long-t5-tglobal-base-sci-simplify](https://huggingface.co/pszemraj/long-t5-tglobal-base-sci-simplify))


