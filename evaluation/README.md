# GPT-4o Mini Response Evaluation Pipeline

This repository provides a Python-based evaluation pipeline to assess the accuracy of model-generated answers against ground truth responses using OpenAI's GPT-4o model. It uses a structured system prompt and invokes the OpenAI Chat Completion API to rate the alignment of responses on a binary accuracy scale.

## 🧠 Project Overview

The script performs the following tasks:

1. Loads a dataset of questions, model responses, and ground truth answers.
2. Evaluates each model response for **accuracy** by comparing it to the ground truth using GPT-4o.
3. Appends the result as a numeric score (0 or 1) in a new column `Final Answer Score`.
4. Exports the final DataFrame to a new CSV file.
5. Computes the overall mean score to assess model performance.


## 🔧 Dependencies

Ensure the following Python packages are installed:

```bash
pip install openai pandas pillow tqdm
```

## 📄 How It Works

### Key Components

* **`compare_results()`**: Sends prompt to GPT-4o to evaluate if the model's response semantically matches the ground truth.
* **`process_row()`**: Processes each row in the dataset and appends the evaluation score.
* **`ThreadPoolExecutor`**: Speeds up evaluation by concurrently processing rows.

### The script expects the input CSV (gpt-4.1-final-responses.csv) to have the following columns:

| question | choices | Ground Truth steps | Response Answer |
| -------- | ------- | ------------------ | --------------- |
| ...      | ...     | ...                | ...             |

> Choices are optional and not used in this evaluation function.

## 🚀 Running the Script

1. Set your OpenAI API key:

   ```python
   openai_api_key = "your-api-key"
   ```

2. Place your dataset at the correct path:

   ```python
   df = pd.read_csv("/path/to/gpt-4o-mini-responses.csv")
   ```

3. Run the script. It will:

   * Evaluate each response
   * Save the new results in `gpt-4o-mini-final-answer-evaluation-results.csv`
   * Print the mean accuracy score

## 🧪 Output

* A CSV file with an additional column: `Final Answer Score` (0 or 1)
* Printed overall average score showing model performance

## 📝 Notes

* Ensure your OpenAI API key has access to the GPT-4o model.
* API calls can incur cost. Consider batching or sampling for large datasets.
* Avoid using deprecated Pillow attributes like `textsize`; use `textlength` for width and `font size * lines` for height.
