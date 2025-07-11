# pip install huggingface_hub
# python -c "from huggingface_hub import snapshot_download; snapshot_download(repo_id='Tengyunw/qwen3_8b_eagle3', local_dir='qwen3_8b_eagle3')"

import os
os.environ['HF_ENDPOINT'] = 'hf-mirror.com'

from huggingface_hub import snapshot_download; 
# snapshot_download(repo_id='Tengyunw/qwen3_8b_eagle3', local_dir='C:\llm_models\qwen3_8b_eagle3')
snapshot_download(repo_id='Tengyunw/qwen3_8b_eagle3', local_dir='C:\llm_models\qwen3_8b_eagle3')

