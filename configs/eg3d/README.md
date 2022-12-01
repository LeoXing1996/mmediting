# EG3D (CVPR'2022)

> [Efficient geometry-aware 3D generative adversarial networks](https://openaccess.thecvf.com/content/CVPR2022/html/Chan_Efficient_Geometry-Aware_3D_Generative_Adversarial_Networks_CVPR_2022_paper.html)

> **Task**: 3D-aware Generation

<!-- [ALGORITHM] -->

## Abstract

<!-- [ABSTRACT] -->

Unsupervised generation of high-quality multi-view-consistent images and 3D shapes using only collections of single-view 2D photographs has been a long-standing challenge. Existing 3D GANs are either compute-intensive or make approximations that are not 3D-consistent; the former limits quality and resolution of the generated images and the latter adversely affects multi-view consistency and shape quality. In this work, we improve the computational efficiency and image quality of 3D GANs without overly relying on these approximations. We introduce an expressive hybrid explicit-implicit network architecture that, together with other design choices, synthesizes not only high-resolution multi-view-consistent images in real time but also produces high-quality 3D geometry. By decoupling feature generation and neural rendering, our framework is able to leverage state-of-the-art 2D CNN generators, such as StyleGAN2, and inherit their efficiency and expressiveness. We demonstrate state-of-the-art 3D-aware synthesis with FFHQ and AFHQ Cats, among other experiments.

<!-- [IMAGE] -->

<div align=center>
<img src="https://user-images.githubusercontent.com/28132635/204269503-b66a6761-00e8-49ba-842f-65aae3110278.png"/>
</div>

## Results and Models

|    Model     |     Comment     | FID50k | FID50k-Camera |                  Config                  |  Download   |
| :----------: | :-------------: | :----: | :-----------: | :--------------------------------------: | :---------: |
| ShapeNet-Car | official weight | 5.6573 |    5.2325     | [config](/configs/eg3d/eg3d_shapenet.py) | [model](<>) |
|     AFHQ     | official weight | 2.9134 |    6.4213     |   [config](/configs/eg3d/eg3d_afhq.py)   | [model](<>) |
|     FFHQ     | official weight | 4.3076 |    6.4453     |     [config](/configs/eg3d_ffhq.py)      | [model](<>) |

- `FID50k-Camera` denotes image generated with random sampled camera position.
- `FID50k` denotes image generated with camera position randomly sampled from the original dataset.

### Influence of FP16

All metrics are evaluated under FP32, and it's hard to determine how they will change if we use FP16.
For example, if we use FP16 at the super resolution module in [FFHQ model](/configs/eg3d_ffhq.py), the output images will be slightly blurrier than the ones generated under FP32, but FID (**4.03**) will be better than FP32 ones.

## About generate images and videos with High-Level API

```python
TODO
```

Then you the following video will be saved.

<div align=center>
<video src="https://user-images.githubusercontent.com/28132635/204278664-b73b133b-9c3f-4a87-8750-133b7dedaebb.mp4"/>
</div>

TODO: To interpolate

<div align=center>
<video src="https://user-images.githubusercontent.com/28132635/204279787-09aa4764-d696-4abb-a21b-3fbf9c701d08.mp4"/>
</div>

You can also change random seed in your code.

TODO: seed 42

<div align=center>
<video src="https://user-images.githubusercontent.com/28132635/204280820-234e93c6-b7ec-4d1a-9346-4185fbdb6163.mp4 "/>
</div>

## How to prepare dataset

## Citation

```latex
@InProceedings{Chan_2022_CVPR,
    author    = {Chan, Eric R. and Lin, Connor Z. and Chan, Matthew A. and Nagano, Koki and Pan, Boxiao and De Mello, Shalini and Gallo, Orazio and Guibas, Leonidas J. and Tremblay, Jonathan and Khamis, Sameh and Karras, Tero and Wetzstein, Gordon},
    title     = {Efficient Geometry-Aware 3D Generative Adversarial Networks},
    booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
    month     = {June},
    year      = {2022},
    pages     = {16123-16133}
}
```
