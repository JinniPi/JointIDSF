export lr=5e-5
export c=0.6
export s=1234
echo "${lr}"
export MODEL_DIR=checkpoint/JointBERT-CRF_ATIS
export MODEL_DIR=$MODEL_DIR"/"$lr"/"$c"/"$s
echo "${MODEL_DIR}"
python3 main.py --token_level word-level \
                  --model_type atisbert \
                  --model_dir $MODEL_DIR \
                  --data_dir data/atis \
                  --seed $s \
                  --do_train \
                  --do_eval \
                  --save_steps 140 \
                  --logging_steps 140 \
                  --num_train_epochs 50 \
                  --tuning_metric mean_intent_slot \
                  --use_crf \
                  --gpu_id 0 \
                  --embedding_type soft \
                  --intent_loss_coef $c \
                  --learning_rate $lr \
                  --train_batch_size 32 \
                  --eval_batch_size 32
