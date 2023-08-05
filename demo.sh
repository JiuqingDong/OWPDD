# python demo/demo.py --config-file ./output/t1_final/config.yaml \
#   --input ./datasets/VOC2007/Inference/*.jpg \
#   --confidence-threshold 0.3 \
#   --output "./Visualize1/" \
#   --opts MODEL.WEIGHTS "./output/t1_final/model_final.pth"

python demo/demo.py --config-file ./output-R50-C4-imagenet/t1_final/config.yaml \
  --input ./datasets/VOC2007/Inference/*.jpg \
  --confidence-threshold 0.3 \
  --output "./Visualize/output-R50-C4-imagenet/t1_final" \
  --opts MODEL.WEIGHTS "./output-R50-C4-imagenet/t1_final/model_final.pth"


python demo/demo.py --config-file ./output-R50-C4-imagenet/t2_final/config.yaml \
  --input ./datasets/VOC2007/Inference/*.jpg \
  --confidence-threshold 0.3 \
  --output "./Visualize/output-R50-C4-imagenet/t2_final" \
  --opts MODEL.WEIGHTS "./output-R50-C4-imagenet/t2_final/model_final.pth"


python demo/demo.py --config-file ./output-R50-C4-imagenet/t3_final/config.yaml \
  --input ./datasets/VOC2007/Inference/*.jpg \
  --confidence-threshold 0.3 \
  --output "./Visualize/output-R50-C4-imagenet/t3_final" \
  --opts MODEL.WEIGHTS "./output-R50-C4-imagenet/t3_final/model_final.pth"


python demo/demo.py --config-file ./output-R50-C4-imagenet/t4_final/config.yaml \
  --input ./datasets/VOC2007/Inference/*.jpg \
  --confidence-threshold 0.3 \
  --output "./Visualize/output-R50-C4-imagenet/t4_final" \
  --opts MODEL.WEIGHTS "./output-R50-C4-imagenet/t4_ft/model_final.pth"