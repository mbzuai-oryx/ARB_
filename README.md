

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
  [![Our Page](https://img.shields.io/badge/Visit-Our%20Page-C5D9D9?style=flat)](https://mbzuai-oryx.github.io/ARB/)
  [![GitHub issues](https://img.shields.io/github/issues/mbzuai-oryx/Camel-Bench?color=D8EADC&label=issues&style=flat)](https://github.com/mbzuai-oryx/ARB/issues)
  [![GitHub stars](https://img.shields.io/github/stars/mbzuai-oryx/TimeTravel?color=C7D7E3&style=flat)](https://github.com/mbzuai-oryx/ARB/stargazers)
  [![GitHub license](https://img.shields.io/github/license/mbzuai-oryx/Camel-Bench?color=C8B9A7)](https://github.com/mbzuai-oryx/ARB/blob/main/LICENSE)
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
 🤗  **[22 May 2025]** ARB dataset available on [HuggingFace](https://huggingface.co/datasets/MBZUAI/ARB).<br>

<br>
<br>

  
<div align="left">
  
## <img src="https://github.com/user-attachments/assets/4e69bf65-7b6e-4dd4-8eda-d38b9f1049fc" width="40" height="40" /> ARB Scope and Diversity
 

ARB  is the first benchmark focused on  step-by-step reasoning in Arabic cross both textual and visual modalities, covering 11 diverse domains spanning science, culture, OCR, and historical interpretation.
<br>
</p>
<p align="center">
   <img src="assets/arb_sample_intro.png" width="750px" height="500px" alt="Figure: ARB Dataset Coverage"/>
</p>
</div>
</p>

## 🌟 Key Features

- **1,356** multimodal samples, each with an image, Arabic question, and reasoning-based answer.
- **5,119** curated reasoning steps reflecting human logic
- **11 diverse domains**, from visual reasoning to historical and scientific analysis.
- **Native Arabic speakers** and **domain experts** verified.
- **Hybrid sources**: original Arabic data, high-quality translations, and synthetic samples.
- **Robust evaluation framework** for final answer accuracy and reasoning quality
- Fully **open-source dataset** and toolkit to support research in **Arabic reasoning and multimodal AI**.

<br>

## 🏗️ ARB Construction Pipeline

<p align="center">
   <img src="assets/arb_pipeline.png" width="750px" height="180px" alt="Figure: ARB Pipeline Overview"/>
</p>

<br>

## <img src="https://github.com/user-attachments/assets/626aedcd-fdb0-4a1f-87de-bad0574900e5" width="30" height="30" /> ARB Collection

<p align="center">
   <img src="assets/arb_collection.png" width="600px" height="300px" alt="Figure: ARB Collection"/>


</p>
<br>

## <img src="https://github.com/user-attachments/assets/bdd52751-8503-4b30-9a85-e4e17f69242c" width="30" height="30" /> ARB Data Distribution over Domains

<p align="center">
   <img src="assets/arb_dist.png" width="400px" height="350px" alt="Figure: ARB dist"/>
</p>

<div align="center">
  
### Source Types Across Domains

| **Domain**                 | **English Bench** | **Arabic Bench** | **Human-Created** | **Synthetic** |
|---------------------------|:-----------------:|:----------------:|:-----------------:|:-------------:|
| Visual Reasoning          | ✅                | –                | –                 | –             |
| OCR & Document Analysis   | –                 | –                | ✅                | ✅            |
| Chart & Data Table (CDT)  | ✅                | ✅               | ✅                | ✅            |
| Math & Logic              | ✅                | –                | –                 | –             |
| Social & Cultural         | ✅                | –                | –                 | –             |
| Computer Vision Perception| ✅                | –                | –                 | –             |
| Medical Image Analysis    | ✅                | ✅               | –                 | –             |
| Scientific Reasoning      | ✅                | –                | –                 | –             |
| Agricultural Interpretation | ✅              | –                | ✅                | ✅            |
| Remote Sensing Understanding | –             | ✅               | –                 | –             |
| Historical & Anthropological | ✅            | –                | ✅                | ✅            |

</div>
<br>

## <img src="https://github.com/user-attachments/assets/2e19e70d-4f4d-4a98-a200-854a80de3cb9" width="30" height="30" />  Download

```bash
from datasets import load_dataset

# Login using e.g. `huggingface-cli login` to access this dataset
ds = load_dataset("MBZUAI/ARB")
```
<br>

## <img src="https://github.com/user-attachments/assets/b9105099-639c-4411-8949-9fc4b7f6b86a" width="30" height="30" />  Evaluation Protocol
<div>
<p align="left">
  
We evaluated 12 open- and closed-source LMMs using:</p>
- **Lexical and Semantic Similarity Scoes**: BLEU, ROUGE, BERTScore.</p>
- **Cross-lingual semantic alignment**: LaBSE</p>
- **Custom Rubric (Arabic):**: Our curated metric rebric includes 10 factors like faithfulness, interpretive depth, coherence, hallucination, and more.</p>

### <img src="https://github.com/user-attachments/assets/9a10bc39-78ff-41d8-97f8-7cef32df518e" width="30" height="30" /> LLM-as-Judge (Arabic prompt-based)

We evaluate models using:

- Step-by-step reasoning quality (coherence, informativeness, commonsense)
- Final answer accuracy
- Agreement with human raters (Krippendorff’s Alpha > 87%)
</p>
</div>
<br>

## <img src="https://github.com/user-attachments/assets/508bcdab-08e2-48e0-b89f-94b76190fdc0" width="30" height="30"> Stepwise Evaluation Results 
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


## <img src="https://github.com/user-attachments/assets/08e47f66-e0aa-49b5-b886-ad65ae7a6faa" width="30" height="30" /> Citation
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
