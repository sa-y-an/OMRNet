# OMRNet

### Introduction

OMR systems form the basis of many important examinations all over the world. However, existing Optical Mark Recognition (OMR) systems tend to be expensive and rigid in their operation, often resulting in erroneous evaluations due to strict correction protocols. 

<div align="center">
  <img src="https://github.com/sa-y-an/OMRNet/assets/55195504/87722e3b-f9b7-4145-9910-7be9e164aad6" height="50%" width="50%"  />
  <p>
    <i>
    Fig.: Some samples of the answer box images used in training. The samples are taken from the <a href="https://sites.google.com/view/mcq-dataset"> MC Answer Boxes dataset </a>
    </i>
  </p>
</div>

Few shortcommings of the modern day OMR are summarized below. 
- Extraction of skewed Region of Interests (ROI) due to misalignment of scanners. 
- The omr systems are rigid and template specific. The algorithm that works for one type of OMR will not necessarily work for another. 
- Thresholding based Algorithms 
- No scope to cross out a particular box.

## Our Work

In this work we have proposed a light weight Mobile Net V2 based classifier model OMRNet. OMRNet classifies answer boxes into three class: Marked, Empty and crossed-out. Furthermore, being trained on a diverse dataset (<a href="https://sites.google.com/view/mcq-dataset"> MC Answer Boxes dataset </a>) it can accomodate any skewness of answer boxes. The neural network architecture of the model is shown below. 

<div align="center">
  <img src=https://github.com/sa-y-an/OMRNet/assets/55195504/1c73b656-c53e-4de1-a7b2-d6d8a6b2c19a" height="50%" width="50%"  />
  <p>
    <i>
    Fig.: Transfer Learning on MobileNetV2 and our proposed model </a>
    </i>
  </p>
</div>

## Performance And Accuracy 

Since OMRNet will find its major applications in resource constraint regions we have designed our model to be extremely lightweight. Our model as of 13th July, 2023 has achieved the state of the art accuracy on the dataset. However, inspite of high accuracy it is extremely lightweight. We have described in detail about its light weightedness and how we achieved it in our paper. We have applied a quantization model to reduce its size 7 times. The quantized model is just <b> 3 MB </b>. 

<div align="center">
  <img src="https://github.com/sa-y-an/OMRNet/assets/55195504/23241c12-0246-4741-aa8c-69b12f76d694" height="50%" width="50%"  />
  <p>
    <i>
    Fig.: Comparison of the test accuracy of OMRNet and post quantized OMRNet.
    </i>
  </p>
</div>
