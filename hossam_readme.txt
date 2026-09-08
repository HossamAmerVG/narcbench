export FLASHINFER_DISABLE_JIT=1
export VLLM_USE_FLASHINFER_SAMPLER=0


time bash scripts/run_model.sh Qwen/Qwen3-32B-AWQ


export CUDA_HOME=/opt/conda/lib/python3.12/site-packages/nvidia/cu13
export PATH=$CUDA_HOME/bin:$PATH
export LD_LIBRARY_PATH=$CUDA_HOME/lib:$LD_LIBRARY_PATH
