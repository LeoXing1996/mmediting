_base_ = 'liif_edsr_norm_c64b16_g1_1000k_div2k.py'

experiment_name = 'liif_edsr_norm_c64b16_g1_1000k_div2k_srx18'
work_dir = f'./work_dirs/{experiment_name}'

scale_test = 18

data_root = 'data'
dataset_type = 'BasicImageDataset'
test_pipeline = [
    dict(
        type='LoadImageFromFile',
        key='gt',
        color_type='color',
        channel_order='rgb',
        imdecode_backend='cv2'),
    dict(
        type='LoadImageFromFile',
        key='img',
        color_type='color',
        channel_order='rgb',
        imdecode_backend='cv2'),
    dict(type='ToTensor', keys=['img', 'gt']),
    dict(type='GenerateCoordinateAndCell', scale=scale_test, reshape_gt=False),
    dict(type='PackEditInputs')
]

# test config for Set5
set5_dataloader = dict(
    num_workers=4,
    persistent_workers=False,
    drop_last=False,
    sampler=dict(type='DefaultSampler', shuffle=False),
    dataset=dict(
        type=dataset_type,
        metainfo=dict(dataset_type='set5', task_name='sisr'),
        data_root=data_root + '/Set5',
        data_prefix=dict(img='LRbicx4', gt='GTmod12'),
        pipeline=test_pipeline))
set5_evaluator = [
    dict(type='PSNR', crop_border=2, prefix='Set5'),
    dict(type='SSIM', crop_border=2, prefix='Set5'),
]

# test config for Set14
set14_dataloader = dict(
    num_workers=4,
    persistent_workers=False,
    drop_last=False,
    sampler=dict(type='DefaultSampler', shuffle=False),
    dataset=dict(
        type=dataset_type,
        metainfo=dict(dataset_type='set14', task_name='sisr'),
        data_root=data_root + '/Set14',
        data_prefix=dict(img='LRbicx4', gt='GTmod12'),
        pipeline=test_pipeline))
set14_evaluator = [
    dict(type='PSNR', crop_border=2, prefix='Set14'),
    dict(type='SSIM', crop_border=2, prefix='Set14'),
]

# test config for DIV2K
div2k_dataloader = dict(
    num_workers=4,
    persistent_workers=False,
    drop_last=False,
    sampler=dict(type='DefaultSampler', shuffle=False),
    dataset=dict(
        type='BasicImageDataset',
        ann_file='meta_info_DIV2K800sub_GT.txt',
        metainfo=dict(dataset_type='div2k', task_name='sisr'),
        data_root=data_root + '/DIV2K',
        # TODO: what this"
        data_prefix=dict(
            img='DIV2K_test_LR_bicubic/X4', gt='DIV2K_test_HR_sub'),
        filename_tmpl=dict(img='{}_x4', gt='{}'),
        pipeline=test_pipeline))
div2k_evaluator = [
    dict(type='PSNR', crop_border=2, prefix='DIV2K'),
    dict(type='SSIM', crop_border=2, prefix='DIV2K'),
]

# test config
test_cfg = dict(type='MultiTestLoop')
test_dataloader = [
    set5_dataloader,
    # set14_dataloader,
    # div2k_dataloader,
]
test_evaluator = [
    set5_evaluator,
    # set14_evaluator,
    # div2k_evaluator,
]
