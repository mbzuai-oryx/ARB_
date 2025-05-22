

<div align="center">
  <img src="assets/arab_logo.png" width="11%" align="left"/>
</div>

<div style="margin-top:50px;">
  <h1 style="font-size: 30px; margin: 0;">  ARB: A Comprehensive Arabic Multimodal Reasoning Benchmark</h1>
</div>

 <div  align="center" style="margin-top:10px;"> 
    
  [Sara Ghaboura](https://huggingface.co/SLMLAH) <sup> * </sup> &nbsp;
  [Ketan More](https://github.com/ketanmore2002) <sup> * </sup> &nbsp;
  [Wafa Alghallabi](https://huggingface.co/SLMLAH) &nbsp;
  [Omkar Thawakar](https://omkarthawakar.github.io)  &nbsp;
  <br>
  [Jorma Laaksonen](https://scholar.google.com/citations?user=qQP6WXIAAAAJ&hl=en) &nbsp;
  [Hisham Cholakkal](https://scholar.google.com/citations?hl=en&user=bZ3YBRcAAAAJ) &nbsp;
  [Salman Khan](https://scholar.google.com/citations?hl=en&user=M59O9lkAAAAJ) &nbsp;
  [Rao M. Anwer](https://scholar.google.com/citations?hl=en&user=_KlvMVoAAAAJ)<br>
  <em> <sup> *Equal Contribution  </sup> </em>
  <br>
  <br>  
  [![arXiv](https://img.shields.io/badge/arXiv-2502.14865-C4EAE5)](https://arxiv.org/abs/2502.14865)
  [![Our Page](https://img.shields.io/badge/Visit-Our%20Page-C5D9D9?style=flat)](https://mbzuai-oryx.github.io/TimeTravel/)
  [![GitHub issues](https://img.shields.io/github/issues/mbzuai-oryx/Camel-Bench?color=D8EADC&label=issues&style=flat)](https://github.com/mbzuai-oryx/TimeTravel/issues)
  [![GitHub stars](https://img.shields.io/github/stars/mbzuai-oryx/TimeTravel?color=C7D7E3&style=flat)](https://github.com/mbzuai-oryx/TimeTravel/stargazers)
  [![GitHub license](https://img.shields.io/github/license/mbzuai-oryx/Camel-Bench?color=C8B9A7)](https://github.com/mbzuai-oryx/TimeTravel/blob/main/LICENSE)
  <br>
  <em> <sup> *Equal Contribution  </sup> </em>
  <br>
  <br>
  

  
<p align="center">
    <img src="assets/line.png"  height="9px">
</p> 

</div>
<div align="center">
 <b> If you like our project, please give us a star ⭐ on GitHub for the latest update. </b><br>
</div>
<br>
<p align="center">
    <img src="assets/line.png" height="9px">
</p> 
<br>
<br>
</p> 

##  <img src="https://github.com/user-attachments/assets/1abcf195-ad44-4500-a14b-f1a4bef9b748" width="40" height="40" />Latest Updates
 🔥  **[22 May 2025]** ARB is **1st** Arabic multimodal benchmark focused on step-by-step reasoning is released.<br>
 🤗  **[22 May 2025]** ARB dataset available on [HuggingFace](https://huggingface.co/datasets/MBZUAI/TimeTravel).<br>

<br>
<br>

  
<div align="left">
  
## <img src="https://github.com/user-attachments/assets/42ae8138-bee1-414b-be7c-60378afdbc34" width="30" height="30" /> ARB Scope and Diversity
 

ARB  is the first benchmark focused on  step-by-step reasoning in Arabic cross both textual and visual modalities, covering 11 diverse domains spanning science, culture, OCR, and historical interpretation.
<br>
</p>
<p align="center">
   <img src="assets/arb_sample_intro.png" width="750px" height="500px" alt="Figure: ARB Dataset Coverage"/>
</p>
</div>
</p>

## 🌟 Key Features

- Includes **1,356** multimodal samples with **5,119** curated reasoning steps.
- Spans **11 diverse domains**, from visual reasoning to historical and scientific analysis.
- Emphasizes **step-by-step reasoning**, beyond just final answer prediction.
- Each sample contains a **chain of 2–6+ reasoning steps** aligned to human logic.
- Curated and verified by **native Arabic speakers** and **domain experts** for linguistic and cultural fidelity.
- Built from **hybrid sources**: original Arabic data, high-quality translations, and synthetic samples.
- Features a **robust evaluation framework** measuring both final answer accuracy and reasoning quality.
- Fully **open-source dataset** and toolkit to support research in **Arabic reasoning and multimodal AI**.

<br>

## 🏗️ ARB Construction Pipeline

<p align="center">
   <img src="assets/arb_pipeline.png" width="750px" height="180px" alt="Figure: ARB Pipeline Overview"/>
</p>

<br>

## 🗂️ ARB Collection

<p align="center">
   <img src="assets/arb_collection.png" width="600px" height="300px" alt="Figure: ARB Collection"/>



### 🔢 Source Types Across Domains

| Domain                    | English Bench | Arabic Bench | Human-Created | Synthetic |
| ------------------------- | ------------- | ------------ | ------------- | --------- |
| Math & Logic              | ✓             | –            | –             | ✓         |
| Remote Sensing            | –             | ✓            | –             | ✓         |
| Chart/Table Understanding | ✓             | ✓            | ✓             | ✓         |
| Visual Reasoning          | ✓             | –            | –             | –         |
| Historical Understanding  | ✓             | –            | ✓             | ✓         |

</p>
<br>

## 🗂️ ARB Distribution

<p align="center">
   <img src="assets/arb_dist.png" width="400px" height="350px" alt="Figure: ARB dist"/>
</p>

<br>

## 📥 Download

```bash
from datasets import load_dataset

# Login using e.g. `huggingface-cli login` to access this dataset
ds = load_dataset("MBZUAI/ARB")
```

## 🧪 Evaluation Protocol
<div>
<p align="left">
  
We evaluated 12 open- and closed-source LMMs using:</p>
- **Lexical and Semantic Similarity Scoes**: BLEU, ROUGE, BERTScore.</p>
- **Cross-lingual semantic alignment**: LaBSE</p>
- **Custom Rubric (Arabic):**: Our curated metric rebric includes 10 factors like faithfulness, interpretive depth, coherence, hallucination, and more.</p>


### 🎯 LLM-as-Judge (Arabic prompt-based)

We evaluate models using:

- Step-by-step reasoning quality (coherence, informativeness, commonsense)
- Final answer accuracy
- Agreement with human raters (Krippendorff’s Alpha > 87%)
</p>
</div>
<br>

## 🏆 Stepwise Evaluation Results 
For Closed-Source Models:<br>
|                     |   GPT-4o |   GPT-4o-mini |   GPT-4.1 |   o4-mini |   Gemini 1.5 Pro |   Gemini 2.0 Flash |
|:--------------------|---------:|--------------:|----------:|----------:|-----------------:|-------------------:|
| Final Answer (%)    |    60.22 |         52.22 |     59.43 |     58.93 |            56.7  |              57.8  |
| Reasoning Steps (%) |    64.29 |         61.02 |     80.41 |     80.75 |            64.34 |              64.09 |
<br>

For Open-Source Models:<br>
|                     |   Qwen2.5-VL-7B |   Llama-3.2-11B |   AIN |   Llama-4 Scout |   Aya-Vision-8B |   InternVL3-8B |
|:--------------------|----------------:|----------------:|------:|----------------:|----------------:|---------------:|
| Final Answer (%)    |           37.02 |           25.58 | 27.35 |           48.52 |           28.81 |          31.04 |
| Reasoning Steps (%) |           64.03 |           53.2  | 52.77 |           77.7  |           63.64 |          54.5  |

<br>

## 📂 Dataset Structure
<div>
<p align="left">

Each sample includes:
- `image`: Visual input
- `question`: Arabic reasoning prompt
- `choices`: The choices for MCQ
- `steps`: Ordered reasoning chain
- `answer`: Final solution (Arabic)
- `domain`: One of 11 categories (e.g., OCR, Scientific, Visual, Math)
- `curriculum`: One of the 4 curricula followed by the prompt for steps generation (Computational, Sci/Med, Textual/Partial, and General)
</p>

</div>


<br>
<div align="left">
  
## 📚 Citation
If you use ARB dataset in your research, please consider citing:

```bibtex
@misc{ghaboura2025timetravelcomprehensivebenchmark,
      title={}, 
      author={},
      year={2025},
      eprint={},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={}, 
}
```

</div>



---


<p align="center">
   <img src="assets/IVAL_logo.png" width="18%" style="display: inline-block; margin: 0 10px;" />
   <img src="assets/Oryx_logo.jpeg" width="12%" style="display: inline-block; margin: 0 10px;" />
   <img src="assets/MBZUAI_logo.png" width="40%" style="display: inline-block; margin: 0 10px;" />
</p>
